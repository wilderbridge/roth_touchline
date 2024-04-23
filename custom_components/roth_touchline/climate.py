import json
from datetime import timedelta
import logging
import logging.config

import async_timeout
from homeassistant.components.climate import (
    ClimateEntity,
    ClimateEntityFeature,
    HVACMode,
)
from homeassistant.const import ATTR_TEMPERATURE, UnitOfTemperature
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
    UpdateFailed,
)
from roth_touchline_sl_api_version_1_0_client.api.modules import (
    get_users_user_id_modules,
    get_users_user_id_modules_module_udid,
    zone_change,
)
from roth_touchline_sl_api_version_1_0_client.models import ZoneMode

_LOGGER = logging.getLogger(__name__)

LOGGING_CONFIG = {
    "version": 1,
    "handlers": {
        "default": {
            "class": "logging.StreamHandler",
            "formatter": "http",
            "stream": "ext://sys.stderr",
        }
    },
    "formatters": {
        "http": {
            "format": "%(levelname)s [%(asctime)s] %(name)s - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        }
    },
    "loggers": {
        "httpx": {"handlers": ["default"], "level": "DEBUG"},
        "httpcore": {"handlers": ["default"], "level": "DEBUG"},
    },
}

logging.config.dictConfig(LOGGING_CONFIG)


async def async_setup_entry(
    hass: HomeAssistant,
    config: ConfigType,
    async_add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Iterate through and add all Touchline devices."""
    api = hass.data["api"]
    user_id = hass.data["user_id"]
    module = hass.data["module"]
    modules_from_api = await get_users_user_id_modules.asyncio_detailed(
        client=api, user_id=user_id
    )

    udid = ""
    for module_in_api in json.loads(modules_from_api.content):
        if module_in_api["name"] == module:
            udid = module_in_api["udid"]

    coordinator = RothTouchlineCoordinator(hass, api, user_id, udid)
    await coordinator.async_config_entry_first_refresh()

    async_add_entities(
        RothTouchlineClimate(coordinator, idx)
        for idx, ent in enumerate(
            json.loads(coordinator.data.content)["zones"]["elements"]
        )
    )


class RothTouchlineCoordinator(DataUpdateCoordinator):
    def __init__(self, hass, api, user_id, udid):
        super().__init__(
            hass,
            _LOGGER,
            name="RothTouchline",
            update_interval=timedelta(seconds=60),
        )
        self.api = api
        self.user_id = user_id
        self.udid = udid

    async def _async_update_data(self):
        try:
            async with async_timeout.timeout(10):
                return await get_users_user_id_modules_module_udid.asyncio_detailed(
                    client=self.api, user_id=self.user_id, module_udid=self.udid
                )
        except Exception as err:
            raise UpdateFailed(f"Error communicating with API: {err}")

    async def _send_command(self, zone_change):
        try:
            async with async_timeout.timeout(10):
                return await zone_change.asyncio(
                    client=self.api,
                    user_id=self.user_id,
                    module_udid=self.udid,
                    body=zone_change,
                    modeOrZone="zone",
                )
        except Exception as err:
            raise UpdateFailed(f"Error communicating with API: {err}")

    async def set_temperature(self, zone_change):
        return await self._send_command(zone_change)

    async def toggle(self, zone_change):
        return await self._send_command(zone_change)


class RothTouchlineClimate(CoordinatorEntity, ClimateEntity):
    _attr_hvac_modes = [HVACMode.HEAT, HVACMode.OFF]
    _attr_supported_features = (
        ClimateEntityFeature.TARGET_TEMPERATURE
        | ClimateEntityFeature.TURN_OFF
        | ClimateEntityFeature.TURN_ON
    )
    _attr_temperature_unit = UnitOfTemperature.CELSIUS
    _enable_turn_on_off_backwards_compatibility = False

    def __init__(self, coordinator, idx):
        super().__init__(coordinator, context=idx)
        self._idx = idx
        if hasattr(self.coordinator.data, "content"):
            self.coordinator.data = json.loads(
                self.coordinator.data.content
            )["zones"]["elements"]
        zone_data = self.coordinator.data[self._idx]["zone"]
        self._id = zone_data["mode"]["id"]
        self._zone_id = zone_data["zone"]["id"]
        self._attr_unique_id = str(self._id)
        self._name = zone_data["description"]["name"]
        self._current_temperature = (
            zone_data["zone"]["currentTemperature"] / 10
            if zone_data["zone"]["currentTemperature"] is not None
            else None
        )
        self._target_temperature = (
            zone_data["mode"]["setTemperature"] / 10
            if zone_data["zone"]["setTemperature"] is not None
            else None
        )
        self._available = (
            zone_data["zone"]["signalStrength"] is not None
            and zone_data["zone"]["zoneState"] != "zoneUnregistered"
        )
        self._attr_entity_registry_enabled_default = (
            zone_data["zone"]["signalStrength"] is not None
        )
        self._extra_state_attributes = {
            "battery_level": zone_data["zone"]["batteryLevel"],
            "signal_strength": zone_data["zone"]["signalStrength"],
            "humidity": zone_data["zone"]["humidity"],
            "zoneState": zone_data["zone"]["zoneState"],
        }
        self._attr_hvac_mode = (
            HVACMode.OFF if zone_data["zone"]["zoneState"] == "zoneOff" else HVACMode.HEAT
        )

    @callback
    def _handle_coordinator_update(self) -> None:
        if hasattr(self.coordinator.data, "content"):
            self.coordinator.data = json.loads(
                self.coordinator.data.content
            )["zones"]["elements"]
        zone_data = self.coordinator.data[self._idx]["zone"]
        self._id = zone_data["mode"]["id"]
        self._zone_id = zone_data["zone"]["id"]
        self._attr_unique_id = self._id
        self._name = zone_data["description"]["name"]
        self._current_temperature = (
            zone_data["zone"]["currentTemperature"] / 10
            if zone_data["zone"]["currentTemperature"] is not None
            else None
        )
        self._target_temperature = (
            zone_data["mode"]["setTemperature"] / 10
            if zone_data["zone"]["setTemperature"] is not None
            else None
        )
        self._available = (
            zone_data["zone"]["signalStrength"] is not None
            and zone_data["zone"]["zoneState"] != "zoneUnregistered"
        )
        self._attr_entity_registry_enabled_default = (
            zone_data["zone"]["signalStrength"] is not None
        )
        self._extra_state_attributes = {
            "battery_level": zone_data["zone"]["batteryLevel"],
            "signal_strength": zone_data["zone"]["signalStrength"],
            "humidity": zone_data["zone"]["humidity"],
            "zoneState": zone_data["zone"]["zoneState"],
        }
        self._attr_hvac_mode = (
            HVACMode.OFF if zone_data["zone"]["zoneState"] == "zoneOff" else HVACMode.HEAT
        )
        self.async_write_ha_state()

    @property
    def name(self):
        """Return the name of the climate device."""
        return self._name

    async def async_set_hvac_mode(self, hvac_mode):
        if hvac_mode == "off":
            await self.async_turn_off()
        elif hvac_mode == HVACMode.HEAT:
            await self.async_turn_on()
        else:
            print("Unknown HVAC mode: " + hvac_mode)

    async def async_turn_on(self):
        zone_mode = ZoneMode(id=self._zone_id)
        zone_mode.additional_properties = {"zoneState": "zoneOn"}
        res = await self.coordinator.toggle(zone_mode)
        if res is not None:
            self._attr_hvac_mode = HVACMode.HEAT
            self._available = False
            self.async_write_ha_state()
            return True
        return False

    async def async_turn_off(self):
        zone_mode = ZoneMode(id=self._zone_id)
        zone_mode.additional_properties = {"zoneState": "zoneOff"}
        res = await self.coordinator.toggle(zone_mode)
        if res is not None:
            self._attr_hvac_mode = HVACMode.OFF
            self._available = False
            self.async_write_ha_state()
            return True
        return False

    @property
    def extra_state_attributes(self):
        return self._extra_state_attributes

    @property
    def current_temperature(self):
        return self._current_temperature

    @property
    def current_humidity(self):
        return self._extra_state_attributes["humidity"]

    @property
    def target_temperature(self):
        """Return the temperature we try to reach."""
        return self._target_temperature

    async def async_set_temperature(self, **kwargs: any) -> None:
        """Set new target temperature."""
        if ATTR_TEMPERATURE in kwargs:
            self._target_temperature = kwargs[ATTR_TEMPERATURE]
            zone_mode = ZoneMode(
                id=self._id,
                parent_id=self._parentId,
                mode="constantTemp",
                const_temp_time=0,
                set_temperature=int(kwargs[ATTR_TEMPERATURE] * 10),
                schedule_index=0,
            )
            res = await self.coordinator.set_temperature(zone_mode)
            return res is not None


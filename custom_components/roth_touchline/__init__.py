"""The roth_touchline integration."""

from __future__ import annotations

import voluptuous as vol

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.typing import ConfigType
from . import config_flow

from roth_touchline_sl_api_version_1_0_client import AuthenticatedClient, Client
from roth_touchline_sl_api_version_1_0_client.models import Token, User
from roth_touchline_sl_api_version_1_0_client.api.authentication import post_authentication
from roth_touchline_sl_api_version_1_0_client.types import Response

from .const import DOMAIN, CONF_MODULE, CONF_USERNAME, CONF_PASSWORD

USER_CONFIG_SCHEMA = vol.Schema({
    vol.Required(CONF_USERNAME): cv.string,
    vol.Required(CONF_PASSWORD): cv.string
})

PLATFORMS: list[Platform] = [Platform.CLIMATE]

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up components."""
    if DOMAIN not in config:
        return True

    conf = config[DOMAIN]
    username = conf.get(CONF_USERNAME)
    password = conf.get(CONF_PASSWORD)
    module = conf.get("module")

    hass.data.setdefault(DOMAIN, {})
    BASE_URL = "https://roth-touchlinesl.com/api/v1"

    # Create API instance
    client = Client(base_url=BASE_URL)

    # Validate the API connection (and authentication)
    user = User(username=username, password=password)
    async with client as client:
        token: Token = await post_authentication.asyncio(client=client, body=user)

    # Store an API object for your platforms to access
    api = AuthenticatedClient(base_url=BASE_URL, token=token.token)
    hass.data["api"] = api
    hass.data["user_id"] = token.user_id
    hass.data["module"] = module

    config_flow.register_flow_implementation(
        hass, conf[CONF_USERNAME], conf[CONF_PASSWORD], conf["module"]
    )

    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True

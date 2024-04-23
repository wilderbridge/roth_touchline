"""Config flow for roth_touchline integration."""

from __future__ import annotations

import json
import logging
from typing import Any

from roth_touchline_sl_api_version_1_0_client import AuthenticatedClient, Client
from roth_touchline_sl_api_version_1_0_client.api.authentication import (
    post_authentication,
)
from roth_touchline_sl_api_version_1_0_client.api.modules import (
    get_users_user_id_modules,
)
from roth_touchline_sl_api_version_1_0_client.models import (
    PostAuthenticationResponse401,
    Token,
    User,
)
import voluptuous as vol

from homeassistant.config_entries import ConfigFlow, ConfigFlowResult
from homeassistant.const import CONF_PASSWORD, CONF_USERNAME
from homeassistant.core import HomeAssistant, callback
from homeassistant.exceptions import HomeAssistantError
from homeassistant.helpers import config_validation as cv

from .const import BASE_URL, DOMAIN

USER_CONFIG_SCHEMA = vol.Schema(
    {vol.Required(CONF_USERNAME): cv.string, vol.Required(CONF_PASSWORD): cv.string}
)
_LOGGER = logging.getLogger(__name__)


@callback
def register_flow_implementation(
    hass: HomeAssistant, username: str, password: str, module: str
) -> None:
    hass.data.setdefault("touchline_sl_impl", {})

    hass.data["touchline_sl_impl"] = {
        CONF_USERNAME: username,
        CONF_PASSWORD: password,
        "module": module,
    }


class RothTouchlineHub:
    """Placeholder class to make tests pass.

    TODO Remove this placeholder class and replace with things from your PyPI package.
    """

    async def authenticate(self, username: str, password: str) -> bool:
        self._username = username
        self._password = password
        client = Client(base_url=BASE_URL)
        user = User(username=username, password=password)
        async with client as client:
            token: Token = await post_authentication.asyncio(client=client, body=user)
        if token is PostAuthenticationResponse401:
            return False
        elif token.user_id is not None:
            self._token = token.token
            self._user_id = token.user_id
            return True
        else:
            return False

    async def retrieve_sites(self):
        client = AuthenticatedClient(base_url=BASE_URL, token=self._token)
        async with client as client:
            modules = await get_users_user_id_modules.asyncio_detailed(
                client=client, user_id=self._user_id
            )
        modules = json.loads(modules.content)
        return [module["name"] for module in modules]


async def validate_input(
    hass: HomeAssistant, data: dict[str, Any], hub: RothTouchlineHub
) -> dict[str, Any]:

    if not await hub.authenticate(data[CONF_USERNAME], data[CONF_PASSWORD]):
        raise InvalidAuth

class ConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for roth_touchline."""

    VERSION = 1

    def __init__(self):
        self.hub = RothTouchlineHub()

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        errors: dict[str, str] = {}
        if user_input is not None:
            try:
                await validate_input(self.hass, user_input, self.hub)
            except CannotConnect:
                errors["base"] = "cannot_connect"
            except InvalidAuth:
                errors["base"] = "invalid_auth"
            except Exception:  # pylint: disable=broad-except
                _LOGGER.exception("Unexpected exception")
                errors["base"] = "unknown"
            else:
                return await self.async_step_site(user_input)

        return self.async_show_form(step_id="user", data_schema=USER_CONFIG_SCHEMA)

    async def async_step_site(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle the initial step."""
        errors: dict[str, str] = {}
        if user_input is not None and "module" in user_input:
            await self.async_set_unique_id(user_input["module"])
            return self.async_create_entry(title=user_input["module"], data=user_input)
        choices = await self.hub.retrieve_sites()
        if len(choices) == 0:
            return self.async_abort(reason="no_available_sites")
        return self.async_show_form(
            step_id="site",
            data_schema=vol.Schema({vol.Required("module"): vol.In(choices)}),
            errors=errors,
        )


class CannotConnect(HomeAssistantError):
    """Error to indicate we cannot connect."""


class InvalidAuth(HomeAssistantError):
    """Error to indicate there is invalid auth."""

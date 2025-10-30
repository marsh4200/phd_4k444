import voluptuous as vol
from homeassistant import config_entries
from .const import DOMAIN, DEFAULT_HOST, DEFAULT_PORT

class PHDConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title=f"PHD 4K444 ({user_input.get('host', DEFAULT_HOST)})", data=user_input)

        data_schema = vol.Schema({
            vol.Required('host', default=DEFAULT_HOST): str,
            vol.Required('port', default=DEFAULT_PORT): int,
        })
        return self.async_show_form(step_id='user', data_schema=data_schema)

    async def async_step_options(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title='', data=user_input)

        data_schema = vol.Schema({
            vol.Required('debug', default=False): bool,
        })
        return self.async_show_form(step_id='options', data_schema=data_schema)

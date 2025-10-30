import logging
from .const import DOMAIN, DEFAULT_HOST, DEFAULT_PORT
_LOGGER = logging.getLogger(__name__)

async def async_setup(hass, config):
    hass.data.setdefault(DOMAIN, {})
    return True

async def async_setup_entry(hass, entry):
    from .controller import PHDController
    host = entry.data.get("host", entry.options.get("host", DEFAULT_HOST))
    port = entry.data.get("port", entry.options.get("port", DEFAULT_PORT))
    debug = entry.options.get("debug", False)
    controller = PHDController(host, port, debug=debug)
    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = {"controller": controller, "entry": entry}
    await hass.config_entries.async_forward_entry_setups(entry, ["switch"])
    return True

async def async_unload_entry(hass, entry):
    await hass.config_entries.async_unload_platforms(entry, ["switch"])
    hass.data[DOMAIN].pop(entry.entry_id, None)
    return True

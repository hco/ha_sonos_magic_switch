"""Config flow for Sonos Magic Switch."""

from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_entry_flow, device_registry as dr

from .const import DOMAIN


async def _async_has_devices(hass: HomeAssistant) -> bool:
    """Return if there are devices that can be discovered."""
    # TODO Check if there are any devices that can be discovered in the network.
    #    devices = await hass.async_add_executor_job(my_pypi_dependency.discover)
    # return len(devices) > 0

    device_registry = dr.async_get(hass)
    print("printing devices in has_devices")
    # device_registry.devices contains all devices in the device registry.
    # iterate over all of them and print them
    for device in device_registry.devices.values():
        print(device)

    return True


config_entry_flow.register_discovery_flow(
    DOMAIN, "Sonos Magic Switch", _async_has_devices
)

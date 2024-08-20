from typing import Any

from homeassistant.components.switch import SwitchEntity
from homeassistant.core import State
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers.event import async_track_state_change_event


async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the Sonos Magic Switch platform."""
    """ print the config_entry object to see what it contains """

    device_registry = dr.async_get(hass)

    # device_registry.devices contains all devices in the device registry.
    # iterate over all of them and print them
    # for device in device_registry.devices.values():
    #     pprint.pp(device.identifiers)
    #     pprint.pprint(device)

    # filter all devices that contain a tuple whichs first element is "sonos" in the identifiers
    # and that have a name
    sonos_devices = [
        device
        for device in device_registry.devices.values()
        if any(identifier[0] == "sonos" for identifier in device.identifiers)
    ]

    async_add_entities(
        [SonosMagicSwitch(device) for device in sonos_devices if device.name]
    )


class SonosMagicSwitch(SwitchEntity):
    """Representation of a Sonos Magic Switch."""

    _original_device: dr.DeviceEntry
    _media_player_entity_id: str

    def __init__(self, device: dr.DeviceEntry):
        """Initialize the Sonos Magic Switch."""
        self._original_device = device
        """ abort if the device has no name """
        if not device.name:
            return

        self._attr_name = device.name + " Magic Switch"
        self._attr_unique_id = device.id + "_sonos_magic_switch"
        self._attr_is_on = False

        # get media_player entity_id from the device
        # mediay_player_entity_id = [
        #     identifier[1]
        #     for identifier in device.identifiers
        #     if identifier[0] == "sonos"
        # ][0]

        # unsub = async_track_state_change_event(self.hass)

    async def async_added_to_hass(self) -> None:
        """Run when this Entity has been added to HA."""
        # Importantly for a push integration, the module that will be getting updates
        # needs to notify HA of changes. The dummy device has a registercallback
        # method, so to this we add the 'self.async_write_ha_state' method, to be
        # called where ever there are changes.
        # The call back registration is done once this entity is registered with HA
        # (rather than in the __init__)
        # self._roller.register_callback(self.async_write_ha_state)
        self._media_player_entity_id = await self.__get_media_player_entity_id()

        if not self._media_player_entity_id:
            return

        self.unsub = async_track_state_change_event(
            self.hass, self._media_player_entity_id, self._media_player_state_changed
        )
        self.__update_entity_picture()
        await self._update_state_from_media_player()

    def __update_entity_picture(self):
        largest_group_state = self.__find_largest_group_of_media_players()

        if not largest_group_state:
            self._attr_entity_picture = None
            return

        self._attr_entity_picture = largest_group_state.entity_id

    async def __get_media_player_entity_id(self) -> str:
        entity_registry = er.async_get(self.hass)
        device_entities = er.async_entries_for_device(
            entity_registry, self._original_device.id
        )

        media_player = [
            entity
            for entity in device_entities
            if entity.entity_id.startswith("media_player.")
        ][0]

        return media_player.entity_id

    async def _media_player_state_changed(self, event):
        await self._update_state_from_media_player()

    async def _update_state_from_media_player(
        self,
    ):
        media_player_state = self.hass.states.get(self._media_player_entity_id)
        if not media_player_state:
            return

        self._attr_is_on = media_player_state.state == "playing"
        self.async_write_ha_state()

    async def async_will_remove_from_hass(self) -> None:
        """Entity being removed from hass."""
        # The opposite of async_added_to_hass. Remove any registered call backs here.
        if self.unsub:
            self.unsub()

    @property
    def device_info(self) -> dr.DeviceInfo:
        """Return the device info."""
        return dr.DeviceInfo(
            identifiers=self._original_device.identifiers,
        )

    def turn_on(self, **kwargs: Any) -> None:
        """Join group or start playing if no group exists."""
        if not self._media_player_entity_id:
            return

        largest_group_state = self.__find_largest_group_of_media_players()

        if not largest_group_state:
            self.hass.services.call(
                "media_player",
                "media_play",
                {"entity_id": self._media_player_entity_id},
            )
        else:
            self.hass.services.call(
                "media_player",
                "join",
                {
                    "entity_id": largest_group_state.entity_id,
                    "group_members": [self._media_player_entity_id]
                    + largest_group_state.attributes["group_members"],
                },
            )

    def __find_largest_group_of_media_players(self) -> State | None:
        entity_registry = er.async_get(self.hass)
        device_registry = dr.async_get(self.hass)

        media_player_states = [
            entity_state
            for entity in entity_registry.entities.values()
            if entity.entity_id.startswith("media_player.")
            if (device_id := entity.device_id)
            if (device := device_registry.async_get(device_id))
            if any(identifier[0] == "sonos" for identifier in device.identifiers)
            if (entity_state := self.hass.states.get(entity.entity_id)) is not None
            if entity_state.state == "playing"
        ]

        if not media_player_states:
            return None

        # sort the media players by the number of group members
        media_player_states.sort(
            key=lambda x: len(x.attributes.get("group_members", [])), reverse=True
        )

        return media_player_states[0]

    def turn_off(self, **kwargs: Any) -> None:
        """If the media player is alone, pause it, otherwise remove it from the group."""
        state = self.hass.states.get(self._media_player_entity_id)
        if not state:
            return

        if state.attributes["group_members"] == [self._media_player_entity_id]:
            self.hass.services.call(
                "media_player",
                "media_pause",
                {"entity_id": self._media_player_entity_id},
            )
        else:
            self.hass.services.call(
                "media_player",
                "unjoin",
                {"entity_id": self._media_player_entity_id},
            )

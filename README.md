# WORK IN PROGRESS

This is still a work in progress, and is not ready for use.

# Sonos Magic Switch Home Assistant Integration

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

Integration which adds a switch to SONOS players.
Turning it **on** will join the largest group of sonos players. If there is no playing group, it will try to start playing on the current player, with the last played source.

If you turn it **off**, it will leave the group, or stop playing.

**This integration will set up the following platforms.**

| Platform | Description                                        |
| -------- | -------------------------------------------------- |
| `switch` | Join or leave a sonos group, or start/stop playing |

## Installation:

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=hco&repository=ha-sonos-magic-switch&category=integration)

1. Go to HACS -> Integrations
1. Click the three dots on the top right and select `Custom Repositories`
1. Enter `https://github.com/hco/ha-sonos-magic-switch` as repository, select the category `Integration` and click Add
1. Go to Configuration -> Integrations
1. In the bottom right, click on the [Add Integration button](https://my.home-assistant.io/redirect/config_flow_start?domain=sonos_magic_switch), search for `Sonos Magic Switch` and click on it
1. Restart Home Assistant

## Configuration is done in the UI

<!---->

## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

---

[integration_blueprint]: https://github.com/hco/ha-sonos-magic-switch
[commits-shield]: https://img.shields.io/github/commit-activity/y/hco/ha-sonos-magic-switch.svg?style=for-the-badge
[commits]: https://github.com/hco/ha-sonos-magic-switch/commits/main
[exampleimg]: example.png
[license-shield]: https://img.shields.io/github/license/hco/ha-sonos-magic-switch.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/hco/ha-sonos-magic-switch.svg?style=for-the-badge
[releases]: https://github.com/hco/ha-sonos-magic-switch/releases

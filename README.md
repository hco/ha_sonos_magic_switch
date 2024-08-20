# WORK IN PROGRESS

This is still a work in progress, and is not ready for use.

# Sonos Magic Switch Home Assistant Integration

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

_Integration to integrate with [integration_blueprint][integration_blueprint]._

**This integration will set up the following platforms.**

| Platform | Description                                    |
| -------- | ---------------------------------------------- |
| `switch` | Join or leave a sonos group `True` or `False`. |

## Installation

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
1. If you do not have a `custom_components` directory (folder) there, you need to create it.
1. In the `custom_components` directory (folder) create a new folder called `integration_blueprint`.
1. Download _all_ the files from the `custom_components/integration_blueprint/` directory (folder) in this repository.
1. Place the files you downloaded in the new directory (folder) you created.
1. Restart Home Assistant
1. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Integration blueprint"

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

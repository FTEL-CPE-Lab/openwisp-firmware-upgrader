"""
Mapping between hardware models and firwmare image
This if focused on OpenWRT only fpr now, but it should
be possible to add support for different embedded
systems in the future.
"""
from collections import OrderedDict

from . import settings as app_settings

if app_settings.CUSTOM_OPENWRT_IMAGES:
    OPENWRT_FIRMWARE_IMAGE_MAP = OrderedDict(app_settings.CUSTOM_OPENWRT_IMAGES)
else:  # pragma: no cover
    OPENWRT_FIRMWARE_IMAGE_MAP = OrderedDict()

OPENWRT_FIRMWARE_IMAGE_MAP.update(
    OrderedDict(
        (
            (
                'ipq40xx-generic-nokia_wi2b-ac220i-squashfs-sysupgrade.bin',
                {'label': 'Nokia Airscale WI2B-AC220i', 'boards': ('Nokia Airscale WI2B-AC220i',)},
            ),
        )
    )
)

# OpenWRT only for now, in the future we'll merge
# different dictionaries representing different firmwares
# eg: AirOS, Raspbian
FIRMWARE_IMAGE_MAP = OPENWRT_FIRMWARE_IMAGE_MAP

# Allows getting type from image board
REVERSE_FIRMWARE_IMAGE_MAP = {}
# Choices used in model
FIRMWARE_IMAGE_TYPE_CHOICES = []

for key, info in FIRMWARE_IMAGE_MAP.items():
    FIRMWARE_IMAGE_TYPE_CHOICES.append((key, info['label']))
    for board in info['boards']:
        REVERSE_FIRMWARE_IMAGE_MAP[board] = key

####################################################################
# Asterfusion CX-N Devices Platform                                #
#                                                                  #
# Module contains an implementation of SONiC Platform Base API and #
# provides the platform information                                #
#                                                                  #
####################################################################

try:
    from .constants import *

    from sonic_platform_base.platform_base import PlatformBase
    from sonic_platform.chassis import Chassis
except ImportError as err:
    raise ImportError(str(err) + "- required module not found")


class Platform(PlatformBase):
    """Platform-specific Platform class"""

    def __init__(self):
        PlatformBase.__init__(self)
        self._chassis = Chassis()

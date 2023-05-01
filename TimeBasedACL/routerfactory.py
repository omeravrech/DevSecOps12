from interfaces import IFactory, IRouter
from ciscorouter import CiscoRouter
from enums import Vendors
from ping3 import ping
from socket import gethostbyname


class RouterFactory(IFactory):
    @classmethod
    def generate(cls, vendor: str, address: str, *args, **kwargs) -> IRouter:
        """ This class responsible for generating new device
        """
        vendor = getattr(Vendors, vendor.capitalize(), None)

        # Verify host is available
        if (address is None) or (ping(address, size=64, timeout=2, seq=1) == 0):
            return None

        kwargs["address"] = gethostbyname(address)

        if vendor == Vendors.Cisco:
            return CiscoRouter(**kwargs)

from interfaces import IFactory, IRouter
from ciscorouter import CiscoRouter
from enums import Vendors
from ping3 import ping

class RouterFactory(IFactory):
    @classmethod
    def generate(cls, vendor:str, address:str, *args, **kwargs) -> IRouter:
        vendor = getattr(Vendors,vendor.capitalize(),None)
        
        if (address is None) or (ping(address, size=64, timeout=2, seq=1) == 0):
            return None
        
        kwargs["address"] = address
        
        if vendor == Vendors.Cisco:
            return CiscoRouter(**kwargs)
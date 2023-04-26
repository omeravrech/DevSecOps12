from enums import UserMode

class IRouter:
    def __init__(self, **kwargs) -> None:
        for k, v in kwargs.items():
            setattr(self, f"_{k}", v)
        self._connected = False
    
    def is_connected(self) -> bool:
        return self._connected
    
    def connect(self) -> None:
        raise NotImplementedError()
    
    def check_user_mode(self) -> UserMode:
        raise NotImplementedError()
    
    def execute(self, commands) -> str:
        # Verify commands is a list
        if not isinstance(commands,list):
            raise TypeError("Commands must be an array of strings")
        raise NotImplementedError()
    
    def close(self) -> None:
        raise NotImplementedError()
    
    
class IFactory:
    @classmethod
    def generate(cls, vendor:str, address:str, *args, **kwargs) -> IRouter:
        raise NotImplementedError()
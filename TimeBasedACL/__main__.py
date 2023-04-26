from enums import UserMode
from interfaces import IRouter
from routerfactory import RouterFactory

host = input("Please enter router address: ")
username = input(f"Please enter the username for authenticate to {host}: ")
password = input(f"Now enter the password for authenticate to {host}: ")

# Generate router instance
router = RouterFactory.generate("cisco", host, username=username, password=password)

try:
    router.connect()
    mode = router.check_user_mode()
    if mode == UserMode.user:
        password = input(f"Please enter the password admin mode: ")
        router.execute(["enable", password])
    elif mode == UserMode.config:
        router.execute(["", "end"])
    
    if mode != UserMode.admin and router.check_user_mode() != UserMode.admin: # If previous check and new check still not equal to admin, then login failed
        raise ConnectionError()

    output = router.execute([
        "config t"
        "time-range TR_AUTOMATED_PY",
        "periodic daily 00:00 to 06:00",
        "!",
        "ip access-list extended ACL_IN_AUTOMATED_PY",
        "deny tcp any host <IP_ADDR> time-range TR_AUTOMATED_PY",
        "permit ip any any",
        "!",
        "ip access-list extended ACL_OUT_AUTOMATED_PY",
        "deny tcp host <IP_ADDR> any time-range TR_AUTOMATED_PY",
        "permit ip any any",
        "!",
        "interface <INTERFACE>",
        "ip access-group ACL_IN_AUTOMATED_PY in",
        "ip access-group ACL_OUT_AUTOMATED_PY out",
        "!",
        "end",
        "write",
        ""
    ])
except Exception as e:
    print("Error been accoured while running",e)
finally:
    router.close()
    
    
    
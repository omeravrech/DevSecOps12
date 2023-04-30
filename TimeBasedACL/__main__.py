from enums import UserMode
from routerfactory import RouterFactory
import re

COMMANDS_TO_EXECUTE = """
    ip access-list extended ACL_IN_AUTOMATED_PY
        deny tcp any host <IP_ADDR> time-range TR_AUTOMATED_PY
        permit ip any any
    !
    ip access-list extended ACL_OUT_AUTOMATED_PY
        deny tcp host <IP_ADDR> any time-range TR_AUTOMATED_PY
        permit ip any any
    !
    interface <INTERFACE>",
        ip access-group ACL_IN_AUTOMATED_PY in
        ip access-group ACL_OUT_AUTOMATED_PY out
    !
"""

router = None
host = input("Please enter router address: ")
username = input(f"Please enter the username for authenticate to {host}: ")
password = input(f"Now enter the password for authenticate to {host}: ")

try:
    # Generate router instance
    router = RouterFactory.generate("cisco", host, username=username, password=password)
    if router is None:
        raise ConnectionError("Can't open connection to {host}")

    print(f"Connecting to {host}...")
    router.connect()
    print(f"{host} is connected.")

    # Verify that we entered to admin console mode
    mode = router.check_user_mode()
    if mode == UserMode.user:
        password = input(f"Please enter the password admin mode: ")
        router.execute(["enable", password])
    elif mode == UserMode.config:
        router.execute(["", "end"])
    
    if mode != UserMode.admin and router.check_user_mode() != UserMode.admin: # If previous check and new check still not equal to admin, then login failed
        raise ConnectionError()

    # Extract interfaces with ip addresses
    output = router.execute(["term length 0", "show ip interface brief"])
    interfaces = re.finditer(r"(?P<intf_name>(^[a-zA-Z0-9\/-]+))( )+(?P<intf_addr>([0-9]{1,3}(\.)?){4})",
                             output,
                             re.MULTILINE)
    # Building the ACL configuration
    commands = "config t\n" \
               "    time-range TR_AUTOMATED_PY\n" \
               "        periodic daily 00:00 to 06:00\n" \
               "    !"
    # Iterate over interfaces with IPs
    for interface in interfaces:
        commands += COMMANDS_TO_EXECUTE\
                        .replace("<IP_ADDR>", interface.group("intf_addr"))\
                        .replace("<INTERFACE>", interface.group("intf_name"))
    # Cisco save command
    commands += "    end\nwrite\n\n!"

    print("Start configuring the following commands:\n", commands)
    output = router.execute(commands.split("\n"))
    print("Configuration been done.")

except Exception as e:
    print("Error been accorded while running", e)
finally:
    router.close()
    
    
    
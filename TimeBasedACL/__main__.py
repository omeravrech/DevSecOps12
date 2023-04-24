from interfaces import IRouter
from routerfactory import RouterFactory

host = input("Please enter router address: ")
username = input(f"Please enter the username for authenticate to {host}: ")
password = input(f"Now enter the password for authenticate to {host}: ")

router = RouterFactory.generate("cisco", host, username=username, password=password)
if isinstance(router,IRouter):
    router.connect()
    print(router.execute(["ll", "ls -la /"]))
    router.close()
    
    
    
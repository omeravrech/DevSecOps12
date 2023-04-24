from interfaces import IRouter
from routerfactory import RouterFactory

hostname = input("Please enter router address:")

router = RouterFactory.generate("cisco", hostname, port=22, username="root", password="system")
if isinstance(router,IRouter):
    router.connect()
    print(router.execute(["ll", "ls -la /"]))
    router.close()
    
    
    
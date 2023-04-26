from enum import Enum

class Vendors(Enum):
    Cisco = 1
    
class UserMode(Enum):
    user=0
    admin=1
    config=2

class Periodic(Enum):
    Daily=0         # Every day of the week
    Sunday=1
    Monday=2
    Tuesday=3
    Wednesday=4
    Thursday=5
    Friday=6
    Saturday=7
    Weekdays=8      # Monday thru Friday
    Weekend=9       # Saturday and Sunday
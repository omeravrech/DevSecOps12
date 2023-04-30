from enum import Enum


class Vendors(Enum):
    Cisco = 1


class UserMode(Enum):
    unclear = 0
    user = 1
    admin = 2
    config = 3

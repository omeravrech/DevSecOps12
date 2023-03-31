import requests


class User:
    def __init__(self, d:dict):
        self.__dict__ = d

    def __str__(self):
        name = getattr(self,"name")
        if name:
            return f"Name: {name}, Email: {getattr(self,'email')}"
        else:
            return f"I don't have name :("

class SpeedUser:
    @classmethod
    def generate(self) -> list[User]:
        result = []

        res = requests.get("https://jsonplaceholder.typicode.com/users", verify=False) # I add verify because on my computer I have security features that interfere in the traffic.
        if 200 > res.status_code or res.status_code > 299:
            return result
        
        users = res.json()
        for user in users:
            result.append(User(user))
        return result
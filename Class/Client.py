import requests
from random import randint

from Class.Menu import Menu
from Class.Farmer import Farmer


class Client:
    def __init__(self, user, password) -> None:
        self.user, self.password = user, password
        self.response = self.login()
        self.token = self.response['token']
        self.headers = {
            'Authorization': f'Bearer {self.token}',
            "Cookie": "PHPSESSID=" + str(randint(0, 1000))
        }
        self.farmer = Farmer(self)

    def login(self) -> dict:
        req = requests.post("https://leekwars.com/api/farmer/login-token",
                            data={"login": self.user, "password": self.password})
        return req.json()

    def run(self):
        Menu(self).intro()

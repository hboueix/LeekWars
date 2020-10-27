import requests


class Farmer:

    def __init__(self, client) -> None:
        self.client = client
        self.fights = client.response['farmer']['fights']
        self.leeks = client.response['farmer']['leeks']

    @property
    def garden(self) -> dict:
        req = requests.get(
            "https://leekwars.com/api/garden/get",
            headers=self.headers)
        return req.json()['garden']

    def solo_fight(self, leek_id, nb_fights):
        for i in range(nb_fights):
            response = requests.get(
                f"https://leekwars.com/api/garden/get-leek-opponents/{leek_id}", 
                headers=self.client.headers)
            # printjson(response.json())

            target = response.json()['opponents'][0]['id']

            response = requests.post(
                f"https://leekwars.com/api/garden/start-solo-fight", 
                data={"leek_id": leek_id, 
                    "target_id": target},
                headers=self.client.headers)
            # printjson(response.json())

    def get_leek_names(self) -> list:
        return [leek['name'] for id, leek in self.leeks.items()]

    def get_leek_id(self, leek_name) -> str:
        return [id for id, leek in self.leeks.items() if leek['name'] == leek_name][0]

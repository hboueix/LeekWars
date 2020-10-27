import asyncio
import requests
from tqdm import tqdm


class Farmer:

    def __init__(self, client) -> None:
        self.client = client
        self.id = client.response['farmer']['id']
        self.fights = client.response['farmer']['fights']
        self.leeks = client.response['farmer']['leeks']

    @property
    def garden(self) -> dict:
        req = requests.get(
            "https://leekwars.com/api/garden/get",
            headers=self.client.headers)
        return req.json()['garden']

    async def solo_fight(self, leek_id, nb_fights):
        id_fights = list()
        for i in tqdm(range(nb_fights)):
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
            self.fights -= 1
            # printjson(response.json())

            id_fights.append(response.json()['fight'])

        await asyncio.sleep(1)

        return self.sum_fights(id_fights)

    def sum_fights(self, id_fights):
        res = {'total': 0, 'win':0, 'loose': 0, 'tie': 0}
        for id_fight in id_fights:
            fight = self.get_fight(id_fight)
            win = self.is_fight_win(fight)
            res['total'] += 1
            if win != None:
                res['win'] += int(win)
                res['loose'] += int(not win)
            else:
                res['tie'] += 1
        return res

    def get_fight(self, fight_id):
        response = requests.get(
            f"https://leekwars.com/api/fight/get/{fight_id}",
            headers=self.client.headers)
        return response.json()

    def is_fight_win(self, fight):
        winner = fight['winner']
        if winner == 0:
            return None
        return (winner == 1 and str(self.id) in fight['farmers1'].keys()) \
            or (winner == 2 and (self.id) in fight['farmers2'].keys())

    def get_leek_names(self) -> list:
        return [leek['name'] for id, leek in self.leeks.items()]

    def get_leek_id(self, leek_name) -> str:
        return [id for id, leek in self.leeks.items() if leek['name'] == leek_name][0]

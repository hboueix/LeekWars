import requests
import json
from random import randint

from config import Config

USER = Config['USER']
PASSWORD = Config['PASSWORD']


def printjson(inline_json):
    print(json.dumps(inline_json, indent=4, sort_keys=True))


response = requests.post(f"https://leekwars.com/api/farmer/login-token",
                         data={"login": USER, "password": PASSWORD})
# printjson(response.json())
token = response.json()['token']
fights = response.json()['farmer']['fights']

headers = {'Authorization': f'Bearer {token}',
           "Cookie": "PHPSESSID=" + str(randint(0, 1000))}

response = requests.get(
    f"https://leekwars.com/api/garden/get", headers=headers)
# printjson(response.json())
garden = response.json()['garden']

HASHLEEK = 71075
LEEKHASH = 71203

for i in range(fights):
    response = requests.get(
        f"https://leekwars.com/api/garden/get-leek-opponents/{LEEKHASH}", headers=headers)
    # printjson(response.json())

    target = response.json()['opponents'][0]['id']
    # print(target)

    response = requests.post(f"https://leekwars.com/api/garden/start-solo-fight", data={
                             "leek_id": LEEKHASH, "target_id": target}, headers=headers)
    printjson(response.json())

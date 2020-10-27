from config import Config

from Class.Client import Client


client = Client(
    Config['LOGIN'], 
    Config['PASSWORD']
)

client.run()

HASHLEEK = 71075
LEEKHASH = 71203

# for i in range(farmer.fights):
#     response = requests.get(
#         f"https://leekwars.com/api/garden/get-leek-opponents/{LEEKHASH}", headers=farmer.headers)
#     # printjson(response.json())

#     target = response.json()['opponents'][0]['id']
#     # print(target)

#     response = requests.post(f"https://leekwars.com/api/garden/start-solo-fight", data={
#                              "leek_id": LEEKHASH, "target_id": target}, headers=farmer.headers)
#     printjson(response.json())

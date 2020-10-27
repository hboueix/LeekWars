from config import Config

from Class.Client import Client

client = Client(
    Config['LOGIN'],
    Config['PASSWORD']
)

client.run()

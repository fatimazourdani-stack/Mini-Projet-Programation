from pymongo import MongoClient
from urllib.parse import quote_plus


class EnregistreurDB:
    def __init__(self, username="abderraoufterrak_db_user",
                 password="Ez0Ugt79q5V8QX6U",
                 cluster="mini-projet.iveyqng.mongodb.net",
                 db_name="drone_energy"):
        encoded_password = quote_plus(password)
        uri = f"mongodb+srv://{username}:{encoded_password}@{cluster}/"
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db["mesures"]

    def inserer_mesure(self, mesure):
        self.collection.insert_one(mesure)

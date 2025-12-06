from modules.motor import MoteurDrone
from modules.mongo import EnregistreurDB
from modules.detect import Analyseur


moteurs = [MoteurDrone(i) for i in range(1, 5)]
enregistreur = EnregistreurDB()
analyseur = Analyseur()


for _ in range(2):
    for moteur in moteurs:
        mesure = moteur.generer_consommation()
        message = analyseur.verifier_anomalie(mesure)
        mesure["anomalie"] = message
        enregistreur.inserer_mesure(mesure)

        if message:
            print(message)

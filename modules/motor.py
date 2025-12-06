import random
import time


class MoteurDrone:
    def __init__(self, id_moteur, min_watt=20, max_watt=60):
        self.id = id_moteur
        self.min_watt = min_watt
        self.max_watt = max_watt

    def generer_consommation(self):
        return {
            "moteur_id": self.id,
            "consommation": round(
                random.uniform(self.min_watt, self.max_watt), 2
            ),
            "timestamp": time.time()
        }

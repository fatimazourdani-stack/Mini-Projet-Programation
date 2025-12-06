class Analyseur:
    def __init__(self, seuil_bas=30, seuil_haut=70):
        self.seuil_bas = seuil_bas
        self.seuil_haut = seuil_haut

    def verifier_anomalie(self, mesure):
        consommation = mesure["consommation"]
        if consommation < self.seuil_bas:
            return (
                f"⚠️ Anomalie: consommation trop basse "
                f"({consommation}W) - moteur {mesure['moteur_id']}"
            )
        elif consommation > self.seuil_haut:
            return (
                f"⚠️ Anomalie: consommation trop haute "
                f"({consommation}W) - moteur {mesure['moteur_id']}"
            )
        return None

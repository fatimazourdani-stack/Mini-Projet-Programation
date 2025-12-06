from modules.motor import MoteurDrone
from modules.detect import Analyseur
from modules.mongo import EnregistreurDB
import sys
from pathlib import Path


sys.path.insert(0, str(Path(__file__).parent.parent))


# ----- Moteur tests -----
def test_generer_consommation():
    moteur = MoteurDrone(1, 10, 50)
    mesure = moteur.generer_consommation()
    assert "moteur_id" in mesure
    assert "consommation" in mesure
    assert "timestamp" in mesure
    assert 10 <= mesure["consommation"] <= 50
    assert mesure["moteur_id"] == 1


# ----- Analyseur tests -----
def test_verifier_anomalie():
    analyseur = Analyseur(seuil_bas=20, seuil_haut=60)
    low = {"moteur_id": 1, "consommation": 10, "timestamp": 0}
    high = {"moteur_id": 1, "consommation": 70, "timestamp": 0}
    normal = {"moteur_id": 1, "consommation": 40, "timestamp": 0}
    assert "trop basse" in analyseur.verifier_anomalie(low)
    assert "trop haute" in analyseur.verifier_anomalie(high)
    assert analyseur.verifier_anomalie(normal) is None


# ----- DB tests -----
def test_connection():
    db = EnregistreurDB()
    db_names = db.client.list_database_names()
    assert isinstance(db_names, list)

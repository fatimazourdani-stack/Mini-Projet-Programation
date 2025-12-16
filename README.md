# Mini-Projet-Programation
Le mini projet de module Programation pour la formation doctoral 2024-2025
Made by:
SAADA Nesrine : nesrine.saada@ummto.dz  /  Doctorante en Électrotechnique industrielle
MADJOUDJ Abdeslam :      sara.bezzouh@ummto.dz  / Doctorante en Électrotechnique industrielle
ZOURDANI Fatima: fatima.zourdani@ummto.dz  / Doctorante en Reseaux electriques

1. L'intitule de projet
Ce projet simule le suivi et l’analyse de la consommation énergétique des moteurs d’un drone.
Il utilise la programmation orientée objet, la simulation de capteurs, la détection d’anomalies et le stockage des données dans MongoDB.


2. Fonctionnalités
Simulation de 4 moteurs de drone avec génération aléatoire de consommation.
Détection d’anomalies si la consommation est trop basse ou trop haute.
Stockage de toutes les mesures dans une collection unique MongoDB, incluant les anomalies.
Code testé avec Pytest et vérifié avec flake8 pour la qualité du code.


3. Structure du projet
WS/
 ├─ modules/
 │   ├─ __init__.py
 │   ├─ moteur.py
 │   ├─ analyseur.py
 │   └─ db.py
 ├─ tests/
 │   └─ test_all.py
 └─ main.py

modules/ → contient les classes du projet.
tests/ → contient les tests unitaires.
main.py → script principal pour exécuter la simulation.

4. Prérequis
Python 3.8+
MongoDB Atlas (ou local)
Bibliothèques Python :
pip install pymongo pytest flake8


5. Utilisation
Modifier le fichier modules/db.py pour renseigner votre username, password et cluster MongoDB.
Lancer le script principal :
python main.py
Les mesures et anomalies sont stockées dans MongoDB dans la collection mesures.
Les anomalies apparaissent dans le champ anomalie (ou null si aucune).


6. Tests unitaires
Pour exécuter les tests :
python -m pytest
Vérifie que toutes les fonctionnalités des modules fonctionnent correctement.


7. Qualité du code
Pour vérifier la conformité du code avec PEP8 :
flake8 modules/ tests/ main.py
Corrige les éventuelles erreurs de style et de formatage.

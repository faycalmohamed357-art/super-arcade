# storage.py - Sauvegarde et chargement de la partie en JSON

import json

FICHIER_SAUVEGARDE = "partie_empire.json"

def sauvegarder_partie(empire):
    """Convertit les données de l'objet empire en dictionnaire JSON."""
    donnees = {
        "nom": empire.nom,
        "pays": empire.pays,
        "argent": empire.argent,
        "petrole": empire.petrole,
        "niveau_qg": empire.niveau_qg,
        "tech_militaires": empire.tech_militaires,
        "tech_economie": empire.tech_economie,
        "soldats": empire.soldats,
        "blindes": empire.blindes,
        "territoires_conquis": empire.territoires_conquis,
        "pactes_non_agression": empire.pactes_non_agression,
        "alliance": empire.alliance
    }
    try:
        with open(FICHIER_SAUVEGARDE, "w", encoding="utf-8") as f:
            json.dump(donnees, f, indent=4, ensure_ascii=False)
        print("\n 💾 Partie sauvegardée avec succès dans partie_empire.json !")
    except IOError as e:
        print(f"\n ⚠️ Erreur lors de la sauvegarde : {e}")

def charger_partie():
    """Lit le fichier JSON et renvoie un dictionnaire ou None."""
    try:
        with open(FICHIER_SAUVEGARDE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None


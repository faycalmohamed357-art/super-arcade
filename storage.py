# storage.py - Gestion de la sauvegarde des scores

FICHIER_SCORES = "scores_permanents.txt"

def sauvegarder_score(nom, score):
    """Enregistre le score d'un joueur dans le fichier texte."""
    try:
        with open(FICHIER_SCORES, "a", encoding="utf-8") as f:
            f.write(f"{nom}:{score}\n")
        print(f" Score de {nom} ({score} pts) sauvegardé avec succès !")
    except IOError as e:
        print(f" Erreur lors de la sauvegarde du score : {e}")

def lire_scores():
    """Lit et retourne la liste des scores enregistrés."""
    scores = []
    try:
        with open(FICHIER_SCORES, "r", encoding="utf-8") as f:
            for ligne in f:
                ligne = ligne.strip()
                if ":" in ligne:
                    nom, score_str = ligne.split(":", 1)
                    scores.append((nom, int(score_str)))
    except FileNotFoundError:
        print(" Aucun fichier de score trouvé. Un nouveau sera créé au premier jeu.")
    except Exception as e:
        print(f" Erreur de lecture des scores : {e}")
    return scores


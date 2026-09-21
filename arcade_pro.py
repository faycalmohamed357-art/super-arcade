import random

FICHIER_SCORES = "scores_permanents.txt"

def sauvegarder_score(pseudo, score):
    with open(FICHIER_SCORES, "a") as f:
        f.write(f"{pseudo}:{score}\n")

def charger_scores():
    scores = []
    try:
        with open(FICHIER_SCORES, "r") as f:
            for ligne in f:
                if ":" in ligne:
                    nom, sc = ligne.strip().split(":")
                    scores.append((nom, int(sc)))
    except FileNotFoundError:
        pass
    return scores

def jouer(pseudo):
    secret = random.randint(1, 20)
    coups = 0
    print("\n--- DEVINER LE NOMBRE (1 à 20) ---")
    while True:
        essai = int(input("Ton choix : "))
        coups += 1
        if essai < secret:
            print("C'est PLUS !")
        elif essai > secret:
            print("C'est MOINS !")
        else:
            print(f"Gagné en {coups} coup(s) !")
            sauvegarder_score(pseudo, coups)
            break

def afficher_classement():
    scores = charger_scores()
    if not scores:
        print("\nAucun score enregistré.")
        return
    print("\n=== CLASSEMENT GENERAL ===")
    scores.sort(key=lambda x: x[1])  # Trie par meilleur score (plus bas)
    for i, (nom, sc) in enumerate(scores, 1):
        print(f"{i}. {nom} - {sc} coup(s)")

# --- PROGRAMME PRINCIPAL ---
pseudo = input("Entre ton pseudo de joueur : ")
while True:
    print("\n=========================")
    print("     SUPER ARCADE PRO    ")
    print("=========================")
    print("1. Jouer une partie")
    print("2. Voir le classement")
    print("3. Quitter")
    choix = input("> ")
    if choix == "1":
        jouer(pseudo)
    elif choix == "2":
        afficher_classement()
    elif choix == "3":
        print("À bientôt Pro !")
        break
    else:
        print("Choix invalide !")


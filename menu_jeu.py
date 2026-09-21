import random

# --- 1. FONCTION DE JEU ---
def jouer_partie():
    secret = random.randint(1, 10)
    tentatives = 0
    trouve = False
    
    print("\n--- NOUVELLE PARTIE ---")
    while not trouve:
        essai = int(input("Devine le nombre (1 à 10) : "))
        tentatives += 1
        
        if essai < secret:
            print("C'est PLUS grand !")
        elif essai > secret:
            print("C'est PLUS petit !")
        else:
            print(f"BRAVO ! Tu as trouvé en {tentatives} coup(s) !")
            trouve = True
            
    return tentatives  # On renvoie le score obtenu

# --- 2. FONCTION STATISTIQUES ---
def afficher_stats(liste_scores):
    if len(liste_scores) == 0:
        print("\n[!] Aucune partie jouée pour le moment.")
    else:
        print("\n=== HISTORIQUE ET SCORES ===")
        for i, score in enumerate(liste_scores, 1):
            print(f"Partie {i} : {score} coup(s)")
        
        moyenne = sum(liste_scores) / len(liste_scores)
        print(f"\nNombre de parties : {len(liste_scores)}")
        print(f"Meilleur score     : {min(liste_scores)} coup(s)")
        print(f"Moyenne des coups  : {round(moyenne, 2)}")

# --- 3. PROGRAMME PRINCIPAL ET MENU ---
historique_scores = []
en_cours = True

while en_cours:
    print("\n=========================")
    print("      SUPER ARCADE       ")
    print("=========================")
    print("1. Jouer une partie")
    print("2. Voir les scores")
    print("3. Quitter")
    
    choix = input("Fais ton choix (1, 2 ou 3) : ")
    
    if choix == "1":
        score_obtenu = jouer_partie()
        historique_scores.append(score_obtenu)
    elif choix == "2":
        afficher_stats(historique_scores)
    elif choix == "3":
        print("\nMerci d'avoir joué ! À bientôt 👋")
        en_cours = False
    else:
        print("\n[!] Choix invalide, entre 1, 2 ou 3.")


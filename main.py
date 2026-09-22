# main.py - Point d'entrée principal de l'Arcade

import storage
import games

def afficher_menu():
    print("\n==============================")
    print("   🎮 SUPER ARCADE PRO 🎮")
    print("==============================")
    print("1. Jouer à la Devinette")
    print("2. Voir le classement des scores")
    print("3. Quitter")
    print("==============================")

def afficher_classement():
    print("\n--- 🏆 CLASSEMENT GÉNÉRAL 🏆 ---")
    scores = storage.lire_scores()
    
    if not scores:
        print("Aucun score enregistré pour le moment.")
        return

    # Tri des scores du plus grand au plus petit
    scores_tries = sorted(scores, key=lambda x: x[1], reverse=True)
    
    for rang, (nom, score) in enumerate(scores_tries, start=1):
        print(f"{rang}. {nom} : {score} pts")

def main():
    nom_joueur = input("Entre ton pseudo : ").strip()
    if not nom_joueur:
        nom_joueur = "Joueur"

    while True:
        afficher_menu()
        choix = input("Choisis une option (1-3) : ").strip()

        if choix == "1":
            score_obtenu = games.jouer_devinette()
            if score_obtenu > 0:
                storage.sauvegarder_score(nom_joueur, score_obtenu)
        elif choix == "2":
            afficher_classement()
        elif choix == "3":
            print(f"\nAu revoir {nom_joueur} ! À bientôt sur Super Arcade Pro ! 👋")
            break
        else:
            print(" Choix invalide ! Veuillez entrer 1, 2 ou 3.")

if __name__ == "__main__":
    main()


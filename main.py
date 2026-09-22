# main.py - Version sécurisée

import storage
import games

def afficher_menu():
    print("\n==============================")
    print("   🎮 SUPER ARCADE PRO 🎮")
    print("==============================")
    print("1. Jouer à la Devinette")
    print("2. Voir le classement et statistiques")
    print("3. Quitter")
    print("==============================")

def afficher_classement_et_stats():
    print("\n--- 🏆 CLASSEMENT & STATISTIQUES 🏆 ---")
    scores = storage.lire_scores()
    
    if not scores:
        print("Aucun score enregistré pour le moment.")
        return

    # Utilisation d'un dictionnaire pour garder le meilleur score par joueur
    meilleurs_scores = {}
    total_points = 0
    
    for nom, score in scores:
        total_points += score
        if nom not in meilleurs_scores or score > meilleurs_scores[nom]:
            meilleurs_scores[nom] = score

    # Tri des meilleurs scores par joueur (du plus grand au plus petit)
    classement = sorted(meilleurs_scores.items(), key=lambda x: x[1], reverse=True)
    
    print("\n Top Joueurs (Meilleurs Scores) :")
    for rang, (nom, score) in enumerate(classement, start=1):
        print(f" {rang}. {nom} : {score} pts")
        
    print(f"\n Total des parties jouées : {len(scores)}")
    print(f" Moyenne des scores : {total_points / len(scores):.1f} pts")

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
            afficher_classement_et_stats()
        elif choix == "3":
            print(f"\nAu revoir {nom_joueur} ! À bientôt sur Super Arcade Pro ! 👋")
            break
        else:
            print(" Choix invalide ! Veuillez saisir uniquement 1, 2 ou 3.")

if __name__ == "__main__":
    main()


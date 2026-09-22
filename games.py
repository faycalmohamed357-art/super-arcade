# games.py - Logique des jeux de l'arcade

import random

def jouer_devinette():
    """Joue à une partie de devinette de nombre et retourne le score obtenu."""
    nombre_secret = random.randint(1, 20)
    tentatives = 0
    max_tentatives = 5
    
    print("\n---  Jeu de Devinette ---")
    print("J'ai choisi un nombre entre 1 et 20. À toi de deviner !")
    
    while tentatives < max_tentatives:
        try:
            essai = int(input(f"Essai {tentatives + 1}/{max_tentatives} - Ton nombre : "))
        except ValueError:
            print(" Entrée invalide ! Veuillez saisir un nombre entier.")
            continue
            
        tentatives += 1
        
        if essai < nombre_secret:
            print("C'est plus grand !")
        elif essai > nombre_secret:
            print("C'est plus petit !")
        else:
            # Calcul du score : plus on devine vite, plus on gagne de points
            score = (max_tentatives - tentatives + 1) * 20
            print(f" Bravo ! Tu as trouvé le nombre {nombre_secret} en {tentatives} coup(s) !")
            return score
            
    print(f" Perdu ! Le nombre secret était {nombre_secret}.")
    return 0


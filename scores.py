# --- 1. LES FONCTIONS ---

def calculer_moyenne(liste_scores):
    somme = sum(liste_scores)
    moyenne = somme / len(liste_scores)
    return moyenne

def afficher_podium(liste_scores):
    print("\n--- TOUS LES SCORES ---")
    # --- 2. LA BOUCLE FOR ---
    for score in liste_scores:
        print("- Score :", score, "tentative(s)")


# --- PROGRAMME PRINCIPAL ---

# Création d'une liste vide pour stocker les scores
mes_scores = []

# On demande 3 scores à l'utilisateur
for i in range(1, 4):
    s = int(input(f"Entre le score n°{i} : "))
    mes_scores.append(s)  # Ajoute le score dans la liste

# Utilisation des fonctions
afficher_podium(mes_scores)

moy = calculer_moyenne(mes_scores)
print("\nScore moyen :", round(moy, 2))
print("Meilleur score (le plus bas) :", min(mes_scores))


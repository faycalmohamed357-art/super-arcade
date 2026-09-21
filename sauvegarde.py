# --- 1. ÉCRIRE / AJOUTER DANS UN FICHIER ---
def sauvegarder_score(pseudo, score):
    # 'a' (append) ajoute le texte à la fin du fichier sans rien effacer
    with open("scores_permanents.txt", "a") as fichier:
        fichier.write(f"{pseudo} : {score} coup(s)\n")
    print("\n[+] Score enregistré sur le disque !")

# --- 2. LIRE LE FICHIER ---
def afficher_historique():
    print("\n=== HISTORIQUE PERMANENT (FICHIER TXT) ===")
    try:
        with open("scores_permanents.txt", "r") as fichier:
            contenu = fichier.read()
            print(contenu)
    except FileNotFoundError:
        print("[!] Aucun score n'a encore été enregistré.")

# --- PROGRAMME PRINCIPAL ---
nom = input("Entre ton pseudo : ")
coups = int(input("Entre ton score : "))

# Exécution des fonctions
sauvegarder_score(nom, coups)
afficher_historique()


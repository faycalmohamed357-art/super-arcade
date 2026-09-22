# main.py - Menu complet avec Recrutement & Conquête Militaire

import engine
import countries

def afficher_menu_empire():
    print("\n--- 🌐 MENU CONQUÊTE & STRATÉGIE 🌐 ---")
    print("1. Voir le statut de l'Empire")
    print("2. Recruter des Troupes (Soldats / Blindés)")
    print("3. Améliorer la Technologie Militaire (Armes)")
    print("4. Améliorer la Technologie Économique (Revenus)")
    print("5. ⚔️ Attaquer et Conquérir un Pays")
    print("6. Quitter le jeu")
    print("---------------------------------------")

def main():
    print("==========================================")
    print("    ⚔️ EMPIRES OF AFRICA & ASIA ⚔️")
    print("==========================================")
    
    nom = input("Entre ton nom de Souverain : ").strip()
    if not nom:
        nom = "Empereur"
        
    pays_valide = None
    while not pays_valide:
        saisie = input("\nChoisis ton pays de départ (ex: Chine, Niger, Inde...) : ")
        pays_valide = countries.valider_pays(saisie)
        if not pays_valide:
            print(" Pays non trouvé en Afrique ou Asie !")

    empire = engine.JoueurEmpire(nom, pays_valide)
    print(f"\n Félicitations ! Tu prends le contrôle de : {pays_valide}")

    while True:
        afficher_menu_empire()
        choix = input("Votre ordre, Majesté (1-6) : ").strip()

        if choix == "1":
            empire.afficher_statut()
        elif choix == "2":
            print("\n--- 🎖️ RECRUTEMENT ---")
            print("1. Soldats (10 $ l'unité)")
            print("2. Blindés (80 $ + 20 pétrole l'unité)")
            type_t = input("Choix (1-2) : ").strip()
            try:
                qte = int(input("Quantité : "))
                if type_t == "1":
                    empire.recruter_armee("soldat", qte)
                elif type_t == "2":
                    empire.recruter_armee("blinde", qte)
            except ValueError:
                print(" Nombre invalide !")
        elif choix == "3":
            empire.ameliorer_technologie("militaire")
        elif choix == "4":
            empire.ameliorer_technologie("economie")
        elif choix == "5":
            saisie_cible = input("\n⚔️ Quel pays d'Afrique ou d'Asie veux-tu attaquer ? : ")
            cible = countries.valider_pays(saisie_cible)
            if cible:
                empire.attaquer_pays(cible)
            else:
                print(" Pays introuvable !")
        elif choix == "6":
            print(f"\nSauvegarde du royaume de {nom}... À bientôt ! 👋")
            break
        else:
            print(" Ordre non reconnu !")

if __name__ == "__main__":
    main()


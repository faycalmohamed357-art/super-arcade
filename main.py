# main.py - Version étendue avec Marché, Espionnage & Événements

import engine
import countries
import storage

def afficher_menu_empire():
    print("\n--- 🌐 MENU CONQUÊTE & STRATÉGIE 🌐 ---")
    print("1. Voir le statut de l'Empire")
    print("2. Recruter des Troupes (Soldats / Blindés)")
    print("3. Améliorer la Technologie (Militaire / Économie)")
    print("4. 🛒 Marché Mondial (Acheter / Vendre Pétrole)")
    print("5. 🕵️ Espionnage (Infiltrer un pays)")
    print("6. 🤝 Diplomatie (Pactes & Alliances)")
    print("7. ⚔️ Attaquer et Conquérir un Pays")
    print("8. 💾 Sauvegarder et Quitter")
    print("---------------------------------------")

def main():
    print("==========================================")
    print("    ⚔️ EMPIRES OF AFRICA & ASIA ⚔️")
    print("==========================================")

    donnees = storage.charger_partie()
    empire = None

    if donnees:
        print(f"\nPartie trouvée pour : {donnees['nom']} ({donnees['pays']})")
        if input("Reprendre cette partie ? (o/n) : ").strip().lower() == 'o':
            empire = engine.JoueurEmpire.depuis_dictionnaire(donnees)

    if not empire:
        nom = input("\nNom du Souverain : ").strip() or "Empereur"
        pays_valide = None
        while not pays_valide:
            pays_valide = countries.valider_pays(input("Choisis ton pays de départ : "))
        empire = engine.JoueurEmpire(nom, pays_valide)

    while True:
        empire.declencher_evenement_aleatoire()
        afficher_menu_empire()
        choix = input("Votre ordre, Majesté (1-8) : ").strip()

        if choix == "1":
            empire.afficher_statut()
        elif choix == "2":
            print("\n1. Soldats (10 $) | 2. Blindés (80 $ + 20 Pétrole)")
            t = input("Choix (1-2) : ").strip()
            try:
                q = int(input("Quantité : "))
                empire.recruter_armee("soldat" if t == "1" else "blinde", q)
            except ValueError:
                print("Quantité invalide !")
        elif choix == "3":
            t = input("1. Militaire | 2. Économie : ").strip()
            empire.ameliorer_technologie("militaire" if t == "1" else "economie")
        elif choix == "4":
            print("\n--- 🛒 MARCHÉ MONDIAL ---")
            print("1. Acheter Pétrole (3 $ / unité)")
            print("2. Vendre Pétrole (2 $ / unité)")
            act = input("Choix (1-2) : ").strip()
            try:
                q = int(input("Quantité de pétrole : "))
                empire.commerce_marche("acheter" if act == "1" else "vendre", q)
            except ValueError:
                print("Quantité invalide !")
        elif choix == "5":
            cible = countries.valider_pays(input("Pays à espionner (150 $) : "))
            if cible:
                empire.espionner_pays(cible)
            else:
                print("Pays introuvable !")
        elif choix == "6":
            print("\n1. Pacte de Non-Agression (200 $) | 2. Rejoindre une Alliance")
            d = input("Choix (1-2) : ").strip()
            if d == "1":
                c = countries.valider_pays(input("Pays cible : "))
                if c: empire.proposer_pacte(c)
            elif d == "2":
                a = input("Nom de l'alliance : ").strip()
                if a: empire.rejoindre_alliance(a)
        elif choix == "7":
            c = countries.valider_pays(input("Pays à attaquer : "))
            if c: empire.attaquer_pays(c)
        elif choix == "8":
            storage.sauvegarder_partie(empire)
            print("\nPartie sauvegardée. À bientôt !")
            break

if __name__ == "__main__":
    main()


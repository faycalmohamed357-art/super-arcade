# main.py - Version complète avec Sauvegarde / Reprise JSON

import engine
import countries
import storage

def afficher_menu_empire():
    print("\n--- 🌐 MENU CONQUÊTE & STRATÉGIE 🌐 ---")
    print("1. Voir le statut de l'Empire")
    print("2. Recruter des Troupes (Soldats / Blindés)")
    print("3. Améliorer la Technologie (Militaire / Économie)")
    print("4. 🤝 Diplomatie : Signer un Pacte de Non-Agression")
    print("5. 🛡️ Diplomatie : Rejoindre / Créer une Alliance")
    print("6. ⚔️ Attaquer et Conquérir un Pays")
    print("7. 💾 Sauvegarder et Quitter")
    print("---------------------------------------")

def main():
    print("==========================================")
    print("    ⚔️ EMPIRES OF AFRICA & ASIA ⚔️")
    print("==========================================")

    donnees_sauvegardees = storage.charger_partie()
    empire = None

    if donnees_sauvegardees:
        print(f"\nUne partie sauvegardée a été trouvée pour : {donnees_sauvegardees['nom']} ({donnees_sauvegardees['pays']})")
        reprise = input("Voulez-vous reprendre cette partie ? (o/n) : ").strip().lower()
        if reprise == 'o':
            empire = engine.JoueurEmpire.depuis_dictionnaire(donnees_sauvegardees)
            print(f"\n Empire de {empire.pays} réarmé et prêt !")

    if not empire:
        nom = input("\nEntre ton nom de Souverain : ").strip()
        if not nom:
            nom = "Empereur"
            
        pays_valide = None
        while not pays_valide:
            saisie = input("Choisis ton pays de départ (ex: Chine, Niger, Inde...) : ")
            pays_valide = countries.valider_pays(saisie)
            if not pays_valide:
                print(" Pays non trouvé en Afrique ou Asie !")

        empire = engine.JoueurEmpire(nom, pays_valide)
        print(f"\n Félicitations ! Tu prends le contrôle de : {pays_valide}")

    while True:
        afficher_menu_empire()
        choix = input("Votre ordre, Majesté (1-7) : ").strip()

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
            print("\n--- 🧬 ARBRE TECHNOLOGIQUE ---")
            print("1. Technologie Militaire (Bonus de Dégâts)")
            print("2. Technologie Économique (Bonus de Revenus)")
            t_choice = input("Choix (1-2) : ").strip()
            if t_choice == "1":
                empire.ameliorer_technologie("militaire")
            elif t_choice == "2":
                empire.ameliorer_technologie("economie")
        elif choix == "4":
            saisie_cible = input("\n📜 Avec quel pays veux-tu signer un pacte ? : ")
            cible = countries.valider_pays(saisie_cible)
            if cible:
                empire.proposer_pacte(cible)
            else:
                print(" Pays introuvable !")
        elif choix == "5":
            nom_all = input("\n🛡️ Entre le nom de l'Alliance : ").strip()
            if nom_all:
                empire.rejoindre_alliance(nom_all)
        elif choix == "6":
            saisie_cible = input("\n⚔️ Quel pays d'Afrique ou d'Asie veux-tu attaquer ? : ")
            cible = countries.valider_pays(saisie_cible)
            if cible:
                empire.attaquer_pays(cible)
            else:
                print(" Pays introuvable !")
        elif choix == "7":
            storage.sauvegarder_partie(empire)
            print(f"\nSauvegarde terminée. À bientôt, Souverain {empire.nom} ! 👋")
            break
        else:
            print(" Ordre non reconnu !")

if __name__ == "__main__":
    main()


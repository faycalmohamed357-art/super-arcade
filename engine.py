# engine.py - Moteur de jeu : Économie, Armée, Recherche, Guerre & Diplomatie

import random
import countries

class JoueurEmpire:
    def __init__(self, nom, pays):
        self.nom = nom
        self.pays = pays
        self.argent = 1500
        self.petrole = 800
        self.niveau_qg = 1
        
        # Technologies
        self.tech_militaires = 1
        self.tech_economie = 1
        
        # Armée
        self.soldats = 100
        self.blindes = 10
        
        # Territoires & Diplomatie
        self.territoires_conquis = [pays]
        self.pactes_non_agression = []
        self.alliance = None

    def afficher_statut(self):
        bonus_alliance = 1.2 if self.alliance else 1.0
        puissance_militaire = int(((self.soldats * 10 + self.blindes * 50) * self.tech_militaires) * bonus_alliance)
        
        print(f"\n==========================================")
        print(f" 🏰 EMPIRE : {self.pays.upper()} (Souverain : {self.nom})")
        print(f"==========================================")
        print(f"💰 Argent : {self.argent} $ | 🛢️ Pétrole : {self.petrole}")
        print(f"🏛️ Niveau du QG : {self.niveau_qg}")
        print(f"🧬 Tech Militaire : Niv. {self.tech_militaires} | Tech Économie : Niv. {self.tech_economie}")
        print(f"🎖️ Armée : {self.soldats} Soldats | 🪖 {self.blindes} Blindés")
        print(f"⚔️ Puissance de combat totale : {puissance_militaire} pts")
        print(f"🤝 Alliance actuelle : {self.alliance if self.alliance else 'Aucune'}")
        print(f"📜 Pactes signés : {', '.join(self.pactes_non_agression) if self.pactes_non_agression else 'Aucun'}")
        print(f"🗺️ Territoires contrôlés ({len(self.territoires_conquis)}) : {', '.join(self.territoires_conquis)}")
        print(f"==========================================")

    def recruter_armee(self, type_troupe, quantite):
        cout_unitaire_argent = 10 if type_troupe == "soldat" else 80
        cout_unitaire_petrole = 0 if type_troupe == "soldat" else 20
        
        total_argent = cout_unitaire_argent * quantite
        total_petrole = cout_unitaire_petrole * quantite
        
        if self.argent >= total_argent and self.petrole >= total_petrole:
            self.argent -= total_argent
            self.petrole -= total_petrole
            if type_troupe == "soldat":
                self.soldats += quantite
                print(f"\n 🎖️ {quantite} soldats ont rejoint l'armée !")
            else:
                self.blindes += quantite
                print(f"\n 🪖 {quantite} véhicules blindés ont été construits !")
        else:
            print(f"\n Ressources insuffisantes ! Nécessaire : {total_argent} $ et {total_petrole} pétrole.")

    def ameliorer_technologie(self, type_tech):
        cout = 300 * (self.tech_militaires if type_tech == "militaire" else self.tech_economie)
        if self.argent >= cout:
            self.argent -= cout
            if type_tech == "militaire":
                self.tech_militaires += 1
                print(f"\n 🧬 Recherche militaire terminée ! Armes améliorées au Niveau {self.tech_militaires} !")
            else:
                self.tech_economie += 1
                print(f"\n 🧬 Recherche économique terminée ! Revenus augmentés au Niveau {self.tech_economie} !")
        else:
            print(f"\n Fonds insuffisants ! Nécessaire : {cout} $")

    def proposer_pacte(self, cible):
        if cible in self.territoires_conquis:
            print("\n Impossible de signer un pacte avec un territoire que vous contrôlez déjà !")
            return
        if cible in self.pactes_non_agression:
            print(f"\n Un pacte de non-agression est déjà actif avec {cible}.")
            return
            
        cout_pacte = 200
        if self.argent >= cout_pacte:
            self.argent -= cout_pacte
            self.pactes_non_agression.append(cible)
            print(f"\n 📜 Traité signé ! {cible} a accepté ton pacte de non-agression (-200 $).")
        else:
            print("\n Fonds insuffisants pour négocier un pacte (200 $ requis).")

    def rejoindre_alliance(self, nom_alliance):
        if self.alliance == nom_alliance:
            print(f"\n Vous faites déjà partie de {nom_alliance} !")
            return
            
        self.alliance = nom_alliance
        print(f"\n 🤝 Félicitations ! Votre Empire a rejoint l'alliance '{nom_alliance}' !")
        print(" 🔥 Bonus actif : +20% de puissance militaire globale !")

    def attaquer_pays(self, cible):
        if cible in self.territoires_conquis:
            print(f"\n Ce territoire ({cible}) fait déjà partie de ton empire !")
            return

        if cible in self.pactes_non_agression:
            print(f"\n Impossible d'attaquer {cible} ! Un pacte de non-agression est en cours.")
            return

        if self.soldats < 10:
            print("\n Armée insuffisante pour lancer une invasion ! Recrute au moins 10 soldats.")
            return

        bonus_alliance = 1.2 if self.alliance else 1.0
        ma_puissance = int(((self.soldats * 10 + self.blindes * 50) * self.tech_militaires) * bonus_alliance)
        
        defensifs_soldats = random.randint(30, 200)
        defensifs_blindes = random.randint(2, 25)
        puissance_ennemie = (defensifs_soldats * 10 + defensifs_blindes * 50)
        
        print(f"\n⚔️ ---------------- BATAILLE DE {cible.upper()} ---------------- ⚔️")
        print(f" 🚀 Ta Puissance : {ma_puissance} pts vs 🛡️ Défense Ennemie : {puissance_ennemie} pts")
        
        pertes_soldats = min(self.soldats, random.randint(5, 20))
        pertes_blindes = min(self.blindes, random.randint(0, 3))
        self.soldats -= pertes_soldats
        self.blindes -= pertes_blindes

        if ma_puissance > puissance_ennemie:
            butin_or = random.randint(400, 1200)
            butin_petrole = random.randint(200, 600)
            self.argent += butin_or
            self.petrole += butin_petrole
            self.territoires_conquis.append(cible)
            print(f" VICTOIRE ÉCLATANTE ! {cible} a été conquis et ajouté à ton empire !")
            print(f" 💰 Butin volé : +{butin_or} $ | 🛢️ +{butin_petrole} Pétrole")
        else:
            print(f" DÉFAITE ! L'armée de {cible} a repoussé tes troupes.")
            
        print(f" ⚰️ Pertes subies : -{pertes_soldats} soldats, -{pertes_blindes} blindés.")
        print("---------------------------------------------------------------")


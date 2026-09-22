# engine.py - Moteur complet avec Diplomatie, Sauvegarde, Événements, Espionnage & Marché

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

    @classmethod
    def depuis_dictionnaire(cls, d):
        empire = cls(d["nom"], d["pays"])
        empire.argent = d["argent"]
        empire.petrole = d["petrole"]
        empire.niveau_qg = d["niveau_qg"]
        empire.tech_militaires = d["tech_militaires"]
        empire.tech_economie = d["tech_economie"]
        empire.soldats = d["soldats"]
        empire.blindes = d["blindes"]
        empire.territoires_conquis = d["territoires_conquis"]
        empire.pactes_non_agression = d["pactes_non_agression"]
        empire.alliance = d["alliance"]
        return empire

    def declencher_evenement_aleatoire(self):
        """Génère un événement imprévu à chaque tour."""
        chance = random.random()
        if chance < 0.15:  # 15% de chance
            gain_or = random.randint(300, 700)
            self.argent += gain_or
            print(f"\n 📈 [ÉVÉNEMENT] Croissance économique imprevue ! Gain de +{gain_or} $ !")
        elif chance < 0.25: # 10% de chance
            gisement = random.randint(200, 500)
            self.petrole += gisement
            print(f"\n 🛢️ [ÉVÉNEMENT] Découverte d'un nouveau gisement de pétrole (+{gisement} pétrole) !")
        elif chance < 0.35: # 10% de chance
            perte = random.randint(100, 300)
            if self.argent >= perte:
                self.argent -= perte
                print(f"\n 🌪️ [ÉVÉNEMENT] Tempête majeure subie ! Réparations : -{perte} $.")

    def afficher_statut(self):
        bonus_alliance = 1.2 if self.alliance else 1.0
        puissance_militaire = int(((self.soldats * 10 + self.blindes * 50) * self.tech_militaires) * bonus_alliance)
        
        print(f"\n==========================================")
        print(f" 🏰 EMPIRE : {self.pays.upper()} (Souverain : {self.nom})")
        print(f"==========================================")
        print(f"💰 Argent : {self.argent} $ | 🛢️ Pétrole : {self.petrole}")
        print(f"🧬 Tech Militaire : Niv. {self.tech_militaires} | Tech Économie : Niv. {self.tech_economie}")
        print(f"🎖️ Armée : {self.soldats} Soldats | 🪖 {self.blindes} Blindés")
        print(f"⚔️ Puissance de combat globale : {puissance_militaire} pts")
        print(f"🤝 Alliance : {self.alliance if self.alliance else 'Aucune'}")
        print(f"📜 Pactes : {', '.join(self.pactes_non_agression) if self.pactes_non_agression else 'Aucun'}")
        print(f"🗺️ Territoires ({len(self.territoires_conquis)}) : {', '.join(self.territoires_conquis)}")
        print(f"==========================================")

    def recruter_armee(self, type_troupe, quantite):
        cout_argent = 10 * quantite if type_troupe == "soldat" else 80 * quantite
        cout_petrole = 0 if type_troupe == "soldat" else 20 * quantite
        
        if self.argent >= cout_argent and self.petrole >= cout_petrole:
            self.argent -= cout_argent
            self.petrole -= cout_petrole
            if type_troupe == "soldat":
                self.soldats += quantite
                print(f"\n 🎖️ {quantite} soldats recrutés !")
            else:
                self.blindes += quantite
                print(f"\n 🪖 {quantite} blindés construits !")
        else:
            print("\n Fonds ou pétrole insuffisants !")

    def commerce_marche(self, action, quantite):
        """Marché mondial : Achat / Vente de pétrole."""
        prix_achat = 3   # 1 Pétrole = 3 $
        prix_vente = 2   # 1 Pétrole = 2 $
        
        if action == "acheter":
            total = quantite * prix_achat
            if self.argent >= total:
                self.argent -= total
                self.petrole += quantite
                print(f"\n 🛒 Achat réussi : +{quantite} pétrole pour {total} $ !")
            else:
                print("\n Argent insuffisant !")
        elif action == "vendre":
            if self.petrole >= quantite:
                self.petrole -= quantite
                gain = quantite * prix_vente
                self.argent += gain
                print(f"\n 💵 Vente réussie : +{gain} $ pour {quantite} pétrole !")
            else:
                print("\n Pétrole insuffisant !")

    def espionner_pays(self, cible):
        """Espionne la puissance d'un pays ennemi contre de l'argent."""
        cout_espionnage = 150
        if self.argent >= cout_espionnage:
            self.argent -= cout_espionnage
            defensifs_soldats = random.randint(30, 200)
            defensifs_blindes = random.randint(2, 25)
            puissance_estimee = (defensifs_soldats * 10 + defensifs_blindes * 50)
            
            print(f"\n 🕵️ [RAPPORT D'ESPIONNAGE SUR {cible.upper()}]")
            print(f" 📊 Troupes estimées : ~{defensifs_soldats} Soldats, ~{defensifs_blindes} Blindés.")
            print(f" ⚔️ Puissance totale estimée : ~{puissance_estimee} pts.")
        else:
            print("\n Fonds insuffisants (150 $ requis pour payer les espions).")

    def ameliorer_technologie(self, type_tech):
        cout = 300 * (self.tech_militaires if type_tech == "militaire" else self.tech_economie)
        if self.argent >= cout:
            self.argent -= cout
            if type_tech == "militaire":
                self.tech_militaires += 1
                print(f"\n 🧬 Tech Militaire niveau {self.tech_militaires} atteinte !")
            else:
                self.tech_economie += 1
                print(f"\n 🧬 Tech Économique niveau {self.tech_economie} atteinte !")
        else:
            print(f"\n Fonds insuffisants ({cout} $ requis) !")

    def proposer_pacte(self, cible):
        if cible in self.territoires_conquis or cible in self.pactes_non_agression:
            print("\n Pacte impossible ou déjà existant.")
            return
        if self.argent >= 200:
            self.argent -= 200
            self.pactes_non_agression.append(cible)
            print(f"\n 📜 Pacte signé avec {cible} (-200 $).")
        else:
            print("\n Fonds insuffisants (200 $ requis).")

    def rejoindre_alliance(self, nom_alliance):
        self.alliance = nom_alliance
        print(f"\n 🤝 Empire intégré à l'alliance '{nom_alliance}' (+20% puissance) !")

    def attaquer_pays(self, cible):
        if cible in self.territoires_conquis or cible in self.pactes_non_agression:
            print("\n Attaque impossible (territoire déjà à toi ou sous pacte).")
            return
        if self.soldats < 10:
            print("\n Au moins 10 soldats sont requis pour lancer une invasion !")
            return

        bonus = 1.2 if self.alliance else 1.0
        ma_puissance = int(((self.soldats * 10 + self.blindes * 50) * self.tech_militaires) * bonus)
        
        puissance_ennemie = (random.randint(30, 200) * 10 + random.randint(2, 25) * 50)
        
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
            print(f"\n ⚔️ VICTOIRE ! {cible} conquis ! (+{butin_or} $, +{butin_petrole} Pétrole)")
        else:
            print(f"\n ⚔️ DÉFAITE ! L'armée de {cible} a repoussé ton assaut.")
            
        print(f" ⚰️ Pertes : -{pertes_soldats} soldats, -{pertes_blindes} blindés.")


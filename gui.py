# gui.py - Interface Tactile Kivy pour Empires of Africa & Asia

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import engine

class GameScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', spacing=10, padding=20, **kwargs)
        
        self.empire = engine.JoueurEmpire("Empereur", "Chine")
        
        # Titre
        self.title_label = Label(
            text="⚔️ EMPIRES OF AFRICA & ASIA ⚔️", 
            font_size='22sp', 
            size_hint=(1, 0.1)
        )
        self.add_widget(self.title_label)
        
        # Affichage du statut
        self.status_label = Label(
            text=f"Empire: {self.empire.pays} | Argent: {self.empire.argent} $ | Pétrole: {self.empire.petrole} | Soldats: {self.empire.soldats}", 
            font_size='14sp',
            size_hint=(1, 0.2)
        )
        self.add_widget(self.status_label)
        
        # Zone de Boutons Tactiles
        self.btn_recruter = Button(text="🎖️ Recruter 10 Soldats (100 $)", size_hint=(1, 0.15))
        self.btn_recruter.bind(on_press=self.action_recruter)
        self.add_widget(self.btn_recruter)
        
        self.btn_marche = Button(text="🛒 Acheter 50 Pétrole (150 $)", size_hint=(1, 0.15))
        self.btn_marche.bind(on_press=self.action_marche)
        self.add_widget(self.btn_marche)

    def rafraichir_ecran(self):
        self.status_label.text = f"Empire: {self.empire.pays} | Argent: {self.empire.argent} $ | Pétrole: {self.empire.petrole} | Soldats: {self.empire.soldats}"

    def action_recruter(self, instance):
        self.empire.recruter_armee("soldat", 10)
        self.rafraichir_ecran()

    def action_marche(self, instance):
        self.empire.commerce_marche("acheter", 50)
        self.rafraichir_ecran()

class EmpiresApp(App):
    def build(self):
        return GameScreen()

if __name__ == "__main__":
    EmpiresApp().run()


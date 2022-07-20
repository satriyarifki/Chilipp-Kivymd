from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from screens.home import Home
from kivymd.uix.card import MDCard
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
import json

class ShadowCard(MDCard, RoundedRectangularElevationBehavior):
    pass

class Botnav(MDScreen):
    def get_nama(self):
        f = open('store/user.json')
        data = json.load(f)
        # print(data['nama'])
        return data['nama']
    
    pass
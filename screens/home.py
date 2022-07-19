import json
import time
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivymd.uix.card import MDCard
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.behaviors import BackgroundColorBehavior
<<<<<<< HEAD

=======
>>>>>>> 4576bfda3c27395795f1d401d0aa8bb208b562b9


class ShadowCard(MDCard, RoundedRectangularElevationBehavior):
    pass


class Home(MDScreen):

    def __init__(self, **kw):
        Builder.load_file("kv/home.kv")
        super().__init__(**kw)
<<<<<<< HEAD
    def get_nama(self):
        f = open('store/user.json')
        data = json.load(f)
        # print(data['nama'])
        return data['nama']
    
        
        
=======

    
>>>>>>> 4576bfda3c27395795f1d401d0aa8bb208b562b9

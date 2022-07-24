import json
import time
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivymd.uix.card import MDCard
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.behaviors import BackgroundColorBehavior
import json
import requests
from system.base_url import base_url


class ShadowCard(MDCard, RoundedRectangularElevationBehavior):
    pass


class Home(MDScreen):

    def __init__(self, **kw):
        Builder.load_file("kv/home.kv")
        super().__init__(**kw)

    def get_volume(self):
        store = requests.get(base_url() + '/dataset/ketersediaan').json()

        list_data = {
            'tanggal': store['tanggal'],
            'jumlah_data': store['jumlah_data'],
            'total': store['total']
        }

        return list_data

    def volume(self):
        df = self.get_volume()
        volume = df['total']
        return f'{volume:,} Kilogram'

from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivymd.uix.card import MDCard
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.behaviors import BackgroundColorBehavior
from mysqlx import get_session
from login import Login


class ShadowCard(MDCard, RoundedRectangularElevationBehavior):
    pass


class Home(MDScreen):
    def __init__(self, **kw):
        Builder.load_file("kv/home.kv")
        super().__init__(**kw)
        
    def get_nama(self):
        nama = Login().get_session()
        
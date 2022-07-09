from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

class Splash(MDScreen):
    def __init__(self, **kw):
        Builder.load_file("kv/splash.kv")
        super().__init__(**kw)
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

class Login(MDScreen):
    def __init__(self, **kw):
        Builder.load_file("kv/login.kv")
        super().__init__(**kw)
from audioop import add
from email.mime import base
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
import json
from matplotlib.pyplot import cla
import requests
from system.base_url import base_url

# base_url = 'http://localhost:8000/api'


class Login(MDScreen):
    def __init__(self, **kw):
        Builder.load_file("kv/login.kv")
        super().__init__(**kw)

    def auth(self):
        global jsonData
        dataJson = {
            'email': self.ids.email.text,
            'password': self.ids.password.text
        }
        store = requests.post(base_url() + '/login', json=dataJson)

        jsonData = store.text
        if store.status_code == 200:
            # print(store['email'])
            print(store.text, '\n')

            self.manager.current = 'botnav'
        else:
            print('gagal login')

    def get_session(self):
        data = jsonData.split()
        print(type(data[0]))

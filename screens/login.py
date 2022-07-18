from audioop import add
from email.mime import base
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
import json
from matplotlib.pyplot import cla
import requests
from system.base_url import base_url
from kivymd.toast import toast

# base_url = 'http://localhost:8000/api'


class Login(MDScreen):
    def __init__(self, **kw):
        Builder.load_file("kv/login.kv")
        super().__init__(**kw)

    def auth(self):
        global jsonData
        _email = self.ids.email.text
        _password = self.ids.password.text

        if _email == '' and _password == '':
            toast('Email dan Password tidak boleh kosong')
        else:
            # toast('OK')

            dataJson = {
                'email': _email,
                'password': _password
            }
            store = requests.post(base_url() + '/login', json=dataJson)
            # data = store.json()
            # jsonData = store.text
            data = json.loads(store.text)

            if store.status_code == 200:
                # print(store.text, '\n')
                print(data['email'])
                # self.manager.current = 'botnav'
                toast('Berhasil Login')
            else:
                toast('Gagal Login')

    def get_session(self):
        data = jsonData.split()
        print(type(data[0]))

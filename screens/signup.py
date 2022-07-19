from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.toast import toast
import requests
import json
from system.base_url import base_url


class Signup(MDScreen):
    pass

    def register(self):
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
            store = requests.post(base_url() + '/register', json=dataJson)
            # data = store.json()

            data = json.loads(store.text)
            self.add_user(data)
            if store.status_code == 200:
                # print(store.text, '\n')
                toast('Berhasil Login')
                self.manager.current = 'botnav'
            else:
                toast('Gagal Login')

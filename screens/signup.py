from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.toast import toast
import requests
import json
from system.base_url import base_url
from kivy.properties import StringProperty


class Signup(MDScreen):
    pass

    role = StringProperty("")

    def checkrole(self, instance, bool, value):
        if bool == True:
            self.role = value
            return self.role
        else:
            return None

    def register(self):
        _nama = self.ids.nama.text
        _email = self.ids.email.text
        _password = self.ids.password.text
        _password_confirm = self.ids.password_confirm.text
        _role = self.role

        if _nama == '' and _email == '' and _password == '' and _role == '':
            toast('Nama, Email, Password dan Role tidak boleh kosong')
        else:
            if _password_confirm == _password:
                dataJson = {
                    'nama': _nama,
                    'email': _email,
                    'password': _password,
                    'role': _role
                }
                # print(dataJson)
                store = requests.post(base_url() + '/register', json=dataJson)
                # data = store.json()

                data = json.loads(store.text)
                if store.status_code == 200:
                    toast('Resgiter Berhasil!')
                    self.clear_text()
                    self.manager.current = 'login'
                else:
                    toast('Register Gagal!')
            else:
                toast('Konfirmasi password salah!')

    def clear_text(self, *args):
        self.ids.nama.text = ""
        self.ids.email.text = ""
        self.ids.password.text = ""
        self.ids.password_confirm.text = ""

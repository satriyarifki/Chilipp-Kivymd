from audioop import add
from email.mime import base
from audioop import add
from email.mime import base
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
import json
from matplotlib.pyplot import cla
import requests
from system.base_url import base_url
from kivymd.toast import toast
from kivy.storage.dictstore import DictStore

# base_url = 'http://localhost:8000/api'


class Login(MDScreen):
    user = None

    def __init__(self, **kw):
        Builder.load_file("kv/login.kv")
        super().__init__(**kw)

    def auth(self):
        # users = requests.post(base_url + '/dataset/probabilitas_kelas')
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

            data = json.loads(store.text)
            self.add_user(data)
            if store.status_code == 200:
                # print(store.text, '\n')
                toast('Berhasil Login')
                self.manager.current = 'botnav'
            else:
                toast('Login Gagal! Cek email dan password!')

    def add_user(self, jsonData):
        jsonString = json.dumps(jsonData)
        jsonFile = open("store/user.json", "w")
        jsonFile.truncate()
        jsonFile.write(jsonString)
        jsonFile.close()
        return jsonFile

    def get_user(self):
        data = self.user

        # jsonDict = {
        #     'id': str(data.get('id')),
        #     'nama': data.get('nama'),
        #     'email': data.get('email'),
        #     'alamat': data.get('alamat'),
        #     'role': data.get('role'),
        #     'stop_loss': str(data.get('stop_loss')),
        #     'harga_awal': str(data.get('harga_awal')),
        # }
        # data = self.user
        return data

    def logout(self):
        data = DictStore(self.user)
        return data.delete()

from ast import If
from audioop import add
from email.mime import base
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
import json
from matplotlib.pyplot import cla
import requests
from system.base_url import base_url

jsonData = ''

class Login(MDScreen):
    
    def __init__(self, **kw):
        Builder.load_file("kv/login.kv")
        super().__init__(**kw)
    
    def auth(self):
        # users = requests.post(base_url + '/dataset/probabilitas_kelas')
        dataJson = {
            'email': self.ids.email.text,
            'password': self.ids.password.text
        }
        sess = requests.Session()
        store = sess.post(base_url() + '/login', json=dataJson)
        
        if store.status_code == 200:
            # print(store['email'])
            print(store.text,'\n')
            self.get_session(store.text)
            self.manager.current = 'botnav'
        else :
            print('gagal login')
    
    def get_session(self, jsonData):
        data = jsonData
        print(data)        
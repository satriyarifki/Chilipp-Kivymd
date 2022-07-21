from kivymd.uix.screen import MDScreen
import json
from kivymd.toast import toast
import requests
from system.base_url import base_url


class Changepass(MDScreen):
    pass

    def show_profile(self):
        f = open('store/user.json')
        data = json.load(f)
        # print(data['nama'])
        self.ids.user_id.text = str(data['id'])

    def update_password(self):
        f = open('store/user.json')
        data = json.load(f)
        # print(data['nama'])
        _new = self.ids.new_password.text
        _confirm = self.ids.password_confirm.text

        if data['id'] == 0:
            toast('Anda belum Login!')
        elif _new == '' and _confirm == '':
            toast('Inputan tidak boleh kosong!')
        else:
            if _confirm == _new:
                dataJson = {
                    'password': _confirm
                }
                # print(dataJson)
                store = requests.post(
                    base_url() + '/user/' + str(data['id']) + '/password', json=dataJson)
                # data = store.json()
                if store.status_code == 200:
                    toast('Update Password Berhasil!')
                else:
                    toast('Update Password Gagal!')
            else:
                toast('Konfirmasi Password Harus sama!')

    def clear_text(self):
        self.ids.new_password.text = ''
        self.ids.password_confirm.text = ''

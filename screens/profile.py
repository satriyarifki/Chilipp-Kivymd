from kivymd.uix.screen import MDScreen
import json
from kivymd.toast import toast
import requests
from system.base_url import base_url
from asyncio.windows_events import NULL


class Profile(MDScreen):
    pass

    def show_profile(self):
        f = open('store/user.json')
        data = json.load(f)
        # print(data['nama'])
        self.ids.email.text = data['email']
        self.ids.nama.text = data['nama']
        self.ids.alamat.text = data['alamat']

    def update_profile(self):
        f = open('store/user.json')
        dt = json.load(f)
        _id = str(dt['id'])

        _nama = self.ids.nama.text
        _email = self.ids.email.text
        _alamat = self.ids.alamat.text

        if _id == '' and _nama == '' and _email == '' and _alamat == '':
            toast('Nama, Email dan Alamat tidak boleh kosong (Tekan Tampilkan Profil)')
        else:
            dataJson = {
                'nama': _nama,
                'alamat': _alamat
            }
            # print(dataJson)
            store = requests.post(
                base_url() + '/user/' + _id + '/profile', json=dataJson)
            # data = store.json()

            if store.status_code == 200:
                self.update_json(dt, _nama, _email, _alamat, )
                new = open('store/user.json')
                data = json.load(new)
                # print(data['nama'])
                self.ids.email.text = data['email']
                self.ids.nama.text = data['nama']
                self.ids.alamat.text = data['alamat']
                new.close()
                f.close()

                toast('Update Profile Berhasil!')
            else:
                toast('Update Profile Gagal!')

    def update_json(self, dt, _nama, _email, _alamat):
        js = {"id": int(dt['id']), "nama": _nama, "email": _email, "email_verified_at": dt['email_verified_at'], "alamat": _alamat,
              "stop_loss": dt['stop_loss'], "harga_awal": dt['harga_awal'], "role": dt['role'], "created_at": dt['created_at'], "updated_at": dt['updated_at']}
        jsonFile = open("store/user.json", "w")
        jsonFile.truncate()
        jsonFile.write(json.dumps(js))
        return dt

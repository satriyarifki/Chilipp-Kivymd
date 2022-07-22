from kivymd.uix.screen import MDScreen
import json
from kivymd.toast import toast
import requests
from system.base_url import base_url


class Stoploss(MDScreen):
    pass

    def update_stoploss(self):

        f = open('store/user.json')
        data = json.load(f)
        # print(data['nama'])
        _stoploss = self.ids.stop_loss.text

        if data['id'] == 0:
            toast('Anda belum Login!')
        elif _stoploss == '':
            toast('Inputan tidak boleh kosong!')
        else:
            dataJson = {
                'stop_loss': _stoploss
            }
            # print(dataJson)
            store = requests.post(
                base_url() + '/stop_loss/' + str(data['id']), json=dataJson)
            df = store.json()
            if store.status_code == 200:
                self.update_json(data, int(df['stop_loss']), df['harga_awal'])
                toast('Update Stop Loss Berhasil!')
            else:
                toast('Update Stop Loss Gagal!')

    def clear_text(self):
        self.ids.stop_loss.text = ''

    def update_json(self, dt, stop_loss, harga_awal):
        js = {"id": int(dt['id']), "nama": dt['nama'], "email": dt['email'], "email_verified_at": dt['email_verified_at'], "alamat": dt['alamat'],
              "stop_loss": stop_loss, "harga_awal": harga_awal, "role": dt['role'], "created_at": dt['created_at'], "updated_at": dt['updated_at']}
        jsonFile = open("store/user.json", "w")
        jsonFile.truncate()
        jsonFile.write(json.dumps(js))
        return jsonFile

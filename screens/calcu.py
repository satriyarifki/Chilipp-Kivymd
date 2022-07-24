from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty
import json
from kivymd.toast import toast
import requests
from system.base_url import base_url
import pandas as pd
import numpy as np
from sklearn.svm import SVR


def covert_data(df):
    data = df.copy()
    data['tanggal'] = data['tanggal'].str.split('-').str[2]
    data['tanggal'] = pd.to_numeric(data['tanggal'])
    # Convert Series to list
    return [data['id'].tolist(), data['tanggal'].tolist(), data['harga'].tolist()]


def predict_prices(dates, prices, x):
    dates = np.reshape(dates, (len(dates), 1))  # convert to 1xn dimension
    x = np.reshape(x, (len(x), 1))
    svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)

    # Fit regression model
    svr_rbf.fit(dates, prices)

    return svr_rbf.predict(x)[0]


def get_all():
    response = requests.get(base_url() + '/dataset').json()

    # print(response)
    list_data = []
    for i in response:
        for item in i:
            list_data.append(
                {'id': item['id'], 'tanggal': item['tanggal'], 'harga': item['harga']})

    return list_data


data = get_all()
df = pd.DataFrame.from_dict(data)
ids, dates, prices = covert_data(df)


class Calcu(MDScreen):
    check = StringProperty("")
    pass

    def tujuan(self, instance, bool, value):
        if bool == True:
            self.check = value
            return self.check
        else:
            return None

    def get_harga(self):
        predict_price = predict_prices(ids, prices, [len(data)])
        return predict_price

    def calc(self):
        tujuan = self.check
        estimasi = 0

        _hargapasar = self.get_harga()
        berat = self.ids.berat.text
        selisih = self.ids.selisih.text

        f = open('store/user.json')
        data = json.load(f)
        f.close()

        if data['role'] != 'pengepul':
            toast('Fitur kalkulator hanya untuk Pengepul!')
        else:

            if berat != '' and selisih != '' and tujuan != '':
                if tujuan == 'Jakarta':
                    estimasi = 1200
                elif tujuan == 'Jawa Barat':
                    estimasi = 1030
                elif tujuan == 'Jawa Tengah':
                    estimasi = 950
                elif tujuan == 'Jawa Timur':
                    estimasi = 800
                else:
                    estimasi = 0

                ton = int(berat)/1000
                total = int(berat) * int(estimasi)
                berat = int(berat)
                estimasi = int(estimasi)
                _hargabeli = int(_hargapasar) - int(selisih)
                _keuntungan = (int(selisih) * berat) - total

                self.ids.lblestimasi.text = f'Estimasi          : Rp. {estimasi:,} /kg'
                self.ids.lblberat.text = f'Berat                 : {berat:,} kg / {ton} ton'
                self.ids.lbltujuan.text = f'Tujuan              : {tujuan}'
                self.ids.lbltotalbiaya.text = f'Total Biaya      : Rp. {total:,}'
                self.ids.lblhargapasar.text = f'Harga Pasar    : Rp. {int(_hargapasar):,}'
                self.ids.lblhargabeli.text = f'Prediksi Harga Beli  : Mulai Dari Rp. {_hargabeli:,}'
                self.ids.lblkeuntungan.text = f'Total Keuntungan    : Rp. {_keuntungan:,} Dengan Selisih Rp. {int(selisih):,}'
            else:
                toast('Inputan tidak boleh kosong!')

from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.behaviors import CircularElevationBehavior
from kivymd.uix.card import MDCard
from kivy.uix.image import Image
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
import numpy as np
from system.base_url import base_url
from kivymd.toast import toast
import pandas as pd
import requests
import json
from sklearn.svm import SVR


class ShadowCard(MDCard, RoundedRectangularElevationBehavior):
    pass


class ShadowImage(Image, CircularElevationBehavior):
    pass


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

x = ids
y = prices


fig, ax = plt.subplots()
ax.plot(x, y)

plt.ylabel("Harga")
plt.xlabel("Bulan")
plt.legend()


class Cabaidet(MDScreen):
    def __init__(self, **kw):
        Builder.load_file("kv/cabaidet.kv")
        super().__init__(**kw)

        graf = self.ids.graf
        graf.add_widget(FigureCanvasKivyAgg(plt.gcf()))

    def get_data(self):
        # sampel = self.sampel_data()
        x_berita = self.get_berita()
        # print(sampel['id'], x_berita)
        # self.ubah_berita(sampel['id'], x_berita)

        return x_berita

    def sampel_data(self):
        store = requests.get(base_url() + '/dataset/sampel_data').json()

        list_data = {
            'id': store['id'],
            'tanggal': store['tanggal'],
            'permintaan': store['permintaan'],
            'ketersediaan': store['ketersediaan'],
            'harga': store['harga'],
            'berita': store['berita']
        }

        return list_data

    def get_harga(self):
        predict_price = predict_prices(ids, prices, [len(data)])
        return str(round(predict_price, 3))

    def get_berita(self):
        # prob kelas
        prob = self.probabilitas_kelas()

        # permintaan
        permintaan_naik = self.sort_permintaan('naik')
        permintaan_tetap = self.sort_permintaan('tetap')
        permintaan_turun = self.sort_permintaan('turun')

        # ketersediaan
        ketersediaan_naik = self.sort_ketersediaan('naik')
        ketersediaan_tetap = self.sort_ketersediaan('tetap')
        ketersediaan_turun = self.sort_ketersediaan('turun')

        # Harga
        harga_naik = self.sort_harga('naik')
        harga_tetap = self.sort_harga('tetap')
        harga_turun = self.sort_harga('turun')

        # sample data
        sampel = self.sampel_data()
        x_permintaan = sampel['permintaan']
        x_ketersediaan = sampel['ketersediaan']
        x_harga = sampel['harga']
        x_berita = ''

        # prob permintaan [x = naik, y = tetap, z = turun]
        x_prob_permintaan = 1/np.sqrt(2*3.14*permintaan_naik['stdev']) * np.exp(-(
            pow(x_permintaan-permintaan_naik['mean'], 2))/(pow(permintaan_naik['stdev'], 2)))
        y_prob_permintaan = 1/np.sqrt(2*3.14*permintaan_tetap['stdev']) * np.exp(-(pow(
            x_permintaan-permintaan_tetap['mean'], 2))/(pow(permintaan_tetap['stdev'], 2)))
        z_prob_permintaan = 1/np.sqrt(2*3.14*permintaan_turun['stdev']) * np.exp(-(pow(
            x_permintaan-permintaan_turun['mean'], 2))/(pow(permintaan_turun['stdev'], 2)))

        # print('PROBABILITAS PERMINTAAN')
        # print(x_prob_permintaan)
        # print(y_prob_permintaan)
        # print(z_prob_permintaan)

        # prob ketersediaan [x = naik, y = tetap, z = turun]
        x_prob_ketersediaan = 1/np.sqrt(2*3.14*ketersediaan_naik['stdev']) * np.exp(-(pow(
            x_ketersediaan-ketersediaan_naik['mean'], 2))/(pow(ketersediaan_naik['stdev'], 2)))
        y_prob_ketersediaan = 1/np.sqrt(2*3.14*ketersediaan_tetap['stdev']) * np.exp(-(pow(
            x_ketersediaan-ketersediaan_tetap['mean'], 2))/(pow(ketersediaan_tetap['stdev'], 2)))
        z_prob_ketersediaan = 1/np.sqrt(2*3.14*ketersediaan_turun['stdev']) * np.exp(-(pow(
            x_ketersediaan-ketersediaan_turun['mean'], 2))/(pow(ketersediaan_turun['stdev'], 2)))

        # print('\nPROBABILITAS KETERSEDIAAN')
        # print(x_prob_ketersediaan)
        # print(y_prob_ketersediaan)
        # print(z_prob_ketersediaan)

        # prob harga [x = naik, y = tetap, z = turun]
        x_prob_harga = 1/np.sqrt(2*3.14*harga_naik['stdev']) * np.exp(-(
            pow(x_harga-harga_naik['mean'], 2))/(pow(harga_naik['stdev'], 2)))
        y_prob_harga = 1/np.sqrt(2*3.14*harga_tetap['stdev']) * np.exp(-(
            pow(x_harga-harga_tetap['mean'], 2))/(pow(harga_tetap['stdev'], 2)))
        z_prob_harga = 1/np.sqrt(2*3.14*harga_turun['stdev']) * np.exp(-(
            pow(x_harga-harga_turun['mean'], 2))/(pow(harga_turun['stdev'], 2)))

        # print('\nPROBABILITAS HARAG')
        # print(x_prob_harga)
        # print(y_prob_harga)
        # print(z_prob_harga)

        # hasil klasifikasi [x = naik, y = tetap, z = turun]
        x_klasifikasi = x_prob_permintaan * \
            x_prob_ketersediaan*x_prob_harga*prob['naik']
        y_klasifikasi = y_prob_permintaan * \
            y_prob_ketersediaan*y_prob_harga*prob['tetap']
        z_klasifikasi = z_prob_permintaan * \
            z_prob_ketersediaan*z_prob_harga*prob['turun']

        # print('\nHASIL KLASIFIKASI')
        # print('{0:.12f}'.format(x_klasifikasi))
        # print('{0:.12f}'.format(y_klasifikasi))
        # print('{0:.12f}'.format(z_klasifikasi))

        hasil_klasifikasi = 0

        if x_klasifikasi > y_klasifikasi and x_klasifikasi > z_klasifikasi:
            x_berita = 'naik'
            # hasil_klasifikasi = x_klasifikasi
        if y_klasifikasi > x_klasifikasi and y_klasifikasi > z_klasifikasi:
            x_berita = 'tetap'
            # hasil_klasifikasi = y_klasifikasi
        if z_klasifikasi > x_klasifikasi and z_klasifikasi > y_klasifikasi:
            x_berita = 'turun'
            # hasil_klasifikasi = z_klasifikasi

        # print('\nMAKA HASILNYA')
        # print('BERITA : ' + x_berita)
        # print('ANGKA  : ' + '{0:.12f}'.format(hasil_klasifikasi))
        # print('\nSAMPLE DATA')
        # print('Permintaan (KG)   : ', x_permintaan,
        #       ' atau ', (x_permintaan/1000), ' ton')
        # print('Ketersediaan (KG) : ', x_ketersediaan,
        #       ' atau ', (x_ketersediaan/1000), ' ton')
        dataJson = {
            'berita': x_berita
        }

        store = requests.post(
            base_url() + '/dataset/' + str(sampel['id']) + '/berita', json=dataJson)

        # print(store.status_code)

        return x_berita

    def probabilitas_kelas(self):
        store = requests.get(base_url() + '/dataset/probabilitas_kelas').json()

        list_data = {
            'naik': store['naik'],
            'tetap': store['tetap'],
            'turun': store['turun']
        }

        return list_data

    def sort_permintaan(self, params):
        store = requests.get(
            base_url() + '/dataset/sort_permintaan/' + params).json()

        list_data = {
            'total': store['total'],
            'count': store['count'],
            'total_pangkat_2': store['total_pangkat_2'],
            'count_pangkat_2': store['count_pangkat_2'],
            'mean': store['mean'],
            'stdev': store['stdev'],
            'berita': store['berita'],
        }

        return list_data

    def sort_ketersediaan(self, params):
        store = requests.get(
            base_url() + '/dataset/sort_ketersediaan/' + params).json()

        list_data = {
            'total': store['total'],
            'count': store['count'],
            'total_pangkat_2': store['total_pangkat_2'],
            'count_pangkat_2': store['count_pangkat_2'],
            'mean': store['mean'],
            'stdev': store['stdev'],
            'berita': store['berita'],
        }

        return list_data

    def sort_harga(self, params):
        store = requests.get(
            base_url() + '/dataset/sort_harga/' + params).json()

        list_data = {
            'total': store['total'],
            'count': store['count'],
            'total_pangkat_2': store['total_pangkat_2'],
            'count_pangkat_2': store['count_pangkat_2'],
            'mean': store['mean'],
            'stdev': store['stdev'],
            'berita': store['berita'],
        }

        return list_data

    def stop_loss(self):
        predict_price = predict_prices(ids, prices, [len(data)])
        f = open('store/user.json')
        r = json.load(f)
        stop = (r['stop_loss'] / 100) * r['harga_awal']
        price = predict_price - stop
        # print(data['nama'])
        return str(round(price, 3))

    def refresh(self):
        predict_price = predict_prices(ids, prices, [len(data)])
        f = open('store/user.json')
        r = json.load(f)
        stop = (r['stop_loss'] / 100) * r['harga_awal']
        price = predict_price - stop
        # print(data['nama'])
        self.ids.stop_loss.text = "Rp. " + str(round(price, 3))

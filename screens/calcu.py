from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty


class Calcu(MDScreen):
    check = StringProperty("")
    pass

    def tujuan(self, instance, bool, value):
        if bool == True:
            self.check = value
            return self.check
        else:
            return None

    def calc(self):
        tujuan = self.check
        estimasi = 0
        berat = self.ids.berat.text
        if tujuan == 'Jakarta':
            estimasi = 1300
        elif tujuan == 'Jawa Barat':
            estimasi = 1230
        elif tujuan == 'Jawa Tengah':
            estimasi = 1120
        elif tujuan == 'Jawa Timur':
            estimasi = 1010
        else:
            estimasi = 0

        ton = int(berat)/1000
        total = int(berat) * int(estimasi)
        berat = int(berat)
        estimasi = int(estimasi)
        self.ids.lblestimasi.text = f'Estimasi : Rp. {estimasi:,} /kg'
        self.ids.lblberat.text = f'Berat       : {berat:,} kg / {ton} ton'
        self.ids.lbltujuan.text = f'Tujuan    : {tujuan}'
        self.ids.tftotal.text = f'Rp. {total:,}'

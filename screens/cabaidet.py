from ast import Import
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.behaviors import CircularElevationBehavior
from kivymd.uix.card import MDCard
from kivy.uix.image import Image
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
import numpy as np

class ShadowCard(MDCard, RoundedRectangularElevationBehavior):
    pass

class ShadowImage(Image, CircularElevationBehavior):
    pass

x = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
y = [2000, 2312, 5490, 4350, 3212]


fig, ax = plt.subplots()
ax.bar (x,y, width=1, edgecolor="white")

plt.ylabel("Harga")
plt.xlabel("Bulan")

class Cabaidet(MDScreen):
    def __init__(self, **kw): 
        Builder.load_file("kv/cabaidet.kv")
        super().__init__(**kw)
        
        graf = self.ids.graf
        graf.add_widget(FigureCanvasKivyAgg(plt.gcf()))
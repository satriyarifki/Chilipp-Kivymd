from kivymd.tools.hotreload.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.core.text import LabelBase
import requests
from screens.screens import *
from system.base_url import base_url

class WindowManager(ScreenManager):
    pass

class Chilipp(MDApp):
    CLASSES = {
        'Splash' : 'screens.splash',
        'Login' : 'screens.login',
        'Signup' : 'screens.signup',
        'Botnav' : 'screens.botnav',
        'Home'  : 'screens.home',
        'Calcu' : 'screens.calcu',
        'Cabaidet' : 'screens.cabaidet',
        'Setting' : 'screens.setting',
        'Stoploss' : 'screens.stoploss',
    }
    AUTORELOADER_PATHS = [
        (".", {'recursive': True})
    ]
    KV_FILES = [
        'kv/splash.kv',
        'kv/login.kv',
        'kv/botnav.kv',
        'kv/home.kv',
        'kv/calcu.kv',
        'kv/cabaidet.kv',
        'kv/setting.kv',
        'kv/signup.kv',
        'kv/stoploss.kv',
    ]
    def build_app(self): 
        self.wm = WindowManager()
        screens = [
            # Splash(name='splash'),
            Login(name='login'),
            # Signup(name='signup'),
            Botnav(name='botnav'),
            Home(name='home'),
            Cabaidet(name='cabaidet'),
            Calcu(name='calcu'),
            Setting(name='setting'),
            Stoploss(name='stoploss'),
            
            
        ]
        for screen in screens:
            self.wm.add_widget(screen)
        return self.wm
    
    
    def get_nama(self):
        apadah = requests.Session()
        return apadah
            
if __name__ == '__main__':
    Chilipp().run()
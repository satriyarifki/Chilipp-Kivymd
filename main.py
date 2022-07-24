from kivymd.tools.hotreload.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.core.text import LabelBase
import requests
from screens.screens import *
from screens.login import Login
from kivy.storage.dictstore import DictStore


class WindowManager(ScreenManager):
    pass


class Chilipp(MDApp):
    CLASSES = {
        'Splash': 'screens.splash',
        'Login': 'screens.login',
        'Signup': 'screens.signup',
        'Botnav': 'screens.botnav',
        'Home': 'screens.home',
        'Calcu': 'screens.calcu',
        'Cabaidet': 'screens.cabaidet',
        'Setting': 'screens.setting',
        'Stoploss': 'screens.stoploss',
        'Profile': 'screens.profile',
        'Splash': 'screens.splash',
        'Login': 'screens.login',
        'Signup': 'screens.signup',
        'Botnav': 'screens.botnav',
        'Home': 'screens.home',
        'Calcu': 'screens.calcu',
        'Cabaidet': 'screens.cabaidet',
        'Setting': 'screens.setting',
        'Stoploss': 'screens.stoploss',
        'Changepass': 'screens.changepass',
        'Profile': 'screens.profile',
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
        'kv/changepass.kv',
        'kv/profile.kv',
    ]

    def build_app(self):
        self.wm = WindowManager()
        screens = [
            Splash(name='splash'),
            Login(name='login'),
            # Signup(name='signup'),
            # Botnav(name='botnav'),
            # Home(name='home'),
            # Cabaidet(name='cabaidet'),
            # Calcu(name='calcu'),
            # Setting(name='setting'),
            # Profile(name='profile'),
            # Setting(name='setting'),
            # Stoploss(name='stoploss'),
        ]
        for screen in screens:
            self.wm.add_widget(screen)

        self.wm.add_widget(Botnav(name='botnav'))
        self.wm.add_widget(Home(name='home'))
        self.wm.add_widget(Cabaidet(name='cabaidet'))
        self.wm.add_widget(Calcu(name='calcu'))
        self.wm.add_widget(Setting(name='setting'))
        self.wm.add_widget(Stoploss(name='stoploss'))
        self.wm.add_widget(Changepass(name='changepass'))
        self.wm.add_widget(Profile(name='profile'))
        return self.wm


if __name__ == '__main__':
    Chilipp().run()

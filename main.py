from kivymd.tools.hotreload.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.core.text import LabelBase
from screens.cabaidet import Cabaidet

from screens.screens import *

class WindowManager(ScreenManager):
    pass

class Chilipp(MDApp):
    CLASSES = {
        'Splash' : 'screens.splash',
        'Login' : 'screens.login',
        'Botnav' : 'screens.botnav',
        'Home'  : 'screens.home',
        'Calcu' : 'screens.calcu',
        'Cabaidet' : 'screens.cabaidet',
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
        'kv/cabaidet.kv'
    ]
    def build_app(self): 
        self.wm = WindowManager()
        screens = [
            # Splash(name='splash'),
            # Login(name='login'),
            # Botnav(name='botnav'),
            Home(name='home'),
            Cabaidet(name='cabaidet'),
            Calcu(name='calcu'),
            
        ]
        for screen in screens:
            self.wm.add_widget(screen)
        return self.wm
    
    def _rebuild(self, *args):
        if args[1] == 32:
            self.rebuild()
            
if __name__ == '__main__':
    Chilipp().run()
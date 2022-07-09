from kivymd.tools.hotreload.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.core.text import LabelBase

from screens.screens import *

class WindowManager(ScreenManager):
    pass

class Chilipp(MDApp):
    CLASSES = {
        'Splash' : 'screens.splash',
        'Login' : 'screens.login',
    }
    AUTORELOADER_PATHS = [
        ('.', {'recursive': True})
    ]
    KV_FILES = [
        'kv/splash.kv',
        'kv/login.kv'
    ]
    def build_app(self): 
        self.wm = WindowManager()
        screens = [
            Splash(name='splash'),
            Login(name='login'),
        ]
        for screen in screens:
            self.wm.add_widget(screen)
        return self.wm
    
if __name__ == '__main__':
    Chilipp().run()
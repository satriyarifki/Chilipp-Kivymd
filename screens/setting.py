from asyncio.windows_events import NULL
from kivymd.uix.screen import MDScreen
import json
from screens.login import Login
from screens.profile import Profile


class Setting(MDScreen):
    pass

    def logout(self):
        data = {"id": 0, "nama": "", "email": "", "email_verified_at": NULL, "alamat": "",
                "stop_loss": NULL, "harga_awal": NULL, "role": "", "created_at": NULL, "updated_at": NULL}
        jsonFile = open("store/user.json", "w")
        jsonFile.truncate()
        jsonFile.write(json.dumps(data))
        jsonFile.close()
        self.parent.parent.parent.parent.manager.current = 'login'
        return jsonFile

from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
# from kvdroid.tools import speech
# from kvdroid.tools.audio import Player
import os
from kivymd.uix.list import OneLineListItem, OneLineAvatarIconListItem, IconLeftWidget, ImageLeftWidget
# from kvdroid.tools import toast
from kivy.uix.screenmanager import Screen
# from kvdroid.tools.contact import get_contact_details
from kivy.utils import platform
import tkinter as tk
# from android.config import ACTIVITY_CLASS_NAME, ACTIVITY_CLASS_NAMESPACE
# from android.permissions import request_permissions, Permission



Code = """
#ScreenManager:
#	Screen1:

#<Screen1>:
MDBoxLayout:
	orientation: "vertical"

	MDToolbar:
		title: "Tinsel Player"
		specific_text_color: (1, 1, 0, 1)
		md_bg_color: (.2 , .5, .2, 1)
		right_action_items: [["dots-vertical"]]

	RecycleView:
		id: rv
		viewclass: "CustomIconItem"
	
		RecycleBoxLayout:
			orientation: "vertical"
			size_hint_y: None
			height: self.minimum_height


"""


class Screen1(Screen):
    pass


class CustomIconItem(OneLineAvatarIconListItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #vine = IconLeftWidget(icon="home")
        vine = ImageLeftWidget(source = self.text)
        self.add_widget(vine)


class Bold(MDApp, App):

    def build(self):
        max_iteration = 0
        builder = Builder.load_string(Code)
        return builder

    def on_start(self):
        Music = []

        path = "/storage/emulated/0/DCIM/Facebook/"
        for filename in os.listdir(path):
            current_path = os.path.join(path, filename)

            if os.path.isdir(current_path):
                rec_audio_dirs = current_path
            # audio_dirs.append(rec_audio_dirs)

            elif filename.endswith(".jpg") or filename.endswith(".png"):
                if filename in Music:
                    pass
                else:
                    Music.append(current_path)

        Music_List = len(Music)

        data = [{"text": str(Music[i]), 
        "size_hint_x": 1, "source": str(Music[i])
         
         } for i in range(len(Music))]

        self.root.ids.rv.data = data


Bold().run()

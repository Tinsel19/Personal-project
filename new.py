from kivymd.app import MDApp
from kivy.lang import Builder

Code = """
MDBoxLayout:
	orientation: "vertical"
	
	Camera:
		play: True
	
	Button:
		text: "snap"


"""


class CameraApp(MDApp):
	def build(self):
		builder = Builder.load_string(Code)
		return builder

CameraApp().run()
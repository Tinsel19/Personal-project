from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.metrics import dp
from kivy.uix.widget import Widget
from kivy.properties import Clock
from kivy.uix.image import Image
print(Window.width)

Code = """
MDBoxLayout:
	orientation: "vertical"
	md_bg_color: (1, 0, 0, 1)
	
	id: x
	MDCard:
		orientation: "vertical"
		Image:
			
			source: "FB_IMG_1653801923092.jpg"
		Image:
			source: "FB_IMG_1653801923092.jpg"
		Image:
			source: "FB_IMG_1653801923092.jpg"
	
	


"""
class MyC(Button, Image):
	pass


class Shooter(MDApp, App):

	
	def build(self):
		builder = Builder.load_string(Code)
		
		return builder
		
	
	def on_start(self):
		pass
	

Shooter().run()
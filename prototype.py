from kivymd.app import MDApp
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineListItem

Code = """
ScreenManager:
	Screen:
		BoxLayout:
			orientation: "vertical"
			
			Button:
				text: "Hi"
				on_press: app.hike()
			
			MDList:
				id: jug
					


"""



class Screen1(Screen):
	pass

class Screen2(Screen):
	pass

class Prototype(MDApp, App):
	def build(self):
		builder = Builder.load_string(Code)
		return  builder
	
	def hike(self):
		kite = OneLineListItem()
		self.root.ids.jug.add_widget(kite)


Prototype().run()
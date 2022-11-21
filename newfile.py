from kivy.app import App
from kivymd.app import MDApp
from  kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager


code = """
ScreenManager:
	id: name
	
	IntroScreen:
		name: "intro"
		BoxLayout:
			orientation: "vertical"
			spacing: dp(10)
			#padding: dp(10)
			canvas:
				Color:
					rgba: (0, 0, .7, .08)
				
				Rectangle:
					size: self.size
					pos: self.pos
					
			Label:
			
			Label:
				text: "Discover the Weather in \\nYour City"
				halign: "center"
				bold: True
				font_size: dp(30)
				size_hint_y: .3
				height: dp(30)
				
			Label:
				text: "Get to know your weather maps and radar \\nprecipitation forecast"
				halign: "center"
				bold: True
				size_hint_y: .2
				height: dp(20)
				color: (1, 1, 1, .6)
				font_size: dp(15)
				
			MDFillRoundFlatButton:
				size_hint: .8, .1
				pos_hint: {"center_x": .5}
				text: "Get started"
				bold: True
				rounded_button: True
				md_bg_color: (0,  .5,  1, 1)
				on_release: name.current = "main"
					
				
			Label:
				size_hint_y: .2
				height: dp(10)
			
			
	
	MainScreen:
		name: "main"
		BoxLayout:
			orientation: "vertical"
			spacing: dp(5)
			padding: dp(10)
			canvas:
				Color:
					rgba: (0, 0, .7, .08)
				Rectangle:
					size: self.size
					pos: self.pos
			
			GridLayout:
				size_hint_y: .2
				rows: 1
				MDIconButton:
					icon: "menu"
					md_bg_color: (1, 1, 1, .1)
					
				Label:
					
				MDIconButton:
					icon: "satellite"
					
				Label:
					text: "Isekai World"
					#bold: True
					#font_size: dp(15)
					
				MDIconButton:
					icon: "chevron-down"
					
				MDBoxLayout:
					size_hint: None, 1
					width: dp(100)
					md_bg_color: (1, 1, 1, .1)
					radius: dp(30)
					
					MDIconButton:
						icon: "white-balance-sunny"
						
					MDIconButton:
						icon: "moon-waning-crescent"
						theme_text_color: "Custom"
						text_color: (0, .4, 1, 1)
						md_bg_color: (1, 1, 1, 1)
				
			MDLabel:
				text: "Today's Report"
				bold: True
				font_size: dp(25)
				halign: "left"
			
			Label:
				
			BoxLayout:
				orientation: "vertical"
				size_hint: .5, 1
				pos_hint: {"center_x": .5}
				
				Label:
					text: "It's Cloudy"
					font_size: dp(20)
					#bold: True
				
				Label:
					text: "29"
					font_size: dp(50)
					bold: True
					
					canvas:
						Color:
							rgba: (0, .4, 1, 1)
							
						Ellipse:
							size: (20, 20)
							#radius: 
							pos: self.x*2.3, self.y*1.15
					
				
			GridLayout:
				cols: 3
				rows: 3
				size_hint: .8, 1
				pos_hint: {"center_x": .5}
				
				Label:
					#background_color: (1,0, 0, 1)
					id: b
					canvas:
						Color:
							rgba: (1, 1, 1, .1)
						Ellipse:
							size : (80, 80)
							pos: b.width/2 +40, self.y
							
				Label:
					id : a
					#background_color: (0,1, 0, 1)
					canvas:
						Color:
							rgba:(1, 1, 1, .1)
						Ellipse:
							size : (80, 80)
							pos: (b.width*3)/2 +40, self.y
							
				Label:
					#background_color: (0, 0, 1, 1)
					id: c
					canvas.after:
						Color:
							rgba: (1, 1, 1, .1)
						Ellipse:
							size : (80, 80)
							pos: (b.width*5)/2 +40, self.y
				
				Label:
					text: "23km/h"
					bold: True
					font_size: dp(20)
				
				Label:
					text: "30%"
					bold: True
					font_size: dp(20)
				
				Label:
					text: "23km/h"
					bold: True
					font_size: dp(20)
				
				Label:
					text: "Sunny"
				
				Label:
					text: "Humidity"
				
				Label:
					text: "Chance of rain"
			
			Label:
				size_hint_y: .3
				height: dp(30)
			
			MDGridLayout:
				cols: 4
				rows: 1
				size_hint: .8, None
				height: dp(60)
				spacing: dp(30)
				pos_hint:  {"center_x":.5}
				md_bg_color: (1, 1, 1, .1)
				radius: dp(10)
				
				MDIconButton:
					icon: "home"
					font_size: dp(40)
					icon_size: (50, 50)
					theme_text_color: "Custom"
					text_color: (0, 0, 1, 1)
				
				MDIconButton:
					icon: "magnify"
					theme_text_color: "Custom"
					text_color: (1, 1, 1, .1)
				
				MDIconButton:
					icon: "compass"
					theme_text_color: "Custom"
					text_color: (1, 1, 1, .1)
				
				MDIconButton:
					icon: "account"
					theme_text_color: "Custom"
					text_color: (1, 1, 1, .1)
			
			Label:
				size_hint_y: None
				height: dp(100)
				
					
				
									
			
		
"""
class IntroScreen(Screen):
	pass

class MainScreen(Screen):
	pass
class Test(MDApp, App):
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.theme_cls.theme_style = "Dark"
		
		
	def build(self):
		builder = Builder.load_string(code)
		return builder
		
		
Test().run()
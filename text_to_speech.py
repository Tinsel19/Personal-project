from  kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder 
from kvdroid.tools import speech 
from kvdroid.tools.audio import Player
import os
from kvdroid.tools import toast
from kvdroid.tools.contact import get_contact_details
from kivy.utils import platform
from android.config import ACTIVITY_CLASS_NAME, ACTIVITY_CLASS_NAMESPACE
from android.permissions import request_permissions, Permission



Code = """
#: import webbrowser webbrowser


MDBoxLayout:
	orientation: "vertical"
	md_bg_color: (1, .5, 0, 1)
	spacing: dp(10)
	
	MDLabel:
		text: "Text to Speech Conveter" 
		theme_text_color: "Custom"
		text_color: (1, 1, 1, 1)
		halign: "center"
		background_color: (1, 0, 1, 1)
		size_hint: 1, .2
	
	TextInput:
		id: textinput
		hint_text: "Enter text to be converted "
		background_normal: ""
		size_hint: .8, .2
		pos_hint: {"center_x": .5}
		padding: dp(5), dp(10)
		halign: "center"
		
		canvas.before:
			Color:
				rgba: (0, 0, 0, 1)
			
			Line:
				width: 1
				rectangle: (*self.pos , *self.size)
	
	MDGridLayout:
		rows: 1
		cols: 2
		size_hint: .4 ,1
		pos_hint: {"center_x": .5}
		
		
		MDFlatButton:
			text: "Text to speech"
			theme_text_color: "Custom"
			text_color: ( 1, 1, 1,  1)
			
			on_press: app.show()
			
		
		MDFlatButton:
			text: "Clear input"
			theme_text_color: "Custom"
			text_color: ( 1, 1, 1, 1)
			
			on_press: app.clear_input()

	MDGridLayout:
		rows: 3
		cols: 1
		
		MDLabel:
			text: "Music Player" 
			theme_text_color: "Custom"
			text_color: (1, 1, 1, 1)
			halign: "center"
			background_color: (1, 0, 1, 1)
			size_hint: 1, .2

		MDLabel:
			id: name
			theme_text_color: "Custom"
			text_color: (1, 1, 1, 1)
			halign: "center"
			background_color: (1, 0, 1, 1)
			size_hint: 1, .2
		
		
		MDGridLayout:
			rows: 1
			cols: 5
			size_hint: .9, 1
			padding: dp(20)
			spacing: dp(30)
			pos_hint: {"center_x":.5}
			md_bg_color: (1, .5, 0, 1)
			radius: dp(40)
			
			
			MDIconButton:
				icon: "arrow-left"
				theme_text_color: "Custom"
				text_color: ( 1, 1, 1, 1)
				on_press: app.Previous()
			
			
			MDIconButton:
				icon: "pause"
				theme_text_color: "Custom"
				text_color: ( 1, 1, 1, 1)
				on_press: app.pause()
			
			MDFloatingActionButton:
				icon: "play"
				theme_text_color: "Custom"
				text_color: ( 1, 1, 1, 1)
				on_press: app.Play()
			
			MDIconButton:
				icon: "reload"
				theme_text_color: "Custom"
				text_color: ( 1, 1, 1, 1)
				on_press: app.Resume()
			
			
			
			MDIconButton:
				icon: "arrow-right"
				theme_text_color: "Custom"
				text_color: ( 1, 1, 1, 1)
				on_press: app.Next()
	
	GridLayout:
		rows: 2
		cols: 1
		size_hint: .5, 1
		spacing: dp(10)
		pos_hint: {"center_x":.5}
		padding: dp(20)
					
		MDLabel:
			text: str(app.x)
			theme_text_color: "Custom"
			text_color: (1, 1, 1, 1)
			halign: "center"
			background_color: (1, 0, 1, 1)
			size_hint: 1, .2
					
		MDFlatButton:
			text: "Open Youtube"
			theme_text_color: "Custom"
			text_color: ( 1, 1, 1,  1)
			size_hint: .4, .07
			on_release: webbrowser.open("https://youtube.com/")
			on_press: app.Contacts()
					
	
	
"""




class TextSpeech( MDApp, App):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		#self.directory = []
		self.x = 0
		self.List = []
		path = "//storage//emulated//0"
		for filename in os.listdir(path):
			if filename.endswith(".mp3") or filename.endswith(".m4a"):
				self.List.append(os.path.join(path, filename))
		#self.directory = self.List.copy()
		
		self.music_name = self.List[0]
		
		

	
	def build(self):

		builder = Builder.load_string(Code)
		return builder 
	
	def clear_input(self):
		self.root.ids.textinput.text = ""
		
	def show(self):
		speech(self.root.ids.textinput.text, "en")
		toast("Tinsel19")
	
	def Play(self):
		
		self.player = Player()
		self.root.ids.name.text = self.music_name
		self.player.play(self.List[0])
		self.player.do_loop(True)
		
		
	def pause(self):
		self.player.pause()
	
	def Resume(self):
		self.player.resume();
	
	def Next(self):
		#self.music_name = self.music_list[self.x]
		self.x += 1
		
		if self.x >= 0 and self.x <= (len(self.List) -1):
			
			self.music_name = self.List[self.x]
			self.root.ids.name.text = self.music_name
			
			self.player = Player()
			self.player.play(self.music_name)
			self.player.do_loop(True)
		
	
	def Previous(self):
		
		self.x  -= 1
		if self.x >= 0:
		
			self.music_name = self.List[self.x]
			self.root.ids.name.text = self.music_name
		
			self.player = Player()
			self.player.play(self.music_name)
			self.player.do_loop(True)
		
			
	
	def Contacts(self):
		#get_contact_details("phone_book")
		pass
	

TextSpeech().run()
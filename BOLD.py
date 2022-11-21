from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder 
from kvdroid.tools import speech 
from kvdroid.tools.audio import Player
import os
import datetime
from kivymd.uix.list import OneLineIconListItem, OneLineAvatarIconListItem, ImageLeftWidget, IconRightWidget
from kvdroid.tools import toast
from kivy.uix.screenmanager import Screen
from kvdroid.tools.contact import get_contact_details
from kivy.utils import platform
from android.config import ACTIVITY_CLASS_NAME, ACTIVITY_CLASS_NAMESPACE
from android.permissions import request_permissions, Permission
from kivy.uix.gridlayout import GridLayout

import vlc
import webbrowser
import pygame

pygame.mixer.init()


Code= '''
MDNavigationLayout:
	ScreenManager:
		MainScreen:
			BoxLayout:
				orientation: "vertical"
				spacing: dp(5)
				MDToolbar:
					title: "Tinsel Player"
					md_bg_color: (1, .5, 0, 1)
					specific_text_color: (1, 1, 1, 1)
					left_action_items: [["menu"]]
					right_action_items: [["magnify"]]
				
				
					
				RV:
					id: rv
				
				
				MDGridLayout:
					cols: 1
					rows: 2
					size_hint_y: None
					height: dp(80)
					id: grid
					md_bg_color: (1, .5, 0, 1)
						
					OneLineIconListItem:
						id: mist
						theme_text_color: "Custom"
						text_color: (1, 1, 1, 1)
						
					GridLayout:
						
						rows: 1
						cols: 3
						spacing: dp(self.width/6)
										
						MDIconButton:
							icon: "skip-previous"
							theme_text_color: "Custom"
							text_color: (1, 1, 1, 1)
							on_press: app.Previous()
							id: m_back
												
						MDIconButton:
							icon: "play"
							theme_text_color: "Custom"
							text_color: (1, 1, 1, 1)
							on_press: app.Play()
							id: m_play
											
						MDIconButton:
							icon: "skip-next"
							theme_text_color: "Custom"
							text_color: (1, 1, 1, 1)
							on_press: app.Next()
							id: m_next
							
					
					
						
			
						
		
			
		
		
<RV@RecycleView>
	
	viewclass:'CustomIconItem'
	RecycleBoxLayout:
		orientation: "vertical"
		size_hint_y:None
		height:self.minimum_height
		
'''
class CustomIconItem(OneLineAvatarIconListItem):
	pass
class MainScreen(Screen):
	pass

class DownLayout(GridLayout):
	pass


class app(MDApp):
    def __init__(self, **kwargs):
    	super().__init__(**kwargs)
    	self.x = 0
    
    def build(self):
        return Builder.load_string(Code)
           
    def on_start(self):
    	#I_R_W = IconRightWidget("play")
    	#self.root.ids.OneId.add_widget(I_R_W)
   
    	self.Music = []
    	self.Music1 = []
    	
    	directory = []
    	path = "//storage//emulated//0"
    	for filename in os.listdir(path):
    		if filename.endswith(".mp3") or filename.endswith(".m4a"):
    			self.Music.append(os.path.join(path, filename))
    			self.Music1.append(filename)
    
    	directory = []
    	path = "//storage//emulated//0"
    	for filename in os.listdir(path):
    		if filename.endswith(".mp3") or filename.endswith("m4a") or filename.endswith(".mp4") or filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".smi") or filename.endswith(".docx") or filename.endswith(".pdf") or filename.endswith(".zip") or "." in filename:
    			pass
    		else:
    			directory.append(os.path.join(path, filename))
    	
    	directory = []
    	path = "//storage//emulated//0"
    	for filename in os.listdir(path):
    		if "." in filename:
    			pass
    		elif filename.endswith(".mp3") or filename.endswith(".m4a"):
    			self.Music.append(os.path.join(path, filename))
    			self.Music1.append(filename)
    		else:
    			directory.append(os.path.join(path, filename))
    			
    			
    	directory1 = []
    	x = len(directory)
    	for name in range(x):
    		path = directory[name]
    		for filename in os.listdir(path):
    			if "." in filename:
    				pass
    			else:
    				directory1.append(os.path.join(path, filename))
    				
    	directory2 = []
    	x = len(directory1)
    	for name in range(x):
    		path = directory1[name]
    		for  filename in os.listdir(path):
    			if filename.endswith(".mp3") or filename.endswith(".m4a"):
    				self.Music.append(os.path.join(path, filename))
    				self.Music1.append(filename)
    			elif "." in filename or "_" in filename:
    				pass
    			else:
    				directory2.append(os.path.join(path, filename))
    	
    	directory3 = []
    	x = len(directory2)
    	for name in range(x):
    		path = directory2[name]
    		for filename in os.listdir(path):
    			if filename.endswith(".mp3") or filename.endswith(".m4a"):
    				self.Music.append(os.path.join(path, filename))
    				self.Music1.append(filename)
    			elif "." in filename or "_" in filename:
    				pass
    			else:
    				directory3.append(os.path.join(path, filename))
    	
		
   
    	
    	data = [{'text':str(1+i)+": "+str(self.Music1[i]),  'size_hint_x':1,'id':str(self.Music[i]),  'on_release': lambda x= i: self.play_music(self.Music[x], self.Music1[x])  } for i in range(len(self.Music))]
    	self.root.ids.rv.data = data

    	
    def play_music(self, text, text2):
          webbrowser.open(text)
         
          self.player = Player()
          self.player.play(text)
		
          self.root.ids.mist.text = str(text2)
          self.player.do_loop(True)
          self.name1 = str(text)
          self.name2 = text2    	  
          self.root.ids.m_play.icon = "pause"  	
    	    	    	    	
    
    def Play(self):
    	if self.root.ids.m_play.icon == "pause":
    		self.root.ids.m_play.icon = "play"
    		self.player.pause()
    		self.player.do_loop(True)    		
    	
    	elif self.root.ids.m_play.icon == "play":
    		self.root.ids.m_play.icon = "pause"
    		self.player.resume()
    		self.player.do_loop(True)
    		
    
    def Previous(self):
    	self.x -= 1
    	numx  = self.Music.index(self.name1) + self.x
    	num = numx
    	if num >= 0:
	    	self.player = Player()
	    	self.player.play(self.Music[num])
	    	self.root.ids.mist.text = str(self.Music1[num])
	    	self.player.do_loop(True) 
    	
    def Next(self):
    	self.x += 1
    	numx  = self.Music.index(self.name1) + self.x
    	num = numx
    	if num >= 1 or num <= (len(self.Music) - 1):
	    	self.player = Player()
	    	self.player.play(self.Music[num])
	    	self.root.ids.mist.text = str(self.Music1[num])
	    	self.player.do_loop(True) 
    	
    	

    	
    	
    	

                 
app().run()




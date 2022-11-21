from kivy.app import App
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import Clock
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kvdroid.tools.audio import Player
from kivy.core.window import Window
from kivymd.uix.picker import MDDatePicker, MDTimePicker, MDThemePicker
from kivymd.utils.fitimage import FitImage
from kivy.uix.button import Button





Code = """
MDBoxLayout:
	orientation: "vertical"
	MDNavigationLayout:
		MyManager:
			id: manage
			
			Screen:
				name: "home"
				BoxLayout:
					orientation: "vertical"
					
					ScreenManager:
						id: screen_manager
						
						
						HomeScreen:
							name: "Home"
							BoxLayout:
								orientation: "vertical"
								
								MDToolbar:
									title: "Home"
								
									md_bg_color: (1, .5, 0, 1)
									left_action_items: [["menu", lambda x : nav_drawer.set_state("toggle")]]
									elevation: 10
								
								MDBoxLayout:
									orientation: "vertical"
									size_hint: 1, .5
									pos_hint_y: {"center_x":.6}
									Label:
										size_hint: 1, .2
									
									OneLineIconListItem:
										size_hint: 1, 1
										text: "Videos"
										#theme_text_color: "Custom"
										#text_color: (1, .5, 0, 1)
										#line_color: (1, .5, 0, 1)
										on_press: root.ids.screen_manager.current = "Videos"
									
									OneLineIconListItem:
										size_hint: 1, 1
										text: "Music"
										#theme_text_color: "Custom"
										#text_color: (1, .5, 0, 1)
										#line_color: (1, .5, 0, 1)
										on_press: root.ids.screen_manager.current = "music"
									
									OneLineIconListItem:
										size_hint: 1, 1
										text: "Images"
										#theme_text_color: "Custom"
										#text_color: (1, .5, 0, 1)
										#line_color: (1, .5, 0, 1)
										on_press: root.ids.screen_manager.current = "images"
								
								Label:
									size_hint: 1, .2
									
									
									
																
	########################################	
	###### Video Screen #######################
						
						MyVideos:
							name: "Videos"
							BoxLayout:
								orientation: "vertical"
								
								MDToolbar:
									title: "Videos"
									md_bg_color: (1, .5, 0, 1)
									elevation: 10
									left_action_items: [["menu", lambda x : nav_drawer.set_state("toggle")]]
									right_action_items: [["dots-vertical"]]
									
								
								Label:
								
	
									
									
																	
	#########################################
	########### Music Screen ##################							
						Musicx:
							name: "music"
							BoxLayout:
								orientation: "vertical"
								
								MDToolbar:
									elevation: 10
									title: "Music"
									md_bg_color: (1, .5, 0, 1)
									left_action_items: [["menu", lambda x : nav_drawer.set_state("toggle")]]
									right_action_items: [["dots-vertical"]]
									
								RecycleView:
									id: Mike
									viewclass:'OneLineListItem'
									RecycleBoxLayout:
										orientation: "vertical"
										size_hint_y:None
										height:self.minimum_height
										
								MDRectangleFlatButton:
									id: mist
									size_hint_y: None
									height: dp(50)
									size_hint_x: 1
									#theme_text_color: "Custom"
									text_color: (1, .45, 0, 1)
									line_color: (1, 1, 1, 1)
							
								MDGridLayout:
									
									rows: 1
									cols: 3
									radius: dp(10)
									
									spacing: dp(self.width/6)
									size_hint_y: None
									height: dp(50)
									#md_bg_color: (1, .45, 0 ,1)
													
									MDIconButton:
										icon: "skip-previous"
										#theme_text_color: "Custom"
										#text_color: (1, 1, 1, 1)
										on_press: app.Previous()
										id: m_back
															
									MDIconButton:
										icon: "play"
										#theme_text_color: "Custom"
										#text_color: (1, 1, 1, 1)
										on_press: app.Play()
										id: m_play
														
									MDIconButton:
										icon: "skip-next"
										#theme_text_color: "Custom"
										#text_color: (1, 1, 1, 1)
										on_press: app.Next()
										id: m_next
								Label:
									size_hint: 1, None
									height: dp(10)
						
						
						
						
						
						
	#########################################
	######### Images ########################			
						Images:
							name: "images"
							BoxLayout:
								orientation: "vertical"
								id: cute
									
								MDToolbar:
									elevation: 10
									title: "Images"
									md_bg_color: (1, .5, 0, 1)
									left_action_items: [["menu", lambda x : nav_drawer.set_state("toggle")]]
									right_action_items: [["dots-vertical"]]
								MDBoxLayout:
									orientation: "vertical"
									
									RecycleView:
										id: Mike1
										viewclass: "FitImageL"
										RecycleGridLayout:
											cols: 3
											padding: dp(10)
											size_hint_y: None
											height:self.minimum_height
								
										
						OpenImage:
							id: cut
							name: "gift"
							MDBoxLayout:
								orientation: "vertical"			
										
								MDToolbar:
									title: "Image"
								
								Image:
									id: srt
									
								MDBottomAppBar:
									MDToolbar:
										icon: "home"
										icon: "music"	
							
	
		
																										
																											
	################################
	######## bottom app navugation #########													
					MDGridLayout:
						rows: 1
						cols: 5
						#md_bg_color: (1, .45, 0, 1)
						spacing : dp(self.width/20)
						size_hint_y: None
						height: dp(50)
									
						MDIconButton:
							icon: "home"
							#theme_text_color: "Custom"
							#text_color: (1, 1, 1, .9)
							on_press: root.ids.screen_manager.current = "Home"
										
						MDIconButton:
							icon: "video"
							#theme_text_color: "Custom"
							#text_color: (1, 1, 1, .9)
							on_press: root.ids.screen_manager.current = "Videos"
										
						MDIconButton:
							icon: "music"
							#theme_text_color: "Custom"
							#text_color: (1, 1, 1, .9)
							on_press: root.ids.screen_manager.current = "music"
										
						MDIconButton:
							icon: "image"
							#theme_text_color: "Custom"
							#text_color: (1, 1, 1, .9)
							on_press: root.ids.screen_manager.current = "images"
								
						MDIconButton:
							icon: "android"
							#theme_text_color: "Custom"
							#text_color: (1, 1, 1, .9)
															
							
							
							
							
	#####################################
	##### navigation #######################
	
		MDNavigationDrawer:
			id: nav_drawer
			MDBoxLayout:
				orientation: "vertical"
				spacing: dp(10)
				id: box
				
				MDToolbar:
					title: "BoldX Profile"
					md_bg_color: (1, .5, 0, 1)
					
				MDBoxLayout:
					orientation: "vertical"
					padding: dp(5)
					id: box
					radius: dp(10)
					#md_bg_color: (1,  .45, 0, 1)
					size_hint_y: .3
					
				OneLineListItem:
					text: "Change Theme"
					on_press: app.Theme_changer()
				OneLineListItem:
					text: "Settings"
				Label:
				
	
"""

Image = []
path = "//storage//emulated//0"

for root, dirs, files in os.walk(path):
	for file in files:		
		if file.endswith(".png") or file.endswith(".jpg"):
			Image.append( os.path.join(root, file))
Image.reverse()

Music = []
Music1 = []

for root, dirs, files in os.walk(path):
	for file in files:		
		if file.endswith(".mp3") or file.endswith(".m4a"):
			Music.append( os.path.join(root, file))
			Music1.append(file)



class HomeScreen(Screen):
	pass

class MyVideos(Screen):
	pass
	
class Musicx(Screen):
	pass


class Images(Screen):
	pass

class OpenImage(Screen):
	pass

class MyManager(ScreenManager):
	pass

class FitImageL(FitImage, Button):
	
	pass

class BoldX(MDApp):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.x = 0
	
	def build(self):
		#self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "Orange"
		builder = Builder.load_string(Code)
		max_iteration = -100
		return builder
	
	def on_start(self):
	   
	   data = [{"text": str(Music1[i]), "size_hint_x": 1,
                     "on_release": lambda x=i: self.play_music(Music[x], Music1[x])
                     } for i in range(len(Music))]
                     
	   self.root.ids.Mike.data = data
	   
	   
	   
	   data1 = [{ 'source':Image[i],"size_hint":(1, None), "height": dp(200), "on_release": lambda x=i: self.open_image(Image[x]) }  for i in range(len(Image)) ]
	   self.root.ids.Mike1.data = data1
	
	
	
	
	def open_image(self, srt):
		self.root.ids.venus.current = self.root.ids.cut.name
		self.root.ids.srt.source = srt
	
	
	
	
	def play_music(self, text, text2):
          
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
	   numx  = Music.index(self.name1) + self.x
	   num = numx
	   if num >= 0:
	    	self.player = Player()
	    	self.player.play(Music[num])
	    	self.root.ids.mist.text = str(Music1[num])
	    	self.player.do_loop(True) 
	
	def Next(self):
	   self.x += 1
	   numx  = Music.index(self.name1) + self.x
	   num = numx
	   if num >= 1 or num <= (len(Music) - 1):
	    	self.player = Player()
	    	self.player.play(Music[num])
	    	self.root.ids.mist.text = str(Music1[num])
	    	self.player.do_loop(True) 
	    	
	    	
	    	

	def Theme_changer(self):
	   picker = MDThemePicker()
	   picker.open()
    
		
		

BoldX().run()
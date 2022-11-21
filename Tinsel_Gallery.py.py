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
import os
from kivy.uix.recycleview import RecycleView
# from kvdroid.tools.audio import Player
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivymd.uix.button import MDFlatButton
from kivymd.uix.picker import MDDatePicker, MDTimePicker, MDThemePicker
from kivymd.uix.list import OneLineIconListItem, OneLineAvatarIconListItem,OneLineAvatarListItem, ImageLeftWidget, IconRightWidget, IconLeftWidget, ImageRightWidget
from kivymd.utils.fitimage import FitImage
from kivymd.uix.boxlayout import MDBoxLayout
from kvdroid.tools.font import system_font


Code = """
#: import system_font kvdroid.tools.font.system_font

#<MDLabel>
#	font_name: system_font("en")

#########################################
######### Images ########################	
MDBoxLayout:
	orientation: "vertical"
	
	MyManager:
		id: venus
		
		Images:
			name: "images"
		
			BoxLayout:
				orientation: "vertical"
				id: cute
		
				MDLabel:
					text: "Photos"
					theme_text_color: "Custom"
					size_hint_y: .15
					font_size: dp(20)
					padding: (20, 0)
					bold: True
					valign: "bottom"
					font_name: system_font()
				
		
				RecycleView:
					id: Mike1	
					viewclass: 'CustomImageItem'
		
					RecycleGridLayout:
						padding: dp(10)
						size_hint_y: None
						height: self.minimum_height
						do_scroll_x: True
						#orientation: 'vertical'
						cols: 3
						spacing: dp(10)
						
				MDGridLayout:
					rows: 2
					size_hint_y: None
					height: dp(60)
					#spacing: dp(self.width/6 + 2.5 )
					padding: (dp(20),0)
					
					MDGridLayout:
						rows: 1
						cols: 3
						padding: (dp(40), 0)
						spacing: dp(self.width/6)
						#row_default_width: dp(40)
						
						MDBoxLayout:
							orientation: "vertical"
							size_hint_x: None
							width: dp(45)
							MDIconButton:
								icon: "image"
								theme_text_color: "Custom"
								text_color: (0, .8, .2, 1)
							
							MDLabel:
								text: "Photos"
								theme_text_color: "Custom"
								text_color: (0, .8, .2, 1)
								halign: "center"
								font_size: dp(10)
								
						MDBoxLayout:
							orientation: "vertical"
							size_hint_x: None
							width: dp(45)
							
							MDIconButton:
								icon: "image-multiple-outline"
								on_release: venus.current = "folder"
								on_press: venus.transition.direction = "left"
							MDLabel:
								text: "Albums"
								halign: "center"
								font_size: dp(10)
						
						MDBoxLayout:
							orientation: "vertical"
							size_hint_x: None
							width: dp(45)
							
							MDIconButton:
								icon: "briefcase-variant-outline"
								on_release: venus.current = "tools"
							
							MDLabel:
								text: "Tools"
								halign: "center"
								font_size: dp(10)
					
							
		OpenImage:
			id: cut
			name: "cuu"
			MDBoxLayout:
				orientation: "vertical"
				
				MDGridLayout:
					id: toolbar
					size_hint_y: None
					height: dp(50)
					rows: 1
					
					MDIconButton:
						icon: "chevron-down"
						theme_text_color: "Custom"
						text_color: (0, .9, 0, 1)
						bold: True
						on_release: venus.current = "images"
						on_press: venus.transition.direction = "down"
					
					MDBoxLayout:
						orientation: "vertical"
						size_hint_x: .5
						
						MDLabel:
							text: "Aug 06, 2022"
							bold: True
							font_size: dp(15)
							padding: (dp(5), dp(5))
							
						MDLabel:
							text: "PM 01:32"
							font_size: dp(10)
							padding: (dp(5), dp(0))
					
					Label:
					
					MDIconButton:
						#icon: "facebook"
						#md_bg_color: (0, 0, .8, 1)
						theme_text_color: "Custom"
						text_color: (1, 1, 1, 1)
						font_size: dp(20)
					
					MDIconButton:
						#icon: "whatsapp"
						#md_bg_color: (0, .8, 0, 1)
						theme_text_color: "Custom"
						text_color: (1, 1, 1, 1)
					
					
					
				
				FitImage:
					id: srt
					#source: app.Srt
				
				MDGridLayout:
					rows: 1
					size_hint_y: None
					height: dp(60)
					padding: (dp(40),0)
					spacing: dp(40)
					
					MDBoxLayout:
						orientation: "vertical"
						MDIconButton:
							icon: "share-variant-outline"
						MDLabel:
							text: "share"
							font_size: dp(10)
							#halign: "center"
							padding: (dp(12), 2)
					
					
					MDBoxLayout:
						orientation: "vertical"
						MDIconButton:
							icon: "image-edit-outline"
						MDLabel:
							text: "edit"
							font_size: dp(10)
							padding: (dp(12), 2)
					
					
					MDBoxLayout:
						orientation: "vertical"
						MDIconButton:
							icon: "trash-can-outline"
						MDLabel:
							text: "delete"
							font_size: dp(10)
							padding: (dp(12), 2)
					
					
					MDBoxLayout:
						orientation: "vertical"
						MDIconButton:
							icon: "dots-vertical"
						MDLabel:
							text: "more"
							font_size: dp(10)
							padding: (dp(12), 2)
					
					
					
#				Widget:
#					size_hint: None, None
#					width: 100
#					height: 50
#
#					MDFloatingActionButton:
#				        id: float_btn
#				        icon: "chevron-left"
#				        x: 0
#				        y: toolbar.y/2 -self.height/2
#				        on_release: app.left()
#								
#					MDFloatingActionButton:
#				        id: float_btn
#				        icon: "chevron-right"
#				        
#				        x: toolbar.width -self.width
#				        y: toolbar.y/2 - self.height/2
#				        on_release: app.Right()
				
				


		ImageFolders:
			name: "folder"
			
			MDBoxLayout:
				orientation: "vertical"
				
				MDLabel:
					text: "Albums"
					size_hint_y: .15
					height: dp(50)
					md_bg_color: (1, 1, 1, .1)
					halign: "left"
					bold: True
					font_size: dp(20)
					valign: "bottom"
					padding: (dp(20),dp(50))
				
				RecycleView:
					id: folder
					viewclass: "CustomFolders"
					
					RecycleGridLayout:
						cols: 3
						padding: dp(15)
						size_hint_y: None
						height: self.minimum_height
						do_scroll_x: False
						spacing: dp(10)
						#row_default_height: dp(200)
						spacing: dp(10)
						radius: dp(15)
									
				MDGridLayout:
					rows: 1
					cols: 3
					padding: (dp(40), 5)
					spacing: dp(self.width/6 )
					#row_default_width: dp(40)
					size_hint_y: None
					height: dp(60)
						
					MDBoxLayout:
						orientation: "vertical"
						size_hint_x: None
						width: dp(45)
							
						MDIconButton:
							icon: "image"
							on_release: venus.current = "images"
							on_press: venus.transition.direction = "right"
						MDLabel:
							text: "Photos"
							theme_text_color: "Custom"
							#text_color: (0, .8, .2, 1)
							halign: "center"
							font_size: dp(10)
								
					MDBoxLayout:
						orientation: "vertical"
						size_hint_x: None
						width: dp(45)
						MDIconButton:
							icon: "image-multiple-outline"
							theme_text_color: "Custom"
							text_color: (0, .8, .2, 1)
						MDLabel:
							text: "Albums"
							halign: "center"
							theme_text_color: "Custom"
							text_color: (0, .8, .2, 1)
							font_size: dp(10)
					
					MDBoxLayout:
						orientation: "vertical"
						size_hint_x: None
						width: dp(45)
						MDIconButton:
							icon: "briefcase-variant-outline"
							on_release: venus.current = "tools"
						MDLabel:
							text: "Tools"
							halign: "center"
							font_size: dp(10)

		
		ImageDir:
			name: "imagesub"
			MDBoxLayout:
				orientation: "vertical"
				
				MDBoxLayout:
					#padding: dp(10)
					size_hint_y: None
					height: dp(40)
					id: top
					Widget:
						size_hint_x: .2
						MDIconButton:
							icon: "arrow-left"
							theme_text_color: "Custom"
							text_color: (0, .5, 0, .7)
							on_release: venus.current = "folder"
							pos_hint: None, None
							pos: dp(10), top.y-self.width/6
					MDLabel:
						text: "Screenshot"
						id: fold
						halign: "left"
						#font_size: dp(10)
						bold: True
					
				MDLabel:
					text: "sep"
					size_hint_y: None
					font_size: dp(10)
					height: dp(40)
					padding: ( dp(30), 0)
				
				RecycleView:
					id: foldee
					viewclass: "CustomFolders"
					
					RecycleGridLayout:
						cols: 4
						size_hint_y: None
						height: self.minimum_height
						do_scroll_x: False
						spacing: dp(5)
						radius: dp(15)
				Label:
					size_hint_y: .0001
				
				
		
		
		ToolsScreen:
			name: "tools"
			MDBoxLayout:
				orientation: "vertical"
				padding: dp(15)
				md_bg_color: (1, 1, 1, .2)
				#spacing: dp(5)
				MDLabel:
					text: "Tools"
					halign: "left"
					bold: True
					size_hint_y: .23
					font_size: dp(20)
				
				MDBoxLayout:
					size_hint_y: .27
					md_bg_color: (0, .4, .2, 1)
					padding: dp(15)
					orientation : "vertical"
					radius: (dp(10), dp(10), dp(0), dp(0))
					
					MDBoxLayout:
						MDLabel:
							text: "3.4%"
							#font_size: dp(20)
							halign: "left"
							theme_text_color: "Custom"
							text_color: (1, 1, 1, 1)
							size_hint_x: None
						
						MDLabel:
						
						MDIconButton:
							icon: "image"
							theme_text_color: "Custom"
							text_color: (1, 1, 1, 1)
							size_hint_x: None
						
						MDLabel:
							text: "5151"
							halign: "right"
							theme_text_color: "Custom"
							text_color: (1, 1, 1, 1)
							size_hint_x: None
					
					MDBoxLayout:
						MDLabel:
							text: "Memory consumed by photos"
							font_size: dp(10)
							halign: "left"
							theme_text_color: "Custom"
							text_color: (1, 1, 1, 1)
						
						MDLabel:
						
						
						MDLabel:
							halign: "right"
							text: "Total 1.1GB"
							font_size: dp(10)
							theme_text_color: "Custom"
							text_color: (1, 1, 1, 1)
							
					MDProgressBar:
						max: 100
						min: 0
						value: 15
				
				MDBoxLayout:
					#orientation: "vertical"
					md_bg_color: (1, 1, 1, 1)
					size_hint_y: .27
					padding: (dp(40), 0)
					
					MDGridLayout:
						rows: 2
						cols: 1
						size_hint_x: .6
						MDIconButton:
							icon: "format-clear"
							theme_text_color: "Custom"
							text_color: (0, .5, 0, .7)
						MDLabel:
							text: "Clean Photos"
							bold: True
							font_size: dp(11)
							
					Label:
						
					MDGridLayout:
						rows: 2
						cols: 1
						size_hint_x: .6
						MDIconButton:
							icon: "vibrate"
							theme_text_color: "Custom"
							text_color: (0, .5, 0, .7)
						MDLabel:
							text: "Compress photos"
							bold: True
							font_size: dp(11)
				MDLabel:
					size_hint_y: .1
				CustomButton:
					radius: dp(10)
					md_bg_color: (1, 1, 1, 1)
					background_normal: ""
					background_color: (1, 1, 1, .2)
					size_hint_y: .15
					MDIconButton:
						icon: "collage"
						size_hint_x: .15
						theme_text_color: "Custom"
						text_color: (0, .5, 0, .7)
					MDLabel:
						text: "Collage"
						halign: "left"
					
					MDIconButton:
						icon: "chevron-right"
						theme_text_color: "Custom"
						text_color: (.5, .5, .5, 1)
						size_hint_x: .15
				
				MDLabel:
					size_hint_y: .1
						
				CustomButton:
					radius: dp(10)
					md_bg_color: (1, 1, 1, 1)
					background_color: (1, 1, 1, .2)
					background_normal: ""
					size_hint_y: .15
					MDIconButton:
						icon: "folder-key"
						size_hint_x: .15
						theme_text_color: "Custom"
						text_color: (0, .5, 0, .7)
					MDLabel:
						text: "Xhide"
						halign: "left"
					
					MDIconButton:
						icon: "chevron-right"
						theme_text_color: "Custom"
						text_color: (.5, .5, .5, 1)
						size_hint_x: .15	
				
				MDLabel:
					size_hint_y: .08
				
				CustomButton:
					background_normal: ""
					background_color: (1, 1, 1, .2)
					size_hint: .35, .1
					pos_hint: {"center_x": .5}
					
					MDLabel:
						text: "About AI Gallery"
						halign: "center"
					MDIconButton:
						icon: "chevron-right"
						theme_text_color: "Custom"
						text_color: (.5, .5, .5, 1)
				Label:
				
				
				MDGridLayout:
					rows: 1
					cols: 3
					padding: (dp(40), 5)
					spacing: dp(self.width/6 )
					#row_default_width: dp(40)
					size_hint_y: None
					height: dp(60)
						
					MDBoxLayout:
						orientation: "vertical"
						size_hint_x: None
						width: dp(45)
							
						MDIconButton:
							icon: "image"
							on_release: venus.current = "images"
							on_press: venus.transition.direction = "right"
						MDLabel:
							text: "Photos"
							theme_text_color: "Custom"
							#text_color: (0, .8, .2, 1)
							halign: "center"
							font_size: dp(10)
								
					MDBoxLayout:
						orientation: "vertical"
						size_hint_x: None
						width: dp(45)
						MDIconButton:
							icon: "image-multiple-outline"
							on_release: venus.current = "folder"
							on_press: venus.transition.direction = "left"
						MDLabel:
							text: "Albums"
							halign: "center"
							#theme_text_color: "Custom"
#							text_color: (0, .8, .2, 1)
							font_size: dp(10)
					
					MDBoxLayout:
						orientation: "vertical"
						size_hint_x: None
						width: dp(45)
						MDIconButton:
							icon: "briefcase-variant-outline"
							on_release: venus.current = "tools"
							theme_text_color: "Custom"
							text_color: (0, .8, .2, 1)
						MDLabel:
							text: "Tools"
							halign: "center"
							font_size: dp(10)
							theme_text_color: "Custom"
							text_color: (0, .8, .2, 1)
					
				
			


"""
Image = []
Image1 = []
path = "//storage//emulated//0"
pathx = "//storage//emulated//0//Dcim//Camera"

for root, dirs, files in os.walk(pathx):
	for file in files:		
		if file.endswith(".png") or file.endswith(".jpg"):
			Image.append( os.path.join(root, file))
			Image1.append(file)

image_dir = [path]
image_dir1 = ["Root"]
for root, dirs, files in os.walk(path):
    for dir in dirs:
        x = os.path.join(root, dir)
        y = dir
        
        if y[0].isupper() or "Facebook" in y or "facebook" in y:
        	
        	if "1" in y or "2" in y or "3" in y or "4" in y or "5" in y or "6" in y or "7" in y or "8" in y or "9" in y:
        		pass
        		
        	else:
        	
		        for v in os.listdir(x):
		            if v.endswith(".png") or v.endswith(".jpg"):
		                if x in image_dir:
		                    pass
		                else:
		                    image_dir.append(x)
		                    image_dir1.append(y)
                    
fold_img= []
root_img = []
for path in image_dir:                    
	for root, dirs, files in os.walk(path):
		for file in files:
			
			if file.endswith(".png") or file.endswith(".jpg"):
				fix = os.path.join(root, file)
				
	fold_img.append(fix)
	root_img.append(root)
					
		
		

class CustomImageItem(FitImage, Button):
    def on_release(self):
    	self.root.ids.venus.current = "cut"
    	self.root.ids.venus.transition.direction = "left"
    	
class CustomFolders(FitImage, Button):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.background_normal = ""
		self.background_color = (1, 1, 1, .2)

class CustomButton( MDBoxLayout, Button):
	pass

class MyManager(ScreenManager):
	pass	

class Images(Screen):
    pass

class OpenImage(Screen):
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		#self.name = 'open'
	
class ImageFolders(Screen):
	pass

class ToolsScreen(Screen):
	pass

class ImageDir(Screen):
	pass


class BoldX(MDApp, MyManager):
    
    def Right(self):
    	y = Image.index(self.root.ids.srt.source)  +1
    	self.root.ids.srt.source = Image[y]
    	self.root.ids.toolbar.text = str(Image1[y])
    	
    def left(self):
    	y = Image.index(self.root.ids.srt.source) - 1
    	
    	self.root.ids.srt.source = Image[y]
    	self.root.ids.toolbar.text = str(Image1[y])
    
    def right(self):
    	pass
    
    def open_image(self, srt):
    	self.tik = srt
    	self.root.ids.venus.current = "cuu"
    	self.root.ids.srt.source = srt
    	
    	
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.x = 0
        self.Srt = Image[3]
        
    def open_dir(self, x, y):
    	self.root.ids.venus.current = "imagesub"
    	self.root.ids.fold.text = y
    	path = x
    	fp = []
    	for root, dirs, files in os.walk(path):
    		for file in files:
    			if file.endswith(".png") or file.endswith(".jpg"):
    				fp.append(os.path.join(root, file))
    	data = [{ "size_hint": (1, None),"source": fp[i],"height":dp(150)} for i in range(len(fp))]
    	self.root.ids.foldee.data = data
                

    def build(self):
        #self.theme_cls.theme_style = "Dark"
        #self.theme_cls.primary_palette = "Orange"
        builder = Builder.load_string(Code)
        #max_iteration = -40
        return builder

    def on_start(self):
        data1 = [{ "size_hint": (1, None),"height":dp(200),"source": Image[i], "on_release": lambda x=i: self.open_image(Image[x]) } for i in range(len(Image))]
        self.root.ids.Mike1.data = data1
        
        data = [{ "size_hint": (1, None),"text": image_dir1[i],"source": fold_img[i],"height":dp(150), "on_release": lambda x=i: self.open_dir(image_dir[x], image_dir1[x]) } for i in range(len(image_dir))]
        self.root.ids.folder.data = data
                
       


BoldX().run()

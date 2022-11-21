import random

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton, MDIconButton
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import Clock
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition, WipeTransition
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.list import OneLineAvatarIconListItem, IconLeftWidget, IconRightWidget, MDList, OneLineListItem
from kivymd.uix.picker import MDThemePicker
from kivymd.uix.textfield import MDTextField
from kivymd.uix.tooltip import MDTooltip
from kivymd.utils.fitimage import FitImage
from kivy.uix.button import Button
import os
from kvdroid.tools.audio import Player
from kivymd.uix.menu import MDDropdownMenu
from threading import Thread
import time

# import stagger


Window.size = (dp(400), Window.height)
print(Window.height)

Code = """
#: import ew kivy.uix.effectwidget

MDNavigationLayout:
######################################
############# Custom ScreenManager ####
    MyScreenManager:
        id: my_manager


######################################
############ Opening Screen ###########    
        IntroScreen:
            
            Label:
                text: "Last of a dying BREED \\n The Founding TITAN"
                bold: True
                color: (1, .5, 0, 1)
                font_size: dp(35)
                halign: "center"
                font_name: "VINERITC.TTF"



######################################
########### Home Screen #############
                
        HomeScreen:
            id: home
            name: "home screen"
            EffectWidget:
                effects: [ew.VerticalBlurEffect(size=10), ew.HorizontalBlurEffect(size=10)]
                
                FitImage:
                    #source: "FB_IMG_1580579556493.jpg"
                
            MDBoxLayout:
                orientation: "vertical"
                id: grid
                MDToolbar:
                    title: "Tinsel Player"
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("toggle")]]
                    #md_bg_color: (1, .5, 0, 1)
                
                MDBoxLayout:
                    orientation: "vertical"
                    size_hint: .9, .8
                    pos_hint: {"center_x":.5}
                    padding: dp(10)
                    #md_bg_color: (1, .5, 0, 1)
                    
                    MDSwiper:
                    	MDSwiperItem:
                            
                            MDBoxLayout:
                                orientation: "vertical"
                                MyButton:
                                    source: "FB_IMG_1582214921055.jpg"
                                    #background_color: (1, .5, 0, .85)
                                    size_hint: 1, 1
                                    bold: True
                                    font_size: dp(20)
                                    on_release: root.ids.my_manager.current = "music screen"
                                    
                                MDLabel:
                                    text: "My Music"
                                    size_hint_y:  None
                                    height: dp(20)
                                    halign: "center"
                                    bold: True
                                    theme_text_color: "Custom"
                                    text_color: (1, .7, 0, 1)
		                        
		                        
                        
                        MDSwiperItem:   
                            MDBoxLayout:
                                orientation: "vertical"
                                MyButton:
                                    source: "FB_IMG_1582299548421.jpg" 
                                    size_hint: 1, 1
                                    bold: True
                                    font_size: dp(20)
                                    on_release: root.ids.my_manager.current = "stream"
                                MDLabel:
                                    text: "Stream Favourite \\n Songs & Artist"
                                    size_hint_y:  None
                                    height: dp(35)
                                    halign: "center"
                                    bold: True
                                    theme_text_color: "Custom"
                                    text_color: (1, .7, 0, 1)
		                        
                    	MDSwiperItem:
                    	    MDBoxLayout:
                                orientation: "vertical"
                                MyButton:
                                    source: "FB_IMG_1584375455095.jpg" 
                                    size_hint: 1, 1
                                    bold: True
                                    font_size: dp(20)
                                    on_release: root.ids.my_manager.current = "recent screen"
                                    on_press: app.add_recent()
                                    
                                MDLabel:
                                    text: "Recently Played"
                                    size_hint_y:  None
                                    height: dp(35)
                                    halign: "center"
                                    bold: True
                                    theme_text_color: "Custom"
                                    text_color: (1, .7, 0, 1)


                    	MDSwiperItem:
		                    MDBoxLayout:
                                orientation: "vertical"
                                MyButton:
                                    source: "FB_IMG_1582079773638.jpg" 
                                    background_normal: ""
                                    background_color: (1, .5, 0, .85)
                                    size_hint: 1, 1
                                    bold: True
                                    font_size: dp(20)
                                    on_release: root.ids.my_manager.current = "playlist screen"
		                        MDLabel:
                                    text: "Playlist"
                                    size_hint_y:  None
                                    height: dp(35)
                                    halign: "center"
                                    bold: True
                                    theme_text_color: "Custom"
                                    text_color: (1, .7, 0, 1)
                                    
                    	MDSwiperItem:
		                    MDBoxLayout:
                                orientation: "vertical"
                                MyButton:
                                    source: "FB_IMG_1586136247462.jpg" 
                                    background_normal: ""
                                    background_color: (1, .5, 0, .85)
                                    size_hint: 1, 1
                                    bold: True
                                    font_size: dp(20)
                                    on_release: root.ids.my_manager.current = "favourite screen"
                                MDLabel:
                                    text: "Favourites"
                                    size_hint_y:  None
                                    height: dp(35)
                                    halign: "center"
                                    bold: True
                                    theme_text_color: "Custom"
                                    text_color: (1, .7, 0, 1)
                                    
                        MDSwiperItem:
                    
		                    MDBoxLayout:
                                orientation: "vertical"
                                MyButton:
                                    source: "FB_IMG_1582164320826.jpg" 
                                    background_normal: ""
                                    background_color: (1, .5, 0, .85)
                                    size_hint: 1, 1
                                    bold: True
                                    font_size: dp(20)
                                    on_release: root.ids.my_manager.current = "folders"
                                MDLabel:
                                    text: "Music Folders"
                                    size_hint_y:  None
                                    height: dp(35)
                                    halign: "center"
                                    bold: True
                                    theme_text_color: "Custom"
                                    text_color: (1, .7, 0, 1)
                                    
                        MDSwiperItem:
		                    MDBoxLayout:
                                orientation: "vertical"
                                MyButton:
                                    source: "FB_IMG_1581249392227.jpg" 
                                    background_normal: ""
                                    background_color: (1, .5, 0, .85)
                                    size_hint: 1, 1
                                    bold: True
                                    font_size: dp(20)
                                    on_release: root.ids.my_manager.current = "artist"
		                        
		                        MDLabel:
                                    text: "Class Artist"
                                    size_hint_y:  None
                                    height: dp(35)
                                    halign: "center"
                                    bold: True
                                    theme_text_color: "Custom"
                                    text_color: (1, .7, 0, 1)
                    
                    MDBoxLayout:
                        orientation: "horizontal"
                        size_hint: 1, None
                        #md_bg_color: (1, .6, 0, 1)
                        height: dp(50)
                        
                        MDFloatingActionButton:
                            icon: "play"
                            size_hint_x: None
                            width: dp(50)
                            id: play1
                            elevation: 10
                            on_release: app.dirout_play()
                            canvas.before:
                            	Color:
                            		rgba: 1, 1, 1, 1
								Ellipse:
									pos: self.x - dp(10/2), self.y - dp(10/2)
									size: self.width + dp(10), self.height + dp(10)
                        
                        OneLineAvatarIconListItem:
                            id: music_nameh
                            on_press: app.SCREEN_LIST.append(home.name)
                            on_release: root.ids.my_manager.current = "music ui"
                            
                Widget:
                    size_hint_y: None
                    height: dp(50)
                    
                    

##########################################
############### Music Screen ############
        MusicScreen:
            id: music
            name: "music screen"
            EffectWidget:
                effects: [ew.VerticalBlurEffect(size=10), ew.HorizontalBlurEffect(size=10)]
                
                #FitImage:
                    #source: "FB_IMG_1580579556493.jpg"
                
            MDBoxLayout:
                orientation: "vertical"
                
                MDBackdrop:
                    id: back
                    title: "Music"
                    left_action_items: [["magnify", lambda x: app.open()]]
                    header_text: "search music"
                    #md_bg_color: (1, .5, 0, 1)
                
                    MDBackdropBackLayer:
                        MDBoxLayout:
                            orientation: "vertical"
                            padding: dp(10)
                            #md_bg_color: (1, .5, 0, 1)
                            
                            
                            MDTextField:
                                id: TSearch
                                hint_text: "enter music name"
                                size_hint_y: None
                                height: dp(70)
                                theme_text_color: "Custom"
                                text_color: (0, 0, 0, 1)
                                md_bg_color: (0, 0, 0, 1)
                                
                            MDGridLayout:
                                cols: 2
                                rows: 1
                                size_hint: .5, None
                                height: dp(100)
                                pos_hint: {"center_x":.5}
                                spacing: self.width/3
                                
                                
                                MDIconButton:
                                    icon: "magnify"
                                    on_release: app.Music_Search()
                                    #md_bg_color: (0, 0, 0, 1)
                                
                                MDIconButton:
                                    icon: "delete"
                                    on_release: TSearch.text = "" 
                                    on_press: app.Delete_Search()
                                  
                                    						
                                    #md_bg_color: (0, 0, 0, 1)
                                    
                            RecycleView:
                            	id: sf
                            	viewclass: "SearchedIconItem"
                            	RecycleBoxLayout:
                            		orientation: "vertical"
                            		size_hint_y: None
                            		height: self.minimum_height
                            Label:
                            	size_hint_y: None
                            	height: dp(100)
                            
                                
                    
                    MDBackdropFrontLayer:
                        MDBoxLayout:
                            orientation: "vertical"
                            #md_bg_color: (1, .5, 0, 1)
                    
                    
                    
                            CustomRecycleView:
                                id: rv
                                viewclass: "CustomIconItem"
                                RecycleBoxLayout:
                                    orientation: "vertical"
                                    size_hint_y: None
                                    height: self.minimum_height
                            
			                MDBoxLayout:
			                	orientation: "horizontal"
			                    size_hint: 1, None
			                    height: dp(50)
			                    padding: dp(10)
			                        
								MDFloatingActionButton:
									icon: "play"
			                        size_hint_x: None
			                        width: dp(50)
			                        id: play2
			                        elevation: 10
			                        on_release: app.dirin_play()
			                        
								OneLineAvatarIconListItem:
									id: music_namem
									on_press: app.SCREEN_LIST.append(music.name)
									on_release: root.ids.my_manager.current = "music ui"
									on_press: root.ids.my_manager.transition.direction = "left"
                            Widget:
			                    size_hint_y: None
			                    height: dp(50)
			                    
			                    MDFloatingActionButton:
							        id: float_btn
							        icon: "home"
							        x: back.center_x - self.width/2
							        y: back.height - (self.height*1.5)
							        #md_bg_color: (1, .5, 0, 1)
							        on_release: root.ids.my_manager.current = "home screen"
							        canvas.before:
							            Color:
							                
							                rgba: 1, 1, 1, 1
							            Ellipse:
							                pos: self.x - dp(10/2), self.y - dp(10/2)
							                size: self.width + dp(10), self.height + dp(10)
                                    
##########################################
############### Stream Music Screen ############
        StreamMusic:
            name: "stream"
            EffectWidget:
                effects: [ew.VerticalBlurEffect(size=10), ew.HorizontalBlurEffect(size=10)]
                
                FitImage:
                    #source: "FB_IMG_1580579556493.jpg"
                
            MDBoxLayout:
                orientation: "vertical"
                
                
                
                Label:
                
                MDBottomAppBar:
                    MDToolbar:
                        md_bg_color: (1, .5, 0, 1)
                        icon: "home"
                        type: "bottom"


##########################################
############### Music folders Screen ############
        MusicFolders:
            id: fold1
            name: "folders"
            EffectWidget:
                effects: [ew.VerticalBlurEffect(size=10), ew.HorizontalBlurEffect(size=10)]
                
                FitImage:
                    #source: "FB_IMG_1580579556493.jpg"
                
            MDBoxLayout:
                orientation: "vertical"
                
                MDToolbar:
                    #md_bg_color: (1, .5, 0, 1)
                    id: toolf1
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("toggle")]]
                    title: "Music Folders"
                
                MDBoxLayout:
                    orientation: "vertical"
                    padding: dp(10)
                
                    RecycleView:
                        id: rff
                        viewclass: "MusicDirectoryItem"
                        RecycleBoxLayout:
                            orientation: "vertical"
                            size_hint_y: None
                            height: self.minimum_height
                    
                    MDBoxLayout:
                        orientation: "horizontal"
                        size_hint: 1, None
                        height: dp(50)
                        
                        MDFloatingActionButton:
                            icon: "play"
                            size_hint_x: None
                            width: dp(50)
                            id: play_dir1
                            elevation: 10
                            on_release: app.dirout_play()
                        
                        OneLineAvatarIconListItem:
                            id: sub_dir_item1
                            on_press: app.SCREEN_LIST.append(fold1.name)
                            on_release: root.ids.my_manager.current = "music ui"
                
                Widget:
                    size_hint_y: None
                    height: dp(50)
                    
                    MDFloatingActionButton:
				        id: float_btn
				        icon: "home"
				        x: toolf1.center_x - self.width/2
				        y: toolf1.y - self.height/2
				        #md_bg_color: (1, .5, 0, 1)
				        on_release: root.ids.my_manager.current = "home screen"
				        canvas.before:
				            Color:
				                rgba: root.md_bg_color
				                rgba: 1, 1, 1, 1
				            Ellipse:
				                pos: self.x - dp(10/2), self.y - dp(10/2)
				                size: self.width + dp(10), self.height + dp(10)                

##############################################################
############### Music folders display songs Screen ############
        MusicFoldersDisplay:
            id: fold2
            name: "folder music"
            EffectWidget:
                effects: [ew.VerticalBlurEffect(size=10), ew.HorizontalBlurEffect(size=10)]
                
                FitImage:
                    #source: "FB_IMG_1580579556493.jpg"
			                
            MDBoxLayout:
                orientation: "vertical"
                
                MDToolbar:
                    #md_bg_color: (1, .5, 0, 1)
                    id: folder_music
                    left_action_items: [["chevron-left", lambda x: app.Folder_Back()]]
                    title: "Contents"
                
                MDBoxLayout:
                    orientation: "vertical"
                    padding: dp(10)
                    
                    RecycleView:
                        id: content_music
                        viewclass: "PlayMusicDirectory"
                        RecycleBoxLayout:
                            orientation: "vertical"
                            size_hint_y: None
                            height: self.minimum_height
                    
                    MDBoxLayout:
                        orientation: "horizontal"
                        size_hint: 1, None
                        height: dp(50)
                        
                        MDFloatingActionButton:
                            icon: "play"
                            size_hint_x: None
                            width: dp(50)
                            id: play_dir2
                            elevation: 10
                            on_release: app.dirin_play()
                        
                        OneLineAvatarIconListItem:
                            id: sub_dir_item2
                            on_press: app.SCREEN_LIST.append(fold2.name)
                            on_release: root.ids.my_manager.current = "music ui"
                            on_press: root.ids.my_manager.transition.direction = "left"
				 
                Widget:
                    size_hint_y: None
                    height: dp(50)
                    
                    MDFloatingActionButton:
				        id: float_btn
				        icon: "home"
				        x: folder_music.center_x - self.width/2
				        y: folder_music.y - self.height/2
				        #md_bg_color: (1, .5, 0, 1)
				        on_release: root.ids.my_manager.current = "home screen"
				        canvas.before:
				            Color:
				                rgba: root.md_bg_color
				                rgba: 1, 1, 1, 1
				            Ellipse:
				                pos: self.x - dp(10/2), self.y - dp(10/2)
				                size: self.width + dp(10), self.height + dp(10)                               


#####################################################################
############### Music Artist classification Screen Screen ############
        ClassArtist:
            name: "artist"
            EffectWidget:
                effects: [ew.VerticalBlurEffect(size=10), ew.HorizontalBlurEffect(size=10)]
                
                FitImage:
                    #source: "FB_IMG_1580579556493.jpg"
                
            MDBoxLayout:
                orientation: "vertical"
                
                MDToolbar:
                    id: toolbarR
                    title: "Artist"
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("toggle")]]
                    #md_bg_color: (1, .5, 0, 1)
                
                RecycleView:
                    id: ra
                    viewclass: "RecentItem"
                    RecycleBoxLayout:
                        orientation: "vertical"
                        size_hint_y: None
                        height: self.minimum_height
                
                Label:

                       
                      

##########################################
############### Recently Screen ############
        RecentlyScreen:
            id: recent
            name: "recent screen"
            EffectWidget:
                effects: [ew.VerticalBlurEffect(size=10), ew.HorizontalBlurEffect(size=10)]
                
                FitImage:
                    #source: "FB_IMG_1580579556493.jpg"
			                
            MDBoxLayout:
                orientation: "vertical"
                
                MDToolbar:
                    id: toolbarR
                    title: "Recently Played"
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("toggle")]]
                    #md_bg_color: (1, .5, 0, 1)
                   
                    
                
                RecycleView:
                    id: rr
                    viewclass: "RecentItem"
                    RecycleBoxLayout:
                        orientation: "vertical"
                        size_hint_y: None
                        height: self.minimum_height
				                
                MDBoxLayout:
                	orientation: "horizontal"
                    size_hint: 1, None
                    height: dp(50)
                    padding: dp(10)
                        
                    MDFloatingActionButton:
                    	icon: "play"
                        size_hint_x: None
                        width: dp(50)
                        id: play3
                        elevation: 10
                        on_release: app.Play()
                        
					OneLineAvatarIconListItem:
						id: music_namer
						on_press: app.SCREEN_LIST.append(recent.name)
                        on_release: root.ids.my_manager.current = "music ui"
                            
               
								                    
                Widget:
                    size_hint_y: None
                    height: dp(50)
                    
                    MDFloatingActionButton:
				        id: float_btn
				        icon: "home"
				        x: toolbarR.center_x - self.width/2
				        y: toolbarR.y - self.height/2
				        #md_bg_color: (1, .5, 0, 1)
				        on_release: root.ids.my_manager.current = "home screen"
				        canvas.before:
				            Color:
				                rgba: root.md_bg_color
				                rgba: 1, 1, 1, 1
				            Ellipse:
				                pos: self.x - dp(10/2), self.y - dp(10/2)
				                size: self.width + dp(10), self.height + dp(10)
				               
                        
                    
                

##########################################
############### Favourite Screen ############
        FavouriteScreen:
            id: favour
            name: "favourite screen"
            EffectWidget:
                effects: [ew.VerticalBlurEffect(size=10), ew.HorizontalBlurEffect(size=10)]
                
                FitImage:
                    #source: "FB_IMG_1580579556493.jpg"
                
            MDBoxLayout:
                orientation: "vertical"
                
                MDToolbar:
                    title: "Favourites"
                    id: toolbarF
                    #md_bg_color: (1, .5, 0, 1)
                    
                RecycleView:
                    id: rf
                    viewclass: "FavouriteIconItem"
                    RecycleBoxLayout:
                        orientation: "vertical"
                        size_hint_y: None
                        height: self.minimum_height
                
                MDBoxLayout:
					orientation: "horizontal"
					size_hint: 1, None
					height: dp(50)
					padding: dp(10)
					
					MDFloatingActionButton:
						icon: "play"
						size_hint_x: None
						width: dp(50)
						id: play4
						elevation: 10
						on_release: app.dirin_play()
						
					OneLineAvatarIconListItem:
						id: music_namef
						on_press: app.SCREEN_LIST.append(favour.name)
						on_release: root.ids.my_manager.current = "music ui"
						on_press: root.ids.my_manager.transition.direction = "left"
                            
                Widget:
                    size_hint_y: None
                    height: dp(50)
                    
                    MDFloatingActionButton:
				        id: float_btn
				        icon: "home"
				        x: toolbarF.center_x - self.width/2
				        y: toolbarF.y - self.height/2
				        #md_bg_color: (1, .5, 0, 1)
				        on_release: root.ids.my_manager.current = "home screen"
				        canvas.before:
				            Color:
				                rgba: root.md_bg_color
				                rgba: 1, 1, 1, 1
				            Ellipse:
				                pos: self.x - dp(10/2), self.y - dp(10/2)
				                size: self.width + dp(10), self.height + dp(10)
                        
                    
                

##########################################
############### Playlist Screen ############
        PlaylistScreen:
            id: playlist
            name: "playlist screen"
            EffectWidget:
                effects: [ew.VerticalBlurEffect(size=10), ew.HorizontalBlurEffect(size=10)]
                
                FitImage:
                    #source: "FB_IMG_1580579556493.jpg"
                
            MDBoxLayout:
                orientation: "vertical"
                
                MDToolbar:
                    title: "Playlist" 
                    id: toolbarP
                    #md_bg_color: (1, .5, 0, 1)
                
                PlayListRecycleView:
                    id: rp
                    viewclass: "OneLineIconListItem"
                    RecycleBoxLayout:
                        #cols: 2
                        spacing: dp(10)
                        orientation: "vertical"
                        size_hint_y: None
                        height: self.minimum_height
                        
                MDBoxLayout:
                	orientation: "vertical"
                	padding: dp(10)
                
	                MDBoxLayout:
	                	orientation: "horizontal"
	                    size_hint: 1, None
	                    height: dp(50)
	                        
						MDFloatingActionButton:
							icon: "play"
	                        size_hint_x: None
	                        width: dp(50)
	                        id: play5
	                        elevation: 10
	                        on_release: app.dirin_play()
	                        
						OneLineAvatarIconListItem:
							id: music_namep
							on_press: app.SCREEN_LIST.append(playlist.name)
							on_release: root.ids.my_manager.current = "music ui"
							on_press: root.ids.my_manager.transition.direction = "left"
                            
                Widget:
                    size_hint_y: None
                    height: dp(50)
                    
                    MDFloatingActionButton:
				        id: float_btn
				        icon: "home"
				        x: toolbarP.center_x - self.width/2
				        y: toolbarP.y - self.height/2
				        #md_bg_color: (1, .5, 0, 1)
				        on_release: root.ids.my_manager.current = "home screen"
				        canvas.before:
				            Color:
				                rgba: root.md_bg_color
				                rgba: 1, 1, 1, 1
				            Ellipse:
				                pos: self.x - dp(10/2), self.y - dp(10/2)
				                size: self.width + dp(10), self.height + dp(10)
   
                        
#############################################
############# MusicUi Screen ##############                 

        MusicUi:
            name: "music ui"
            EffectWidget:
                effects: [ew.VerticalBlurEffect(size=10), ew.HorizontalBlurEffect(size=10)]
                
                FitImage:
                    #source: "FB_IMG_1580579556493.jpg"
                
            MDBoxLayout:
                orientation: "vertical"
                #md_bg_color: (1, .5, 0, 1)
                id: tool
                
                Label:            
                
                MDGridLayout:
                    size_hint_y: .55
                    #height: dp(10)
                    rows: 4
                    cols: 1
                    spacing: dp(10)
                    padding: dp(10)
                    MDBoxLayout:
                        padding: dp(5)
                        
                        
                        MDLabel:
                            size_hint_x: None
                            id: Music_ctime
                            width: dp(35)
                            text: "00:00"
                            
                        MDSlider:
                            orientation: "horizontal"
                            id: jack
       
                           
                            cursor_image: ""
                            cursor_size: (dp(10), dp(10))
                            background_width: dp(20)
                            #value_track_color: (1, 0, 0, 1)
                        
                        MDLabel:
                            size_hint_x: None
                            text: "00:00"
                            id: Music_time
                            width: dp(35)
                            
                    
                    MDGridLayout:
                        cols: 5
                        rows: 1
                        spacing: dp(grid.width/20)
                        
                        MDIconButton:
                            icon: "heart-plus"
                            on_release: app.add_favite()
                            # on_release: app.add_favite()
                            
                        MDIconButton:
                            icon: "skip-backward"
                            on_release: app.skip_back()
                       
                        
                        MDIconButton:
                            icon: "repeat"
                            id: repeat
                            on_release: app.repeat()
                        
                        MDIconButton:
                            icon: "skip-forward"
                            on_release: app.skip_forward()
                        
                        MDIconButton:
                            icon: "shuffle-disabled"
                            id: shuffle
                            on_release: app.play_random()
                            
                    OneLineListItem:
                        id: music_name
                        #on_release: app.ui_press()
                        
                    MDGridLayout:
                        rows: 1
                        cols: 3
                        
                        spacing: (grid.width -180) /3
                        
                        MDFloatingActionButton:
                            icon: "skip-previous"
                            elevation: dp(10)
                            on_release: app.Previous()
                            canvas.before:
					            Color:
					                rgba: root.md_bg_color
					                rgba: 1, 1, 1, 1
					            Ellipse:
					                pos: self.x - dp(10/2), self.y - dp(10/2)
					                size: self.width + dp(10), self.height + dp(10)
                        
                        MDFloatingActionButton:
                            icon: "play"
                            id: play
                            elevation: dp(10)
                            on_release: app.Play()
                            canvas.before:
					            Color:
					                rgba: root.md_bg_color
					                rgba: 1, 1, 1, 1
					            Ellipse:
					                pos: self.x - dp(10/2), self.y - dp(10/2)
					                size: self.width + dp(10), self.height + dp(10)
                        
                        MDFloatingActionButton:
                            icon: "skip-next"
                            elevation: dp(10)
                            on_release: app.Next()
                            canvas.before:
					            Color:
					                rgba: root.md_bg_color
					                rgba: 1, 1, 1, 1
					            Ellipse:
					                pos: self.x - dp(10/2), self.y - dp(10/2)
					                size: self.width + dp(10), self.height + dp(10)
                    
                
                Widget:
                    size_hint_y: None
                    height: dp(50)
                    
                    MDFloatingActionButton:
                        icon: "chevron-left"
                        elevation: dp(10)
                        x:  self.width/2
				        y: tool.height - (self.height*1.5)
                        on_release: app.UI_BACK()
                        canvas.before:
                        	Color:
                        		rgba: root.md_bg_color
                        		rgba: 1, 1, 1, 1
							Ellipse:
								pos: self.x - dp(10/2), self.y - dp(10/2)
								size: self.width + dp(10), self.height + dp(10)
   
#############################################
############# Settings Screen ##############                 

        SettingsScreen:
            name: "setting"
            EffectWidget:
                effects: [ew.VerticalBlurEffect(size=10), ew.HorizontalBlurEffect(size=10)]
                
                #FitImage:
                    #source: "FB_IMG_1580579556493.jpg"
                
            MDBoxLayout:
                orientation: "vertical"
                
                MDToolbar:
                    id: toolbars
                    title: "Settings"
                    md_bg_color: (1, .5, 0, 1)
                    
                Label:
                    size_hint_y: None
                    height: dp(30)
                OneLineIconListItem:
                    text: "Change Theme"
                    on_release: app.Theme_Change()
                    IconLeftWidget:
                        icon: "theme-light-dark"
                    
                
                
                Label:
                    
                
                Widget:
                    size_hint_y: None
                    height: dp(50)
                    
                    MDFloatingActionButton:
				        id: float_btn
				        icon: "home"
				        x: toolbars.center_x - self.width/2
				        y: toolbars.y - self.height/2
				        md_bg_color: (1, .5, 0, 1)
				        on_release: root.ids.my_manager.current = "home screen"
				        canvas.before:
				            Color:
				                rgba: root.md_bg_color
				                rgba: 1, 1, 1, 1
				            Ellipse:
				                pos: self.x - dp(10/2), self.y - dp(10/2)
				                size: self.width + dp(10), self.height + dp(10)
                
                
                               
 
##########################################################
###################### navigation menu ####################            
    MDNavigationDrawer:
        id: nav_drawer    
        
        MDBoxLayout:
            orientation: "vertical"
            padding: dp(5)
            
            MDToolbar:
                title: "Menu"
                #md_bg_color: (1, .5, 0, 1)
            
            ScrollView:
                MDList:
                    size_hint_y: None
                    height: dp(400)
                    
                    OneLineIconListItem:
                        text: "Home"
                        on_release: root.ids.my_manager.current = "home screen"
                        IconLeftWidget:
                            icon: "home"
                            
                    OneLineIconListItem:
                        text: "Music"
                        on_release: root.ids.my_manager.current = "music screen"
                        IconLeftWidget:
                            icon: "music"
                    
                    OneLineIconListItem:
                        text: " Stream Music"
                        on_release: root.ids.my_manager.current = "stream"
                        IconLeftWidget:
                            icon: "shopping-music"
                            
                    OneLineIconListItem:
                        text: "Recently Played"
                        on_release: root.ids.my_manager.current = "recent screen"
                        on_press: app.add_recent()
                        IconLeftWidget:
                            icon: "music-box"
                    
                    OneLineIconListItem:
                        text: "Playlist"
                        on_release: root.ids.my_manager.current = "playlist screen"
                        IconLeftWidget:
                            icon: "playlist-music"
                    
                    OneLineIconListItem:
                        text: "Favourites"
                        on_release: root.ids.my_manager.current = "favourite screen"
                        IconLeftWidget:
                            icon: "heart-multiple"
                            
                    OneLineIconListItem:
                        text: "Music Folders"
                        on_release: root.ids.my_manager.current = "folders"
                        IconLeftWidget:
                            icon: "folder-music"
                    
                    OneLineIconListItem:
                        text: "Artists"
                        on_release: root.ids.my_manager.current = "artist"
                        IconLeftWidget:
                            icon: "account-music"
                        
            Label:
                size_hint: 1, .3
            
            OneLineIconListItem:
                text: "More"
                on_release: root.ids.my_manager.current = "setting"
                IconLeftWidget:
                    icon: "headphones-settings"
            
            Label:
                size_hint_y: None
                height: dp(10)


        


"""

##################################################################
###################################################################
################# music loop code #################################

path = "//storage//emulated//0"
path1 = "Root path"
Music = []
Music1 = []
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".mp3") or file.endswith(".m4a"):
            Music.append(os.path.join(root, file))
            Music1.append(file)

music_dir = [path]
music_dir1 = [path1]
for root, dirs, files in os.walk(path):
    for dir in dirs:
        x = os.path.join(root, dir)
        y = dir
        for v in os.listdir(x):
            if v.endswith(".mp3") or v.endswith(".m4a"):
                if x in music_dir:
                    pass
                else:
                    music_dir.append(x)
                    music_dir1.append(y)


##################################################################
##################################################################
########## Screens ###############################################
class IntroScreen(Screen):
    pass


class HomeScreen(Screen):
    pass


class MusicScreen(Screen):
    pass


class StreamMusic(Screen):
    pass


class MusicFolders(Screen):
    pass


class MusicFoldersDisplay(Screen):
    pass


class ClassArtist(Screen):
    pass


class RecentlyScreen(Screen):
    pass


class FavouriteScreen(Screen):
    pass


class PlaylistScreen(Screen):
    pass


class MusicUi(Screen):
    pass


class SettingsScreen(Screen):
    pass


#########################################################
########################################################
################ My swiper Item Button class ##########
class MyButton(FitImage, MDFlatButton):
    pass


#################################################################
#################################################################
############### Custom Left Icon and right icon classes #########

class CustomRecycleView(RecycleView):
    pass


class PlayListRecycleView(RecycleView):
    pass



class TestLayout(MDGridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3
        #self.orientation = "vertical"

        Clock.schedule_once(self.loop, 1)

    def loop(self, dt):
        app = MDApp.get_running_app()
        for i in app.playlist_list:
            button = MDFlatButton(text=f"{i}")
            self.add_widget(button)

class CustomIconButton(MDIconButton, MDTooltip):
    pass





class CustomIconItem(OneLineAvatarIconListItem):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        Pop_list = ["Delete", "Add Playlist", "Play Next", "Music Info"]
        Pop_list.reverse()

        iteml = IconLeftWidget(icon="music")

        itemr = IconRightWidget(icon="dots-vertical", on_release=self.open_menu)

        self.add_widget(itemr)
        self.add_widget(iteml)
        self.venus = []

    def open_menu(self, btn):
        d = {"text": self.text}
        fav_button = CustomIconButton(icon="heart-plus",
                                      tooltip_text="add to favourites",
                                      on_press=self.favourite)

        playlist_button = CustomIconButton(icon="playlist-plus",
                                           tooltip_text="add to playlist",
                                           on_press=self.Playlist)
        close_button = MDFlatButton(text="close", on_release=self.close_main_menu)
        self.dialog = MDDialog(title=self.text, size_hint=(0.7, .3),
                               buttons=[fav_button, playlist_button, close_button ])
        self.dialog.open()

    def close_main_menu(self, txt):
        self.dialog.dismiss()


    def Playlist(self, txt):
        self.textinput = MDTextField(hint_text="create playlist")
        self.dialog1 = MDDialog(
            size_hint=(0.7, .5),
            type="custom",
            content_cls=self.textinput,
            buttons=[
                MDFlatButton(text="create playlist", on_release=self.create_playlist),
                MDFlatButton(text="back", on_release=self.back)
            ])
        self.dialog1.open()

    def back(self, txt):
        self.dialog1.dismiss()
        self.dialog.dismiss()

        self.dialog2 = MDDialog(
            size_hint=(0.7, None),height=dp(400),

            type="custom",
            content_cls=TestLayout(),
            buttons=[MDFlatButton(text="close",
                                  on_release=self.dialog2_dismiss)]

        )

        self.dialog2.open()
        pass

    def dialog2_dismiss(self, txt):
        self.dialog2.dismiss()

    def create_playlist(self, txt):
        app = MDApp.get_running_app()

        if self.textinput.text == "":
            pass
        else:
            app.playlist_list.append(self.textinput.text)


        data = [{"text": str(app.playlist_list[i]), "size_hint_x": 1}
                for i in range(len(app.playlist_list))]

        app.root.ids.rp.data = data

    def favourite(self, txt):
        app = MDApp.get_running_app()
        app.fav1.append(self.text)
        text = app.root.ids.music_name.text

        if text in app.fav:
            pass
        else:
            app.fav.insert(0, self.text)
            app.fav1.insert(0, self.text)

        data = [{"text": str(app.fav1[i]), "size_hint_x": 1,
                 "on_release": lambda x=i: app.play_fav(app.fav1[x])}
                for i in range(len(app.fav))]

        app.root.ids.rf.data = data


class SearchedIconItem(OneLineAvatarIconListItem):
    def open_menu(self):
        self.menu.open()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Pop_list = ["Delete", "Add Playlist", "Play Next", "Music Info"]
        Pop_list.reverse()

        iteml = IconLeftWidget(icon="music")

        itemr = IconRightWidget(icon="dots-vertical")

        menu_items = [{"text": f"{Pop_list[i]}",
                       "viewclass": "OneLineListItem"} for i in range(4)]

        self.menu = MDDropdownMenu(
            caller=itemr,
            items=menu_items,
            width_mult=2)

        itemr.on_release = self.open_menu
        self.add_widget(itemr)
        self.add_widget(iteml)


class FavouriteIconItem(OneLineAvatarIconListItem):
    def open_menu(self):
        self.menu.open()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        Pop_list = ["Remove Favourite", "Add Playlist", "Play Next", "Music Info"]
        Pop_list.reverse()

        iteml = IconLeftWidget(icon="music")

        itemr = IconRightWidget(icon="dots-vertical")

        menu_items = [{"text": f"{Pop_list[i]}",
                       "viewclass": "OneLineListItem"} for i in range(len(Pop_list))]

        self.menu = MDDropdownMenu(
            caller=itemr,
            items=menu_items,
            width_mult=2)

        itemr.on_release = self.open_menu
        self.add_widget(itemr)
        self.add_widget(iteml)


class MusicDirectoryItem(OneLineAvatarIconListItem):
    def open_menu(self):
        self.menu.open()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        Pop_list = ["Make Playlist"]
        Pop_list.reverse()

        iteml = IconLeftWidget(icon="folder-music")

        itemr = IconRightWidget(icon="dots-vertical")

        menu_items = [{"text": f"{Pop_list[i]}",
                       "viewclass": "OneLineListItem"} for i in range(len(Pop_list))]

        self.menu = MDDropdownMenu(
            caller=itemr,
            items=menu_items,
            width_mult=2)

        itemr.on_release = self.open_menu
        self.add_widget(itemr)
        self.add_widget(iteml)


class RecentItem(OneLineAvatarIconListItem):
    def open_menu(self):
        self.menu.open()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Pop_list = ["Remove", "Add Playlist", "Play Next", "Music Info"]
        Pop_list.reverse()

        iteml = IconLeftWidget(icon="music")

        itemr = IconRightWidget(icon="dots-vertical")

        menu_items = [{"text": f"{Pop_list[i]}",
                       "viewclass": "OneLineListItem"} for i in range(len(Pop_list))]

        self.menu = MDDropdownMenu(
            caller=itemr,
            items=menu_items,
            width_mult=2)

        itemr.on_release = self.open_menu
        self.add_widget(itemr)
        self.add_widget(iteml)


class PlayMusicDirectory(OneLineAvatarIconListItem):
    def open_menu(self):
        self.menu.open()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Pop_list = ["Add Playlist", "Play Next", "Music Info"]
        Pop_list.reverse()

        iteml = IconLeftWidget(icon="music")

        itemr = IconRightWidget(icon="dots-vertical")

        menu_items = [{"text": f"{Pop_list[i]}",
                       "viewclass": "OneLineListItem"} for i in range(len(Pop_list))]

        self.menu = MDDropdownMenu(
            caller=itemr,
            items=menu_items,
            width_mult=2)

        itemr.on_release = self.open_menu
        self.add_widget(itemr)
        self.add_widget(iteml)


#############################################
#############################################
################ Screen Manager Class ########
class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.transition = NoTransition
        Clock.schedule_once(self.Change, 5)

    def Change(self, dt):
        self.current = "home screen"


##############################################################
#############################################################
###############   Running App Class #########################
class TinselPlayer(MDApp):
    try:

        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.Music1 = Music1
            self.Music = Music

            self.Minimum = 0
            self.Maximum = 100
            self.Slider = 0

            self.Mini = 0
            self.Maxi = 100
            self.Val = 0

            self.neg = -1
            self.nex = 1

            #
            self.player = Player()

            self.SCREEN_LIST = []

            self.x = 0

            self.vine = ""

            self.fav = []
            self.fav1 = []

            self.rec = []
            self.rec1 = []

            self.playlist_list = []

        def build(self):
            #self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette = "Orange"
            self.builder = Builder.load_string(Code)
            return self.builder

        def on_start(self):
            data = [{"text": str(Music1[i]), "size_hint_x": 1,
                     "on_release": lambda x=i: self.play_music(Music[x], Music1[x]),
                     } for i in range(len(Music))]
            self.root.ids.rv.data = data

            dataff = [{"text": str(music_dir1[i]), "size_hint_x": 1,
                       "on_release": lambda x=i: self.open_folder(music_dir1[x], music_dir[x])
                       } for i in range(len(music_dir))]
            self.root.ids.rff.data = dataff

        def UI_BACK(self):
            self.root.ids.my_manager.current = self.SCREEN_LIST[-1]

        ####################################################################
        ####################################################################
        ################# Open Music folder and play music #################
        def open_folder(self, dirn, dirp):
            self.root.ids.my_manager.current = "folder music"
            self.root.ids.my_manager.transition.direction = "left"
            self.root.ids.folder_music.title = f"{dirn}"

            path = dirp

            fp = []
            fn = []
            for root, dirs, files in os.walk(path):
                for file in files:
                    if file.endswith(".mp3") or file.endswith(".m4a"):
                        fp.append(os.path.join(root, file))
                        fn.append(file)

            data = [{"text": str(fn[i]), "size_hint_x": 1,
                     "on_release": lambda x=i: self.play_music_path(fp[x], fn[x])
                     } for i in range(len(fp))]
            self.root.ids.content_music.data = data

        def play_music_path(self, text, text1):
            if text in self.rec:
                pass
            else:

                self.rec.insert(0, text)
                self.rec1.insert(0, text1)

            self.path_name = text
            self.music_name = text1
            try:
                self.player.play(text)
                pass
            except:
                pass

            int_time = self.player.get_duration()
            int_time_sec = int_time / 1000
            int_time_min = int(int_time_sec // 60)
            int_time_s = int(int_time_sec % 60)

            formattex = f"{int_time_min}:{int_time_s}"
            self.root.ids.Music_time.text = str(formattex)

            self.root.ids.music_name.text = str(self.music_name)
            self.root.ids.music_nameh.text = str(self.music_name)
            self.root.ids.music_namem.text = str(self.music_name)
            self.root.ids.music_namer.text = str(self.music_name)
            self.root.ids.music_namep.text = str(self.music_name)
            self.root.ids.music_namef.text = str(self.music_name)
            self.root.ids.sub_dir_item1.text = str(self.music_name)
            self.root.ids.sub_dir_item2.text = str(self.music_name)
            self.root.ids.play.icon = "pause"
            self.root.ids.play1.icon = "pause"
            self.root.ids.play2.icon = "pause"
            self.root.ids.play3.icon = "pause"
            self.root.ids.play4.icon = "pause"
            self.root.ids.play5.icon = "pause"
            self.root.ids.play_dir1.icon = "pause"
            self.root.ids.play_dir2.icon = "pause"

            Clock.schedule_interval(self.reload, 1)

        ####################################################################
        ####################################################################
        ################# Go back music directory list ###############################
        def Folder_Back(self):
            self.root.ids.my_manager.current = "folders"
            self.root.ids.my_manager.transition.direction = "right"

        #################################################################
        #################################################################
        #################################################################
        #######  Clock Interval Loop for time eternal ###################

        def reload(self, dt):
            self.root.ids.jack.max = int(self.player.get_duration() / 1000)
            # self.root.ids.jack1.max = int(self.player.get_duration() / 1000)
            # self.root.ids.jack2.max = int(self.player.get_duration() / 1000)
            # self.root.ids.jack3.max = int(self.player.get_duration() / 1000)
            # self.root.ids.jack4.max = int(self.player.get_duration() / 1000)
            # self.root.ids.jack5.max = int(self.player.get_duration() / 1000)

            self.root.ids.jack.value = int(self.player.current_position() / 1000)
            # self.root.ids.jack1.value = int(self.player.current_position() / 1000)
            # self.root.ids.jack2.value = int(self.player.current_position() / 1000)
            # self.root.ids.jack3.value = int(self.player.current_position() / 1000)
            # self.root.ids.jack4.value = int(self.player.current_position() / 1000)
            # self.root.ids.jack5.value = int(self.player.current_position() / 1000)

            if int(self.root.ids.jack.value) > int(self.player.current_position() / 1000) + 1:
                self.player.seek(self.root.ids.jack.value)

            elif int(self.root.ids.jack.value) < int(self.player.current_position() / 1000) - 1:
                self.player.seek(self.root.ids.jack.value)

            numx = self.Music1.index(self.root.ids.music_name.text) + 1
            if self.root.ids.repeat.icon == "repeat-once":
                self.player.do_loop(True)

            elif ((self.player.is_playing() == False) and (
                    self.root.ids.repeat.icon == "repeat")) and self.root.ids.play.icon == "pause":

                try:
                    self.player.play(Music[numx])
                except:
                    pass

                self.root.ids.music_name.text = str(Music1[numx])
                self.root.ids.music_nameh.text = str(Music1[numx])
                self.root.ids.music_namem.text = str(Music1[numx])
                self.root.ids.music_namer.text = str(Music1[numx])
                self.root.ids.music_namep.text = str(Music1[numx])
                self.root.ids.music_namef.text = str(Music1[numx])
                self.root.ids.sub_dir_item1.text = str(Music1[numx])
                self.root.ids.sub_dir_item2.text = str(Music1[numx])
                int_time = self.player.get_duration()
                int_time_sec = int_time / 1000
                int_time_min = int(int_time_sec // 60)
                int_time_s = int(int_time_sec % 60)
                formattex = f"{int_time_min}:{int_time_s}"
                self.root.ids.Music_time.text = str(formattex)

            int_time_sec = int(self.player.current_position()) / 1000
            int_time_min = int(int_time_sec // 60)
            int_time_s = int(int_time_sec % 60)
            self.root.ids.Music_ctime.text = f"{int_time_min}:{int_time_s}"

        #################################################################
        #################################################################
        #################################################################
        #######  My Music Search Engine #################################

        def play_search(self, text, text1):

            if text in self.rec:
                pass
            else:
                self.rec.insert(0, text)
                self.rec1.insert(0, text1)

            self.path_name = text
            try:
                self.player.play(text)
            except:
                pass
            self.root.ids.music_name.text = str(text1)
            self.root.ids.music_nameh.text = str(text1)
            self.root.ids.music_namem.text = str(text1)
            self.root.ids.music_namer.text = str(text1)
            self.root.ids.music_namep.text = str(text1)
            self.root.ids.music_namef.text = str(text1)
            self.root.ids.sub_dir_item1.text = str(text1)
            self.root.ids.sub_dir_item2.text = str(text1)

            self.root.ids.play.icon = "pause"
            self.root.ids.play1.icon = "pause"
            self.root.ids.play2.icon = "pause"
            self.root.ids.play3.icon = "pause"
            self.root.ids.play4.icon = "pause"
            self.root.ids.play5.icon = "pause"
            self.root.ids.play_dir1.icon = "pause"
            self.root.ids.play_dir2.icon = "pause"

            int_time = self.player.get_duration()
            int_time_sec = int_time / 1000
            int_time_min = int(int_time_sec // 60)
            int_time_s = int(int_time_sec % 60)

            formattex = f"{int_time_min}:{int_time_s}"
            self.root.ids.Music_time.text = str(formattex)

            Clock.schedule_interval(self.reload, 1)

        def Music_Search(self):
            prior = self.root.ids.TSearch.text.lower()
            self.SM = []
            self.SM1 = []

            for x in range(len(Music)):
                y = Music[x]
                y1 = y.lower()
                if prior in y1:
                    self.SM.append(y)
                    numx = self.Music.index(y)
                    self.SM1.append(Music1[numx])

                data = [{"text": str(self.SM1[i]), "size_hint_x": 1,
                         "on_release": lambda x=i: self.play_search(self.SM[x], self.SM1[x])} for i in
                        range(len(self.SM))]

                self.root.ids.sf.data = data

        #################################################################
        #################################################################
        #################################################################
        #######  Add and play recent pkayed music #######################

        def play_recent(self, text, text1):

            self.path_name = text
            try:
                self.player.play(text)
            except:
                pass
            self.root.ids.music_name.text = str(text1)
            self.root.ids.music_nameh.text = str(text1)
            self.root.ids.music_namem.text = str(text1)
            self.root.ids.music_namer.text = str(text1)
            self.root.ids.music_namep.text = str(text1)
            self.root.ids.music_namef.text = str(text1)
            self.root.ids.sub_dir_item1.text = str(text1)
            self.root.ids.sub_dir_item2.text = str(text1)

            self.root.ids.play.icon = "pause"
            self.root.ids.play1.icon = "pause"
            self.root.ids.play2.icon = "pause"
            self.root.ids.play3.icon = "pause"
            self.root.ids.play4.icon = "pause"
            self.root.ids.play5.icon = "pause"
            self.root.ids.play_dir1.icon = "pause"
            self.root.ids.play_dir2.icon = "pause"

            int_time = self.player.get_duration()
            int_time_sec = int_time / 1000
            int_time_min = int(int_time_sec // 60)
            int_time_s = int(int_time_sec % 60)

            formattex = f"{int_time_min}:{int_time_s}"
            self.root.ids.Music_time.text = str(formattex)

            Clock.schedule_interval(self.reload, 1)

        def add_recent(self):
            data = [{"text": str(self.rec1[i]), "size_hint_x": 1,
                     "on_release": lambda x=i: self.play_recent(self.rec[x], self.rec1[x])} for i in
                    range(len(self.rec))]

            self.root.ids.rr.data = data

        #################################################################
        #################################################################
        #################################################################
        #######  Ui Screen None Active Button ###########################

        def ui_press(self):
            pass

        #################################################################
        #################################################################
        #################################################################
        #######  Delete and clear search textinput and recycleview ######
        def Delete_Search(self):
            self.root.ids.sf.data.clear()
            self.root.ids.sf.refresh_from_data()

        #################################################################
        #################################################################
        #################################################################
        #######  Open My Music search Page   ############################
        def open(self):
            self.root.ids.sf.data.clear()

            self.root.ids.sf.refresh_from_data()
            self.root.ids.rf.refresh_from_data()

            self.root.ids.back.open()

        #################################################################
        #################################################################
        #################################################################
        #######  My Music Play Music Engine      ########################
        def play_music(self, text, text1):
            if text in self.rec:
                pass
            else:

                self.rec.insert(0, text)
                self.rec1.insert(0, text1)

            self.path_name = text
            self.music_name = text1
            try:
                self.player.play(text)
            except:
                pass

            int_time = self.player.get_duration()
            int_time_sec = int_time / 1000
            int_time_min = int(int_time_sec // 60)
            int_time_s = int(int_time_sec % 60)

            formattex = f"{int_time_min}:{int_time_s}"
            self.root.ids.Music_time.text = str(formattex)

            self.root.ids.music_name.text = str(self.music_name)
            self.root.ids.music_nameh.text = str(self.music_name)
            self.root.ids.music_namem.text = str(self.music_name)
            self.root.ids.music_namer.text = str(self.music_name)
            self.root.ids.music_namep.text = str(self.music_name)
            self.root.ids.music_namef.text = str(self.music_name)
            self.root.ids.sub_dir_item1.text = str(self.music_name)
            self.root.ids.sub_dir_item2.text = str(self.music_name)

            self.root.ids.play.icon = "pause"
            self.root.ids.play1.icon = "pause"
            self.root.ids.play2.icon = "pause"
            self.root.ids.play3.icon = "pause"
            self.root.ids.play4.icon = "pause"
            self.root.ids.play5.icon = "pause"
            self.root.ids.play_dir1.icon = "pause"
            self.root.ids.play_dir2.icon = "pause"

            Clock.schedule_interval(self.reload, 1)

        #################################################################
        #################################################################
        #################################################################
        #######  Chnage theme           #################################
        def Theme_Change(self):

            if self.theme_cls.theme_style == "Dark":
                self.theme_cls.theme_style = "Light"

            elif self.theme_cls.theme_style == "Light":
                self.theme_cls.theme_style = "Dark"
            # theme = MDThemePicker()
            # theme.open()

        #################################################################
        #################################################################
        #################################################################
        #######  Add favourite to screen and play       #################
        def add_favite(self):
            text = self.root.ids.music_name.text

            if text in self.fav:
                pass
            else:
                self.fav.insert(0, self.root.ids.music_name.text)
                self.fav1.insert(0, self.root.ids.music_name.text)

            data = [{"text": str(self.fav1[i]), "size_hint_x": 1,
                     "on_release": lambda x=i: self.play_fav(self.fav1[x])} for i in range(len(self.fav))]

            self.root.ids.rf.data = data

        def play_fav(self, f2):

            favi = Music1.index(f2)
            fav = Music[favi]
            self.player.play(fav)
            self.path_name = fav
            self.root.ids.music_name.text = str(f2)
            self.root.ids.music_nameh.text = str(f2)
            self.root.ids.music_namem.text = str(f2)
            self.root.ids.music_namer.text = str(f2)
            self.root.ids.music_namep.text = str(f2)
            self.root.ids.music_namef.text = str(f2)
            self.root.ids.sub_dir_item1.text = str(f2)
            self.root.ids.sub_dir_item2.text = str(f2)

            int_time = self.player.get_duration()
            int_time_sec = int_time / 1000
            int_time_min = int(int_time_sec // 60)
            int_time_s = int(int_time_sec % 60)

            formattex = f"{int_time_min}:{int_time_s}"
            self.root.ids.Music_time.text = str(formattex)

            Clock.schedule_interval(self.reload, 1)

        #################################################################
        #################################################################
        #################################################################
        #######  Send currently playing song a sceond ahead     #########
        def skip_back(self):
            cp = self.player.current_position()

            int_time = self.player.get_duration()

            int_time_sec = int_time / 1000
            self.root.ids.jack.max = int_time_sec

            int_time_sec = int_time / 1000
            int_time_min = int(int_time_sec // 60)
            int_time_s = int(int_time_sec % 60)

            form = [int_time_min, int_time_s]

            Sec = cp / 1000
            self.root.ids.jack.value = int(Sec)

            final = Sec + self.neg

            self.player.seek(final)
            final_min = int(final // 60)
            final_sec = int(final % 60)

            if (int(final_min)) >= form[0] or (int(final_sec)) >= form[1]:
                final_min = "00"
                final_sec = "00"
                final = f"{final_min}:{final_sec}"

            else:
                final = f"{final_min}:{final_sec}"

            self.root.ids.Music_ctime.text = str(final)

        #################################################################
        #################################################################
        #################################################################
        #######  Send Cutrently playing song a second back in time  #####
        def skip_forward(self):
            cp = self.player.current_position()
            int_time = int(self.player.get_duration() / 1000)

            self.root.ids.jack.max = int_time
            Sec = int(cp / 1000)
            self.root.ids.jack.value = int(Sec)

            final = Sec + 1

            self.player.seek(final)
            final_min = int(final // 60)
            final_sec = int(final % 60)

            if (int(final_min)) < 0 or (int(final_sec)) < 0:
                final_min = "00"
                final_sec = "00"
                final = f"{final_min}:{final_sec}"

            else:
                final = f"{final_min}:{final_sec}"

            self.root.ids.Music_ctime.text = str(final)

        #################################################################
        #################################################################
        #################################################################
        #######  Play previous song before current ######################
        def Previous(self):
            self.root.ids.Music_ctime.text = "0:0"
            numy = random.randint(0, len(Music))
            self.x -= 1
            numx = self.Music1.index(self.root.ids.music_name.text) - 1
            num = numx
            self.root.ids.jack.value = int(self.player.current_position() / 1000)

            if self.root.ids.shuffle.icon == "shuffle-disabled":
                if num >= 0:

                    try:
                        self.player.play(Music[numx])
                    except:
                        pass
                    self.root.ids.music_name.text = str(Music1[num])
                    self.root.ids.music_nameh.text = str(Music1[num])
                    self.root.ids.music_namem.text = str(Music1[num])
                    self.root.ids.music_namer.text = str(Music1[num])
                    self.root.ids.music_namep.text = str(Music1[num])
                    self.root.ids.music_namef.text = str(Music1[num])
                    self.root.ids.sub_dir_item1.text = str(Music1[num])
                    self.root.ids.sub_dir_item2.text = str(Music1[num])

                    int_time = self.player.get_duration()
                    int_time_sec = int_time / 1000
                    int_time_min = int(int_time_sec // 60)
                    int_time_s = int(int_time_sec % 60)
                    formattex = f"{int_time_min}:{int_time_s}"
                    self.root.ids.Music_time.text = str(formattex)

            elif self.root.ids.shuffle.icon == "shuffle-variant":
                try:
                    self.player.play(Music[numy])
                except:
                    pass
                self.root.ids.music_name.text = str(Music1[numy])
                self.root.ids.sub_dir_item1.text = str(Music1[num])
                self.root.ids.sub_dir_item2.text = str(Music1[num])
                self.root.ids.music_nameh.text = str(Music1[numy])
                self.root.ids.music_namem.text = str(Music1[numy])
                self.root.ids.music_namer.text = str(Music1[numy])
                self.root.ids.music_namep.text = str(Music1[numy])
                self.root.ids.music_namef.text = str(Music1[numy])

        #################################################################
        #################################################################
        #################################################################
        #######  Pause or Play Current playing music ####################
        def Play(self):
            if self.root.ids.play.icon == "play":
                self.player.resume()
                self.root.ids.play.icon = "pause"
                self.root.ids.play1.icon = "pause"
                self.root.ids.play2.icon = "pause"
                self.root.ids.play3.icon = "pause"
                self.root.ids.play4.icon = "pause"
                self.root.ids.play5.icon = "pause"
                self.root.ids.play_dir1.icon = "pause"
                self.root.ids.play_dir2.icon = "pause"

            elif self.root.ids.play.icon == "pause":
                self.player.pause()
                self.root.ids.play.icon = "play"
                self.root.ids.play1.icon = "play"
                self.root.ids.play2.icon = "play"
                self.root.ids.play3.icon = "play"
                self.root.ids.play4.icon = "play"
                self.root.ids.play5.icon = "play"
                self.root.ids.play_dir1.icon = "play"
                self.root.ids.play_dir2.icon = "play"

        def dirin_play(self):
            if self.root.ids.play_dir2.icon == "play":
                self.player.resume()
                self.root.ids.play.icon = "pause"
                self.root.ids.play1.icon = "pause"
                self.root.ids.play2.icon = "pause"
                self.root.ids.play3.icon = "pause"
                self.root.ids.play4.icon = "pause"
                self.root.ids.play5.icon = "pause"
                self.root.ids.play_dir1.icon = "pause"
                self.root.ids.play_dir2.icon = "pause"

            elif self.root.ids.play_dir2.icon == "pause":
                self.player.pause()
                self.root.ids.play.icon = "play"
                self.root.ids.play1.icon = "play"
                self.root.ids.play2.icon = "play"
                self.root.ids.play3.icon = "play"
                self.root.ids.play4.icon = "play"
                self.root.ids.play5.icon = "play"
                self.root.ids.play_dir1.icon = "play"
                self.root.ids.play_dir2.icon = "play"

        def dirout_play(self):
            if self.root.ids.play_dir1.icon == "play":
                self.player.resume()
                self.root.ids.play.icon = "pause"
                self.root.ids.play1.icon = "pause"
                self.root.ids.play2.icon = "pause"
                self.root.ids.play3.icon = "pause"
                self.root.ids.play4.icon = "pause"
                self.root.ids.play5.icon = "pause"
                self.root.ids.play_dir1.icon = "pause"
                self.root.ids.play_dir2.icon = "pause"

            elif self.root.ids.play_dir1.icon == "pause":
                self.player.pause()
                self.root.ids.play.icon = "play"
                self.root.ids.play1.icon = "play"
                self.root.ids.play2.icon = "play"
                self.root.ids.play3.icon = "play"
                self.root.ids.play4.icon = "play"
                self.root.ids.play5.icon = "play"
                self.root.ids.play_dir1.icon = "play"
                self.root.ids.play_dir2.icon = "play"

        #################################################################
        #################################################################
        #################################################################
        #######  Play Next song after currently playing song  ###########
        def Next(self):
            self.root.ids.Music_ctime.text = "0:0"
            numy = random.randint(0, len(Music))
            self.x += 1
            numx = self.Music1.index(self.root.ids.music_name.text) + 1
            num = numx
            self.root.ids.jack.value = self.player.current_position() / 1000
            if self.root.ids.shuffle.icon == "shuffle-disabled":
                if num <= (len(Music) - 1):
                    # player= Player()
                    try:
                        self.player.play(Music[numx])
                    except:
                        pass

                    self.root.ids.music_name.text = str(Music1[num])
                    self.root.ids.sub_dir_item1.text = str(Music1[num])
                    self.root.ids.sub_dir_item2.text = str(Music1[num])
                    self.root.ids.music_nameh.text = str(Music1[num])
                    self.root.ids.music_namem.text = str(Music1[num])
                    self.root.ids.music_namer.text = str(Music1[num])
                    self.root.ids.music_namep.text = str(Music1[num])
                    self.root.ids.music_namef.text = str(Music1[num])
                    int_time = self.player.get_duration()
                    int_time_sec = int_time / 1000
                    int_time_min = int(int_time_sec // 60)
                    int_time_s = int(int_time_sec % 60)
                    formattex = f"{int_time_min}:{int_time_s}"
                    self.root.ids.Music_time.text = str(formattex)

            elif self.root.ids.shuffle.icon == "shuffle-variant":
                try:
                    self.player.play(Music[numy])
                except:
                    pass
                self.root.ids.music_name.text = str(Music1[numy])
                self.root.ids.sub_dir_item1.text = str(Music1[num])
                self.root.ids.sub_dir_item2.text = str(Music1[num])
                self.root.ids.music_nameh.text = str(Music1[numy])
                self.root.ids.music_namem.text = str(Music1[numy])
                self.root.ids.music_namer.text = str(Music1[numy])
                self.root.ids.music_namep.text = str(Music1[numy])
                self.root.ids.music_namef.text = str(Music1[numy])

        #################################################################
        #################################################################
        #################################################################
        #######  Repeat song #################################
        def repeat(self):
            if self.root.ids.repeat.icon == "repeat":
                self.root.ids.repeat.icon = "repeat-once"
                self.player.do_loop(True)
            elif self.root.ids.repeat.icon == "repeat-once":
                self.root.ids.repeat.icon = "repeat"
                self.player.do_loop(False)

        def play_random(self):
            if self.root.ids.shuffle.icon == "shuffle-variant":
                self.root.ids.shuffle.icon = "shuffle-disabled"

            elif self.root.ids.shuffle.icon == "shuffle-disabled":
                self.root.ids.shuffle.icon = "shuffle-variant"

    except:
        pass


TinselPlayer().run()

import random

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import Clock
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition, WipeTransition
from kivymd.app import MDApp
from kivymd.uix.list import OneLineAvatarIconListItem, IconLeftWidget, IconRightWidget
from kivymd.uix.picker import MDThemePicker
import os
from kvdroid.tools.audio import Player
#import stagger




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
                text: "Short \\n never felt \\n taller \\n until now "
                font_size: dp(35)
                color: (0, 0, 1, 1)
                halign: "center"
                bold: True
                font_name: "VINERITC.TTF"



######################################
########### Home Screen #############
                
        HomeScreen:
            name: "home screen"
            EffectWidget:
                effects: [ew.VerticalBlurEffect(size=10), ew.HorizontalBlurEffect(size=10)]
                
                FitImage:
                    source: "FB_IMG_1580579556493.jpg"
                
            MDBoxLayout:
                orientation: "vertical"
                id: grid
                MDToolbar:
                    title: "Tinsel Player"
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("toggle")]]
                
                MDGridLayout:
                    rows: 2
                    cols: 2
                    size_hint: .6, .8
                    pos_hint: {"center_x":.5}
                    padding: dp(10)
                    
                    MDFlatButton:
                        text: "Music"
                        
                        size_hint: 1, 1
                        on_release: root.ids.my_manager.current = "music screen"
                    
                    MDFlatButton:
                        text: "Recently Played"
                        
                        size_hint: 1, 1
                        on_release: root.ids.my_manager.current = "recent screen"
                    
                    MDFlatButton:
                        text: "Playlist"
                        
                        size_hint: 1, 1
                        on_release: root.ids.my_manager.current = "playlist screen"
                    
                    MDFlatButton:
                        text: "Favourites"
                        
                        size_hint: 1, 1
                        on_release: root.ids.my_manager.current = "favourite screen"
                        
                    
                MDGridLayout:
                    size_hint_y: None
                    height: dp(120)
                    rows: 2
                    cols: 1
                    spacing: dp(10)
                    padding: dp(10)
                    
                    OneLineAvatarIconListItem:
                        #text: "Play Music"
                        id: music_nameh
                        on_release: root.ids.my_manager.current = "music ui"
                        IconLeftWidget:
                            icon: "music"
                        IconRightWidget:
                            icon: "dots-vertical"
                    MDGridLayout:
                        rows: 1
                        cols: 3
                        
                        spacing: grid.width/3.7
                        
                        MDFloatingActionButton:
                            icon: "skip-previous"
                            elevation: dp(10)
                            on_release: app.Previous()
                        
                        MDFloatingActionButton:
                            icon: "play"
                            id: play1
                            elevation: dp(10)
                            on_release: app.Play()
                        
                        MDFloatingActionButton:
                            icon: "skip-next"
                            elevation: dp(10)
                            on_release: app.Next()
                Widget:
                    size_hint_y: None
                    height: dp(50)
                    
                    

##########################################
############### Music Screen ############
        MusicScreen:
            name: "music screen"
            EffectWidget:
                effects: [ew.VerticalBlurEffect(size=10), ew.HorizontalBlurEffect(size=10)]
                
                FitImage:
                    source: "FB_IMG_1580579556493.jpg"
                
            MDBoxLayout:
                orientation: "vertical"
                
                MDBackdrop:
                    title: "Music"
                    left_action_items: [["magnify", lambda x: self.open()]]
                    header_text: "search music"
                
                    MDBackdropBackLayer:
                        MDBoxLayout:
                            orientation: "vertical"
                            padding: dp(10)
                            md_bg_color: (1, 1, 1, 1)
                            
                            
                            MDTextField:
                                hint_text: "enter music name"
                                size_hint_y: None
                                height: dp(50)
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
                                    #md_bg_color: (0, 0, 0, 1)
                                
                                MDIconButton:
                                    icon: "delete"
                                    #md_bg_color: (0, 0, 0, 1)
                            Label:
                                
                    
                    MDBackdropFrontLayer:
                        BoxLayout:
                            orientation: "vertical"
                    
                    
                    
                            RecycleView:
                                id: rv
                                viewclass: "CustomIconItem"
                                RecycleBoxLayout:
                                    orientation: "vertical"
                                    size_hint_y: None
                                    height: self.minimum_height
                            
                            MDGridLayout:
                                size_hint_y: None
                                height: dp(120)
                                rows: 2
                                cols: 1
                                spacing: dp(10)
                                padding: dp(10)
                                
                                OneLineAvatarIconListItem:
                                    #text: "Play Music"
                                    id: music_namem
                                    on_release: root.ids.my_manager.current = "music ui"
                                    IconLeftWidget:
                                        icon: "music"
                                    IconRightWidget:
                                        icon: "dots-vertical"
                                MDGridLayout:
                                    rows: 1
                                    cols: 3
                                    
                                    spacing: grid.width/3.7
                                    
                                    MDFloatingActionButton:
                                        icon: "skip-previous"
                                        elevation: dp(10)
                                        on_release: app.Previous()
                        
                                    MDFloatingActionButton:
                                        icon: "play"
                                        id: play2
                                        elevation: dp(10)
                                        on_release: app.Play()
                                    
                                    MDFloatingActionButton:
                                        icon: "skip-next"
                                        elevation: dp(10)
                                        on_release: app.Next()
                            Widget:
                                size_hint_y: None
                                height: dp(50)
                                
                                MDFloatingActionButton:
                                    icon: "home"
                                    elevation: dp(10)
                                    size_hint: None, None
                                    size: dp(50), dp(50)
                                    pos_hint: None, None
                                    pos:  dp(root.width/5), dp(root.height/2)
                                    on_release: root.ids.my_manager.current = "home screen"
                                    
                            

##########################################
############### Recently Screen ############
        RecentlyScreen:
            name: "recent screen"
            EffectWidget:
                effects: [ew.VerticalBlurEffect(size=10), ew.HorizontalBlurEffect(size=10)]
                
                FitImage:
                    source: "FB_IMG_1580579556493.jpg"
                
            MDBoxLayout:
                orientation: "vertical"
                
                MDToolbar:
                    title: "Recently Played"
                
                Label:
                
                MDGridLayout:
                    size_hint_y: None
                    height: dp(120)
                    rows: 2
                    cols: 1
                    spacing: dp(10)
                    padding: dp(10)
                    
                    OneLineAvatarIconListItem:
                        #text: "Play Music"
                        id: music_namer
                        on_release: root.ids.my_manager.current = "music ui"
                        IconLeftWidget:
                            icon: "music"
                        IconRightWidget:
                            icon: "dots-vertical"
                    MDGridLayout:
                        rows: 1
                        cols: 3
                        
                        spacing: grid.width/3.7
                        
                        MDFloatingActionButton:
                            icon: "skip-previous"
                            elevation: dp(10)
                            on_release: app.Previous()
            
                        MDFloatingActionButton:
                            icon: "play"
                            id: play3
                            elevation: dp(10)
                            on_release: app.Play()
                        
                        MDFloatingActionButton:
                            icon: "skip-next"
                            elevation: dp(10)
                            on_release: app.Next()
                Widget:
                    size_hint_y: None
                    height: dp(50)
                    
                    MDFloatingActionButton:
                        icon: "home"
                        elevation: dp(10)
                        size_hint: None, None
                        size: dp(50), dp(50)
                        pos_hint: None, None
                        pos:  dp(root.width/5), dp(root.height/2)
                        on_release: root.ids.my_manager.current = "home screen"
                        
                    
                

##########################################
############### Favourite Screen ############
        FavouriteScreen:
            name: "favourite screen"
            EffectWidget:
                effects: [ew.VerticalBlurEffect(size=10), ew.HorizontalBlurEffect(size=10)]
                
                FitImage:
                    source: "FB_IMG_1580579556493.jpg"
                
            MDBoxLayout:
                orientation: "vertical"
                
                MDToolbar:
                    title: "Favourites"
                
                Label:
                
                MDGridLayout:
                    size_hint_y: None
                    height: dp(120)
                    rows: 2
                    cols: 1
                    spacing: dp(10)
                    padding: dp(10)
                    
                    OneLineAvatarIconListItem:
                        #text: "Play Music"
                        id: music_namef
                        on_release: root.ids.my_manager.current = "music ui"
                        IconLeftWidget:
                            icon: "music"
                        IconRightWidget:
                            icon: "dots-vertical"
                    MDGridLayout:
                        rows: 1
                        cols: 3
                        
                        spacing: grid.width/3.7
                        
                        MDFloatingActionButton:
                            icon: "skip-previous"
                            elevation: dp(10)
                            on_release: app.Previous()
            
                        MDFloatingActionButton:
                            icon: "play"
                            id: play4
                            elevation: dp(10)
                            on_release: app.Play()
                        
                        MDFloatingActionButton:
                            icon: "skip-next"
                            elevation: dp(10)
                            on_release: app.Next()
                Widget:
                    size_hint_y: None
                    height: dp(50)
                    
                    MDFloatingActionButton:
                        icon: "home"
                        elevation: dp(10)
                        size_hint: None, None
                        size: dp(50), dp(50)
                        pos_hint: None, None
                        pos: dp(root.width/5), dp(root.height/2)
                        on_release: root.ids.my_manager.current = "home screen"
                        
                    
                

##########################################
############### Playlist Screen ############
        PlaylistScreen:
            name: "playlist screen"
            EffectWidget:
                effects: [ew.VerticalBlurEffect(size=10), ew.HorizontalBlurEffect(size=10)]
                
                FitImage:
                    source: "FB_IMG_1580579556493.jpg"
                
            MDBoxLayout:
                orientation: "vertical"
                
                MDToolbar:
                    title: "Playlist"
                
                Label:
                
                MDGridLayout:
                    size_hint_y: None
                    height: dp(120)
                    rows: 2
                    cols: 1
                    spacing: dp(10)
                    padding: dp(10)
                    
                    OneLineAvatarIconListItem:
                        #text: "Play Music"
                        id: music_namep
                        on_release: root.ids.my_manager.current = "music ui"
                        IconLeftWidget:
                            icon: "music"
                        IconRightWidget:
                            icon: "dots-vertical"
                    MDGridLayout:
                        rows: 1
                        cols: 3
                        
                        spacing: grid.width/3.7
                        
                        MDFloatingActionButton:
                            icon: "skip-previous"
                            elevation: dp(10)
                            on_release: app.Previous()
            
                        MDFloatingActionButton:
                            icon: "play"
                            id: play5
                            elevation: dp(10)
                            on_release: app.Play()
                        
                        MDFloatingActionButton:
                            icon: "skip-next"
                            elevation: dp(10)
                            on_release: app.Next()
                Widget:
                    size_hint_y: None
                    height: dp(50)
                    
                    MDFloatingActionButton:
                        icon: "home"
                        elevation: dp(10)
                        size_hint: None, None
                        size: dp(50), dp(50)
                        pos_hint: None, None
                        pos:  dp(root.width/5), dp(root.height/2)
                        on_release: root.ids.my_manager.current = "home screen"
   
                        
#############################################
############# MusicUi Screen ##############                 

        MusicUi:
            name: "music ui"
            EffectWidget:
                effects: [ew.VerticalBlurEffect(size=10), ew.HorizontalBlurEffect(size=10)]
                
                FitImage:
                    source: "FB_IMG_1580579556493.jpg"
                
            MDBoxLayout:
                orientation: "vertical"
                
                Label:            
                
                MDGridLayout:
                    size_hint_y: .5
                    #height: dp(120)
                    rows: 4
                    cols: 1
                    spacing: dp(10)
                    padding: dp(10)
                    MDBoxLayout:
                        padding: dp(5)
                        Slider:
                            max:100
                            min : 0
                            color: (1, 0, 0, 1)
                            cursor_image: ""
                            cursor_size: (dp(10), dp(10))
                            background_width: dp(20)
                            value_track_color: (1, 0, 0, 1)
                        
                        Label:
                            size_hint_x: None
                            id: Music_time
                            width: dp(20)
                            text: "00:00"
                    
                    MDGridLayout:
                        cols: 3
                        rows: 1
                        spacing: grid.width/3.5
                        MDIconButton:
                            icon: "heart-plus"
                            on_release: app.add_favite()
                        
                        MDIconButton:
                            icon: "repeat"
                            id: repeat
                            on_release: app.repeat()
                        
                        MDIconButton:
                            icon: "shuffle-disabled"
                            id: shuffle
                            on_release: app.play_random()
                            
                    OneLineListItem:
                        #text: "Play Music"
                        id: music_name
                        
                    MDGridLayout:
                        rows: 1
                        cols: 3
                        
                        spacing: grid.width/3.7
                        
                        MDFloatingActionButton:
                            icon: "skip-previous"
                            elevation: dp(10)
                            on_release: app.Previous()
                        
                        MDFloatingActionButton:
                            icon: "play"
                            id: play
                            elevation: dp(10)
                            on_release: app.Play()
                        
                        MDFloatingActionButton:
                            icon: "skip-next"
                            elevation: dp(10)
                            on_release: app.Next()
                    
                
                Widget:
                    size_hint_y: None
                    height: dp(50)
                    
                    MDFloatingActionButton:
                        icon: "music"
                        elevation: dp(10)
                        size_hint: None, None
                        size: dp(50), dp(50)
                        pos_hint: None, None
                        pos:  dp(10), dp(root.height/2)
                        on_release: root.ids.my_manager.current = "music screen"
   
#############################################
############# Settings Screen ##############                 

        SettingsScreen:
            name: "setting"
            EffectWidget:
                effects: [ew.VerticalBlurEffect(size=10), ew.HorizontalBlurEffect(size=10)]
                
                FitImage:
                    source: "FB_IMG_1580579556493.jpg"
                
            MDBoxLayout:
                orientation: "vertical"
                
                MDToolbar:
                    
                    title: "Settings"
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
                        icon: "home"
                        elevation: dp(10)
                        size_hint: None, None
                        size: dp(50), dp(50)
                        pos_hint: None, None
                        pos:  dp(root.width/5), dp(root.height/2)
                        on_release: root.ids.my_manager.current = "home screen"
                
                
                               
                




##########################################################
###################### navigation menu ####################            
    MDNavigationDrawer:
        id: nav_drawer    
        
        MDBoxLayout:
            orientation: "vertical"
            padding: dp(5)
            
            MDToolbar:
                title: "Menu"
                
            
            OneLineIconListItem:
                text: "Music"
                on_release: root.ids.my_manager.current = "music screen"
                IconLeftWidget:
                    icon: "music"
                    
            OneLineIconListItem:
                text: "Recently Played"
                on_release: root.ids.my_manager.current = "recent screen"
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
            Label:
            
            OneLineIconListItem:
                text: "More"
                on_release: root.ids.my_manager.current = "setting"
                IconLeftWidget:
                    icon: "headphones-settings"
            
            Label:

"""

######################################
################# music loop code #######

Music = []
Music1 = []
path = "//storage//emulated//0"
for filename in os.listdir(path):
    current_path = os.path.join(path, filename)

    if os.path.isdir(current_path):
        rec_audio_dirs = current_path
    # audio_dirs.append(rec_audio_dirs)

    elif filename.endswith(".mp3") or filename.endswith(".m4a"):
        if filename in Music:
            pass
        else:

            Music.append(current_path)
            Music1.append(filename)


#############################################
########## Screens ##########################
class IntroScreen(Screen):
    pass


class HomeScreen(Screen):
    pass


class MusicScreen(Screen):
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

#########################################
############### Custom button ###########


class CustomIconItem(OneLineAvatarIconListItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        iteml = IconLeftWidget(icon="music")
        itemr = IconRightWidget(icon="dots-vertical")
        self.add_widget(itemr)
        self.add_widget(iteml)


class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.transition = WipeTransition
        Clock.schedule_once(self.Change, 10)




    def Change(self, dt):
        self.current = "home screen"


class TinselPlayer(MDApp, App):
    try:
        
        
        
        
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.Music1 = Music1
            self.Music = Music
            
            self.player = Player()
            max_iteration = -200
            
            
            self.x = 0
            
            
            
            
            
            
            
        def build(self):
            #self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette = "Orange"
            builder = Builder.load_string(Code)
            return builder
            
            
            
            
            

        def on_start(self):
            data = [{"text": str(Music1[i]), "size_hint_x": 1, "on_release": lambda x=i: self.play_music(Music[x], Music1[x])} for i in range(len(Music))]

            self.root.ids.rv.data = data
            
            
            
            
            
            

        def play_music(self, text, text1):
            self.path_name = text
            self.music_name = text1
            self.player.play(text)

            self.root.ids.music_name.text = str(self.music_name)
            self.root.ids.music_nameh.text = str(self.music_name)
            self.root.ids.music_namem.text = str(self.music_name)
            self.root.ids.music_namer.text = str(self.music_name)
            self.root.ids.music_namep.text = str(self.music_name)
            self.root.ids.music_namef.text = str(self.music_name)
            self.root.ids.play.icon = "pause"
            self.root.ids.play1.icon = "pause"
            self.root.ids.play2.icon = "pause"
            self.root.ids.play3.icon = "pause"
            self.root.ids.play4.icon = "pause"
            self.root.ids.play5.icon = "pause"
            
            
            
            
            

        def Theme_Change(self):
            theme = MDThemePicker()
            theme.open()








        def add_favite(self):
            pass






        def Previous(self):
            numy = random.randint(0, len(Music))
            self.x -=1
            numx = self.Music.index(self.path_name) + self.x
            num = numx
            if self.root.ids.shuffle.icon == "shuffle-disabled":
	            if num >= 0:
	                self.player.play(Music[numx])
	                self.root.ids.music_name.text = str(Music1[num])
	                self.root.ids.music_nameh.text = str(Music1[num])
	                self.root.ids.music_namem.text = str(Music1[num])
	                self.root.ids.music_namer.text = str(Music1[num])
	                self.root.ids.music_namep.text = str(Music1[num])
	                self.root.ids.music_namef.text = str(Music1[num])

            elif self.root.ids.shuffle.icon == "shuffle-variant":
                 self.player.play(Music[numy])
                 self.root.ids.music_name.text = str(Music1[numy])
                 self.root.ids.music_nameh.text = str(Music1[numy])
                 self.root.ids.music_namem.text = str(Music1[numy])
                 self.root.ids.music_namer.text = str(Music1[numy])
                 self.root.ids.music_namep.text = str(Music1[numy])
                 self.root.ids.music_namef.text = str(Music1[numy])
                 	                	                







        def Play(self):
            if self.root.ids.play.icon == "play":
                self.player.resume()
                self.root.ids.play.icon = "pause"
                self.root.ids.play1.icon = "pause"
                self.root.ids.play2.icon = "pause"
                self.root.ids.play3.icon = "pause"
                self.root.ids.play4.icon = "pause"
                self.root.ids.play5.icon = "pause"

            elif self.root.ids.play.icon == "pause":
                self.player.pause()
                self.root.ids.play.icon = "play"
                self.root.ids.play1.icon = "play"
                self.root.ids.play2.icon = "play"
                self.root.ids.play3.icon = "play"
                self.root.ids.play4.icon = "play"
                self.root.ids.play5.icon = "play"






        def Next(self):
            numy = random.randint(0, len(Music))
            self.x += 1
            numx = self.Music.index(self.path_name) + self.x
            num = numx
            if self.root.ids.shuffle.icon == "shuffle-disabled":
	            if num >= 1 or num <= (len(Music) -1):
	                self.player.play(Music[numx])
	                self.root.ids.music_name.text = str(Music1[num])
	                self.root.ids.music_nameh.text = str(Music1[num])
	                self.root.ids.music_namem.text = str(Music1[num])
	                self.root.ids.music_namer.text = str(Music1[num])
	                self.root.ids.music_namep.text = str(Music1[num])
	                self.root.ids.music_namef.text = str(Music1[num])
	                
            elif self.root.ids.shuffle.icon == "shuffle-variant":
                 self.player.play(Music[numy])
                 self.root.ids.music_name.text = str(Music1[numy])
                 self.root.ids.music_nameh.text = str(Music1[numy])
                 self.root.ids.music_namem.text = str(Music1[numy])
                 self.root.ids.music_namer.text = str(Music1[numy])
                 self.root.ids.music_namep.text = str(Music1[numy])
                 self.root.ids.music_namef.text = str(Music1[numy])
                 
                 
                 
                 
                 
                 
        def repeat(self):
            if self.root.ids.repeat.icon ==  "repeat":
            	self.root.ids.repeat.icon = "repeat-once"
            	self.player.do_loop(True)
            elif self.root.ids.repeat.icon ==  "repeat-once":
            	self.root.ids.repeat.icon = "repeat"
            	self.player.do_loop(False)
           
           
           
           
           
          

        def play_random(self):
            if self.root.ids.shuffle.icon == "shuffle-variant":
            	self.root.ids.shuffle.icon ="shuffle-disabled"
            
            elif self.root.ids.shuffle.icon =="shuffle-disabled":
            	self.root.ids.shuffle.icon = "shuffle-variant"




    except:
        pass



TinselPlayer().run()

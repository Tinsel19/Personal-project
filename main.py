from kivy.app import App
from kivy.core.window import Window
from kivy.graphics.instructions import Image
from kivy.lang import builder, Builder
from kivy.metrics import dp
from kivy.properties import Clock, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition, FadeTransition, WipeTransition
from kivymd.app import MDApp
from webbrowser import open_new_tab

##############################################################
###########################################################
##IMPORT SCREENS
from kivymd.uix.filemanager import IconButton
from kivymd.uix.list import OneLineAvatarListItem, TwoLineAvatarListItem

from Screen import AppOpen
from Screen1 import Screen1
from Screen2 import Screen2
from Screen3 import Screen3
from Screen4 import Screen4
from Screen5 import Screen5
from Screen6 import Screen6
from Screen7 import Screen7
from Screen8 import Screen8
from Screen9 import Screen9
from Screen10 import Screen10

x = TwoLineAvatarListItem
# y = ImageLeftWidget
#########################################################
### WINDOW DEFAULT SIZE
#Window.size = (dp(400), dp(700))


class CustomButton(IconButton, Image):
    pass


class ArtAuctionApp(MDApp, App):
    def __init__(self, **kwargs):
    	super().__init__(**kwargs)
    	self.sm = ScreenManager()
    	Clock.schedule_once(self.Change, 4)
    	Window.softinput_mode = "below_target"
    
    def Change(self, dt):
    	self.sm.current = "Page1"
    	
    def build(self):
        ##########################################################################
        #####################################################################
        ##Theme
        # self.theme_cls.theme_style = "Dark"
        # self.theme_cls.primary_palette = "Black"
        #########################################################################
        ########################################################################
        ##Clock Iteration
        #Clock.max_iteration = 8
        ##########################################################################
        ########################################################################
        ##ScreenManager
        
        # self.sm.transition_state = "in"
        # self.sm.transition = WipeTransition()
        self.sm.add_widget(Builder.load_string(AppOpen))
        self.sm.add_widget(Builder.load_string(Screen1))
        self.sm.add_widget(Builder.load_string(Screen2))
        self.sm.add_widget(Builder.load_string(Screen3))
        self.sm.add_widget(Builder.load_string(Screen4))
        self.sm.add_widget(Builder.load_string(Screen5))
        self.sm.add_widget(Builder.load_string(Screen6))
        self.sm.add_widget(Builder.load_string(Screen7))
        self.sm.add_widget(Builder.load_string(Screen8))
        self.sm.add_widget(Builder.load_string(Screen9))
        self.sm.add_widget(Builder.load_string(Screen10))

        return self.sm

    ##############################################
    ##### BACK BUTTON TO SIGN UP PAGE
    def back_five(self):
        self.sm.current = "Page5"
        self.sm.transition.direction = "right"
        return self.sm

    ############################################
    ###### BACK BUTTON TO LOG IN PAGE AFTER FIRST SIGN IN
    def back_six(self):
        self.sm.current = "Page6"
        self.sm.transition.direction = "right"
        return self.sm

    ############################################
    ###### BACK BUTTON TO FORGOT PASSWORD PAGE
    def back_seven(self):
        self.sm.current = "Page7"
        self.sm.transition.direction = "right"
        return self.sm

    ###########################################
    ######### BACK BUTTON TO SET UP A NEW PASSWORD PAGE
    def back_eight(self):
        self.sm.current = "Page8"
        self.sm.transition.direction = "right"
        return self.sm

    ##############################################
    ########### BACK BUTTON TO LOG IN AND SIGN UP PAGE
    def back_four(self):
        self.sm.current = "Page4"
        self.sm.transition.direction = "right"
        return self.sm

    #############################################
    ####### RESET TEXTFIELDS IN PAGE FIVE ON SIGN UP CLICK
    def reset_text_five(self):
        self.root.ids.text1.text = ""
        #self.sm.remove_widget(self.sm.add_widget(Builder.load_string(Screen5)))
        #return self.sm.add_widget(Builder.load_string(Screen5))






ArtAuctionApp().run()

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.app import MDApp
from kivymd import images_path
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
import ast
import numpy as np
import math
# from kvdroid.tools import speech
from kivy.app import App
from kivy.core.window import Window
from kivymd.uix.list import TwoLineListItem
from kivy.uix.screenmanager import Screen, ScreenManager
from fractions import Fraction

KV = '''

#: import webbrowser webbrowser


<Numbers>
    size_hint_y: None
    height: self.minimum_height
    cols: 4
    
    MDFlatButton:
        text: "1"
        on_press: app .one()
    
    MDFlatButton:
        text: "2"
        on_press: app.two()
    
    MDFlatButton:
        text: "3"
        on_press: app.three()
    
    MDFlatButton:
        text: "4"
        on_press: app.four()
    
    
    MDFlatButton:
        text: "5"
        on_press: app.five()
    
    
    MDFlatButton:
        text: "6"
        on_press: app.six()
    
    
    MDFlatButton:
        text: "7"
        on_press: app.seven()
    
    
    MDFlatButton:
        text: "8"
        on_press: app.eight()
    
    
    MDFlatButton:
        text: "9"
        on_press: app.nine()
    
    
    MDFlatButton:
        text: "0"
        on_press: app.zero()
    
    
    MDFlatButton:
        text: "."
        on_press: app.dot()
    
    
    MDFlatButton:
        text: ","
        on_press: app.coma()
    
    
    MDFlatButton:
        text: "="
        on_press: app.equals()
    
    MDFlatButton:
        text: "- - -"
        on_press: app.space()
    
    
    MDFlatButton:
        text: "del"
        on_press: app.delete()
    
    
    MDFlatButton:
        text: "C"
        on_press: app.clear()
    
    
  
  
  
  
  
  
<Numerical_Op>
    size_hint_y: None
    height: self.minimum_height
    cols: 4
    
    MDFlatButton:
        text: "("
        on_press: app.left_bracket()
    
    MDFlatButton:
        text: ")"
        on_press: app.right_bracket()
    
    MDFlatButton:
        text: "÷"
        on_press: app.divide()
    
    MDFlatButton:
        text: "*"
        on_press: app.multiply()
    
    MDFlatButton:
        text: "+"
        on_press: app.addition()
    
    MDFlatButton:
        text: "-"
        on_press: app.subtract()
    
    MDFlatButton:
        text: "√"
        on_press: app.square_root()
    
    MDFlatButton:
        text: "^"
        on_press: app.power()
    
    MDFlatButton:
        text: "del"
        on_press: app.delete()
        
    
    MDFlatButton:
        text: "ans"
        on_press: app.answer()
    
    MDFlatButton:
        text: "π"
        on_press: app.Pi()
    
    MDFlatButton:
        text: "="
        on_press: app.equals()









<Trig_Func>
    size_hint_y: None
    height: self.minimum_height
    cols: 4
    
    MDFlatButton:
        text: "sin"
        on_press: app.Sin()
    
    MDFlatButton:
        text: "cos"
        on_press: app.Cos()
        
    
    MDFlatButton:
        text: "tan"
        on_press: app.Tan()
    
    MDFlatButton:
        text: "asin"
        on_press: app.ASin()
    
    MDFlatButton:
        text: "acos"
        on_press: app.ACos()
    
    MDFlatButton:
        text: "atan"
        on_press: app.ATan()
    
    MDFlatButton:
        text: "C"
        on_press: app.clear()
    
    MDFlatButton:
        text: "="
        on_press: app.equals()

<Adavanced>
    size_hint_y: None
    height: self.minimum_height
    cols: 4

  
  
  
  
  
   
<Matrix>
    size_hint_y: None
    height: self.minimum_height
    #spacing: dp(5)
    cols: 1
    
    
    MDGridLayout:
        cols: 3
        rows: 1
        size_hint_y: None
        spacing: dp(30)
        height: self.minimum_height
        
        MDRaisedButton:
            text: "m1*m2"
            theme_text_color: "Custom"
            text_color: (0, 0, 0, .9)
            md_bg_color: (1, 1, 1, 1)
            on_press: app.matrix_multiply()
        
        MDRaisedButton:
            text: "m1+m2"
            theme_text_color: "Custom"
            text_color: (0, 0, 0, .9)
            md_bg_color: (1, 1, 1, 1)
            on_press: app.matrix_addition()
        
        MDRaisedButton:
            text: "m1-m2"
            theme_text_color: "Custom"
            text_color: (0, 0, 0, .9)
            md_bg_color: (1, 1, 1, 1)
            on_press: app.matrix_subtraction()

    
    GridLayout:
        cols: 2
        
        MDGridLayout:
            cols: 4
            rows: 5
            
            MDFlatButton:
                text: "{"
                on_press: app.m_l_bracket()
                theme_text_color: "Custom"
                text_color: (1, .5, 0, 1)
            
            MDFlatButton:
                text: "}"
                on_press: app.m_r_bracket()
                theme_text_color: "Custom"
                text_color: (1, .5, 0, 1)
        
            MDFlatButton:
                text: "1"
                on_press: app.m_one()
                theme_text_color: "Custom"
                text_color: (1, .5, 0, 1)
            
            MDFlatButton:
                text: "2"
                on_press: app.m_two()
                theme_text_color: "Custom"
                text_color: (1, .5, 0, 1)
            
            MDFlatButton:
                text: "3"
                on_press: app.m_three()
                theme_text_color: "Custom"
                text_color: (1, .5, 0, 1)
            
            MDFlatButton:
                text: "4"
                on_press: app.m_four()
                theme_text_color: "Custom"
                text_color: (1, .5, 0, 1)
            
            
            MDFlatButton:
                text: "5"
                on_press: app.m_five()
                theme_text_color: "Custom"
                text_color: (1, .5, 0, 1)
            
            
            MDFlatButton:
                text: "6"
                on_press: app.m_six()
                theme_text_color: "Custom"
                text_color: (1, .5, 0, 1)
            
            
            MDFlatButton:
                text: "7"
                on_press: app.m_seven()
                theme_text_color: "Custom"
                text_color: (1, .5, 0, 1)
            
            
            MDFlatButton:
                text: "8"
                on_press: app.m_eight()
                theme_text_color: "Custom"
                text_color: (1, .5, 0, 1)
            
            
            MDFlatButton:
                text: "9"
                on_press: app.m_nine()
                theme_text_color: "Custom"
                text_color: (1, .5, 0, 1)
            
            
            MDFlatButton:
                text: "0"
                on_press: app.m_zero()
                theme_text_color: "Custom"
                text_color: (1, .5, 0, 1)
            
            
            MDFlatButton:
                text: "."
                on_press: app.m_dot()
                theme_text_color: "Custom"
                text_color: (1, .5, 0, 1)
            
            
            MDFlatButton:
                text: ","
                on_press: app.m_coma()
                theme_text_color: "Custom"
                text_color: (1, .5, 0, 1)
            
            MDFlatButton:
                text: "- - -"
                on_press: app.m_space()
                theme_text_color: "Custom"
                text_color: (1, .5, 0, 1)
            
            
            MDFlatButton:
                text: "del"
                on_press: app.m_delete()
                theme_text_color: "Custom"
                text_color: (1, .5, 0, 1)
            
            
            MDFlatButton:
                text: "C"
                on_press: app.m_clear()
                theme_text_color: "Custom"
                text_color: (1, .5, 0, 1)
            
            MDFlatButton:
                text: "|M1|"
                on_press: app.m_det()
                theme_text_color: "Custom"
                text_color: (1, .5, 0, 1)
    
    
        
        GridLayout:
            cols: 4
            rows: 5
            
            MDFlatButton:
                text: "{"
                on_press: app.m2_l_bracket()
            
            MDFlatButton:
                text: "}"
                on_press: app.m2_r_bracket()
     
            MDFlatButton:
                text: "1"
                on_press: app.m2_one()
            
            MDFlatButton:
                text: "2"
                on_press: app.m2_two()
            
            MDFlatButton:
                text: "3"
                on_press: app.m2_three()
            
            MDFlatButton:
                text: "4"
                on_press: app.m2_four()
            
            
            MDFlatButton:
                text: "5"
                on_press: app.m2_five()
            
            
            MDFlatButton:
                text: "6"
                on_press: app.m2_six()
            
            
            MDFlatButton:
                text: "7"
                on_press: app.m2_seven()
            
            
            MDFlatButton:
                text: "8"
                on_press: app.m2_eight()
            
            
            MDFlatButton:
                text: "9"
                on_press: app.m2_nine()
            
            
            MDFlatButton:
                text: "0"
                on_press: app.m2_zero()
            
            
            MDFlatButton:
                text: "."
                on_press: app.m2_dot()
            
            
            MDFlatButton:
                text: ","
                on_press: app.m2_coma()
          
            
            MDFlatButton:
                text: "- - -"
                font_size: dp(10)
                on_press: app.m2_space()
            
            
            MDFlatButton:
                text: "del"
                on_press: app.m2_delete()
            
            
            MDFlatButton:
                text: "C"
                on_press: app.m2_clear()
            
            MDFlatButton:
                text: "|M2|"
                on_press: app.m2_det()






###################
###################









<Advanced>
    cols: 4
    size_hint_y: None
    height: self.minimum_height
    size_hint_x: 1
    
    MDFlatButton:
        text: "log"
        on_press: app.Log()
    
    MDFlatButton:
        text: "alog"
        on_press: app.Antilog()
    
    MDFlatButton:
        text: "!"
        on_press: app.Factorial()
    
    MDFlatButton:
        text: "e"
        on_press: app.Exponential()



<Quadratic>
    cols: 1
    spacing: dp(10)
    size_hint_y: None
    height: self.minimum_height
    size_hint_x: 1
    
    GridLayout:
        cols: 6
        rows: 3

        MDFlatButton:
            text: "x²"
            on_press: app.q_x_power()

        MDFlatButton:
            text: "x"
            on_press: app.q_x()
                
                                
        MDFlatButton:
            text: "1"
            on_press: app .q_one()
        
        MDFlatButton:
            text: "2"
            on_press: app.q_two()
        
        MDFlatButton:
            text: "3"
            on_press: app.q_three()
        
        MDFlatButton:
            text: "4"
            on_press: app.q_four()
        
        
        MDFlatButton:
            text: "5"
            on_press: app.q_five()
        
        
        MDFlatButton:
            text: "6"
            on_press: app.q_six()
        
        
        MDFlatButton:
            text: "7"
            on_press: app.q_seven()
        
        
        MDFlatButton:
            text: "8"
            on_press: app.q_eight()
        
        
        MDFlatButton:
            text: "9"
            on_press: app.q_nine()
        
        
        MDFlatButton:
            text: "0"
            on_press: app.q_zero()
        
        
        MDFlatButton:
            text: "."
            on_press: app.q_dot()
        
        
        MDFlatButton:
            text: "+"
            on_press: app.q_plus()
        
        
        
        MDFlatButton:
            text: "-"
            on_press: app.q_subtract()
        
        
        MDFlatButton:
            text: "del"
            on_press: app.q_delete()
        
        
        MDFlatButton:
            text: "C"
            on_press: app.q_clear()
        
    

        MDFlatButton:
            text: "="
            on_press: app.q_equals()
    
        
    

<Simultaneous>
    cols: 5
    size_hint_y: None
    height: self.minimum_height
    id: simulate2
    size_hint_x: 1
    
    
    MDFlatButton:
        text: "v"
        on_press: app.s_v()
    
    MDFlatButton:
        text: "x"
        on_press: app.s_x()
    
    MDFlatButton:
        text: "y"
        on_press: app.s_y()

    
    MDFlatButton:
        text: "z"
        on_press: app.s_z()
        
    MDFlatButton:
        text: "k"
        on_press: app.s_k()
    
    MDFlatButton:
        text: "{"
        on_press: app.s_l_bracket()
    
    MDFlatButton:
        text: "}"
        on_press: app.s_r_bracket()
    
    MDFlatButton:
        text: "1"
        on_press: app.s_one()
    
    MDFlatButton:
        text: "2"
        on_press: app.s_two()

    
    MDFlatButton:
        text: "3"
        on_press: app.s_three()

    
    MDFlatButton:
        text: "4"
        on_press: app.s_four()
    
    MDFlatButton:
        text: "5"
        on_press: app.s_five()
    
    MDFlatButton:
        text: "6"
        on_press: app.s_six()
    
    MDFlatButton:
        text: "7"
        on_press: app.s_seven()

    
    MDFlatButton:
        text: "8"
        on_press: app.s_eight()
    
    MDFlatButton:
        text: "9"
        on_press: app.s_nine()
    
    MDFlatButton:
        text: "0"
        on_press: app.s_zero()
    
    MDFlatButton:
        text: "+"
        on_press: app.s_plus()

    
    MDFlatButton:
        text: "-"
        font_size: dp(20)
        on_press: app.s_minus()
    
    MDFlatButton:
        text: "•"
        on_press: app.s_dot()
    
    MDFlatButton:
        text: ","
        on_press: app.s_coma()
    
    MDFlatButton:
        text: "del"
        on_press: app.s_delete()
    
    MDFlatButton:
        text: "C"
        on_press: app.s_clear()

    
    MDFlatButton:
        text: "="
        on_press: app.s_equals()


    
    
        
        



###############################
##############################
########### MAIN LAYOUT #########


MDNavigationLayout:
    MyManager:
        id: manager
        MainScreen:
            name: "main"
            MDBoxLayout:
                textinput: textinput
                orientation: "vertical"
                padding: dp(10)
                spacing: dp(10)
                md_bg_color: (0, 0, 0, .02)
                
                MDToolbar:
                    title: "Calculator"
                    specific_text_color: (1, 1, 1, 1)
                    #md_bg_color: (1, 1, 1, 1)
                    elevation: 10
                    left_action_items: [["menu" , lambda x: nav_drawer.set_state("toggle")]]
                    right_action_items: [["help"  , lambda x: nav_drawer2.set_state("toggle")]]
                    
                TextInput:
                    text: "0"
                    
                    size_hint: 1, .6
                    background_normal: ""
                    halign: "left"
                    padding: 30, 30
                    id: textinput
                    font_size: dp(15)
                
                TextInput:
                    hint_text: "0"
                    size_hint: 1, .3
                    background_normal: ""
                    halign: "right"
                    readonly: True
                    padding: 30, 10
                    font_size: dp(13)
                    id: result
                
                
                ScrollView:
                    GridLayout:
                        size_hint_y: None
                        id: vox
                        height: self.minimum_height
                        cols: 2
                        spacing: dp(10)
                           
                        GridLayout:
                            spacing: dp(30)
                            id: box
                            cols: 1
                            size_hint_y: None
                            height: self.minimum_height
                
                ScrollView:
                    GridLayout:
                        size_hint_y: None
                        id: tin
                        height: self.minimum_height
                        cols: 2
                        spacing: dp(10)
                        
                        GridLayout:
                            size_hint_y: None
                            id: hike
                            height: self.minimum_height
                            cols: 1
            
                
                
        
        
        MatrixScreen:
            name: "matrix"
            MDBoxLayout:
                orientation: "vertical"
                padding: dp(10)
                spacing: dp(10)
                MDToolbar:
                    title: "Matrix"
                    left_action_items: [["chevron-left", lambda x: app.Home()]]
                    specific_text_color: (1, 1, 1, 1)
                    #md_bg_color: (1, 1, 1, 1)
                    elevation: 10
                GridLayout:
                    cols: 2
                    rows: 1
                    size_hint_y: None
                    height: dp(200)
                    spacing: dp(10)
                            
                    TextInput:
                        hint_text: " M1 \\n enter matrix in the format \\n  { {a,  b}, {c,  d} }"
                        
                        id: uix
                        background_normal: ""
                        padding : 30, 30
                            
                    TextInput:
                        hint_text: "  M2  \\n enter matrix in the format \\n  { {a,  b}, {c,  d} }"
                        
                        id: uix2
                        background_normal: ""
                        padding: 30, 30
            
                ScrollView:
                    GridLayout:
                        size_hint_y: None
                        id: mat
                        height: dp(300)
                        cols: 1
            
        QuadraticScreen:
            name: "quadratic"
            MDBoxLayout:
                orientation: "vertical"            
                padding: dp(10)
                md_bg_color: (0, 0, 0, .02)
                spacing: dp(10)
                
                MDToolbar:
                    title: "Quadratic Equations"
                    left_action_items: [["chevron-left" , lambda x: app.Home()]]
                    specific_text_color: (1, 1, 1, 1)
                    #md_bg_color: (1, 1, 1, 1)
                    elevation: 10
                
                MDGridLayout:
                    cols: 1
                    id: quad
                    
                    TextInput:
                        id: quadin
                        hint_text: "ax² ± bX ± c"
                        background_normal: ""
                        halign: "center"
                        padding: 30, 30
                        size_hint_y: None
                        height: dp(200)
                
                
        
        SimultaneousScreen:
            name: "simulate"
            MDBoxLayout:
                orientation: "vertical"            
                padding: dp(10)
                md_bg_color: (0, 0, 0, .02)
                spacing: dp(10)
                id: sike
                
                MDToolbar:
                    title: "Simultaneous Equations"
                    left_action_items: [["chevron-left", lambda x: app.Home()]]
                    specific_text_color: (1, 1, 1, 1)
                    #md_bg_color: (1, 1, 1, 1)
                    elevation: 10
                    
                MDGridLayout:
                    cols: 1
                    id: simulate
                    
                    TextInput:
                        id: simulate1
                        hint_text: "{  v{v1, v2, v3, v4},    x{x1, x2, x3, x4},    y{y1, y2, y3, y4},    z{z1, z2, z3, z4},    k{k1, k2, k3, k4} } "
                        background_normal: ""
                        halign: "center"
                        padding: 30, 30
                        size_hint_y: None
                        #readonly: True
                        height: dp(200)
            
                
            
            
                
    MDNavigationDrawer:
        #anchor: "right"
        id: nav_drawer
        MDBoxLayout:
            orientation: "vertical"
            padding: dp(10)
            spacing: dp(10)
            MDToolbar:
                title: "Calculator"
                specific_text_color: (1, 1, 1, 1)    
                elevation: 10
            
            OneLineIconListItem:
                text: "Matrix"
                on_release: root.ids.manager.current = "matrix"
            
            OneLineIconListItem:
                text: "Quadratic"
                on_release: root.ids.manager.current = "quadratic"
            
            OneLineIconListItem:
                text: "Simultaneous"
                on_release: root.ids.manager.current = "simulate"
            
            OneLineIconListItem:
            
            OneLineIconListItem:
            
            Label:
            
            


    MDNavigationDrawer:
        anchor: "right"
        id: nav_drawer2
        MDBoxLayout:
            orientation: "vertical"
            padding: dp(10)
            spacing: dp(10)			
            
            MDToolbar:
                title: "Calculator"
                specific_text_color: (1, 1, 1, 1)
            
            MDGridLayout:
                cols: 1
                id: help
                spacing: dp(10)
                
                MDToolbar:
                    title: "History"
                    specific_text_color: (1, 1, 1, 1)
                    right_action_items: [["delete", lambda x: app.delete_history()]]
                
                ScrollView:
                    MDList:
                        size_hint_y: None
                        height: dp(800)
                        id: history_list
                        
                
                MDToolbar:
                    title: "Help"
                    specific_text_color: (1, 1, 1, 1)
                    
                    
                                                    
                ScrollView:
                    MDBoxLayout:
                        size_hint_y: None
                        height: dp(1700)
                        orientation: "vertical"
                        spacing: dp(10)
                        
                        Label:
                            color: (0, 0, 0, 1)
                            text: " C = clear all input \\n del = delete last element of the input \\n ! = factorial \\n e = exponential \\n ans = adds the previously gotten answer to the input field  "
                            size_hint_y: None
                            height: dp(200)
                            font_size: dp(11)			
                        
                        
                        Label:
                            color: (0, 0, 0, 1)
                            text: "Numbers \\n The numbers are hidden by default \\n and they require clicking on the \\n 1, 2, 3, 4, button for them to be \\n activated, the numbers drop down in cols of 4"
                            size_hint_y: None
                            height: dp(200)
                            font_size: dp(11)			
                            
                        
                        Label:
                            color: (0, 0, 0, 1)
                            text: "Numerical operators \\n Same as the procedure for accesing numbers, \\n click on the +, *, - button and the operators \\n drop down .  \\n There's a scroll option for both Nunbers and \\n Numerical operators incase the contents are below \\n screen view "
                            size_hint_y: None
                            height: dp(200)
                            font_size: dp(11)			
                        
                        
                        Label:
                            color: (0, 0, 0, 1)
                            text: "Trigonometry \\n Click on the sin, cos, tan button \\n to access the trigonometry functions. \\n The d and r figure seen when the sin and asin \\n buttons are pressed are for converting to degrees \\n and radians respectively. "
                            size_hint_y: None
                            height: dp(200)
                            font_size: dp(11)			
                        
                        
                        Label:
                            color: (0, 0, 0, 1)
                            text: "Advanced Functions \\n Contains the Log, antilog , factorials and some \\n other functions , click on the button to access them"
                            size_hint_y: None
                            height: dp(200)
                            font_size: dp(11)			
                        
                        
                        Label:
                            color: (0, 0, 0, 1)
                            text: "Matrix \\n There are two matrix input field visible by \\n default , both input field accept inputs from device \\n keyboard , the matrix input format has been specified . \\n A input button is hidden in the matrix input, \\n it contains the numbers, determinant , matrix  \\n  multiplication, addtion and subtraction \\n  for both matrix M1 and M2 input fileds. \\n To get accurate results , enter elements row \\n after row, "
                            size_hint_y: None
                            height: dp(200)
                            font_size: dp(11)			
                        
                        
                        Label:
                            color: (0, 0, 0, 1)
                            text: "Quadratic Equations \\n Click on the menu icon at the top left corner \\n of the screen to access the Quadratic equations , \\n the input field is  hidden as usual, click on the button \\n to access  the buttons, it also accepts input \\n from device keyboard"
                            size_hint_y: None
                            height: dp(200)
                            font_size: dp(11)	
                            
                        Label:
                            text: "Simultaneous Equations \\n The simultaneous equation calculator can solve only \\n equations with maximum number of 4 variables,\\n the v, x, y and z respectively, the order of label \\n doesn't matter , k stores the constant value of the  \\n equations. For instance , let's say an equation like  \\n the one below\\n     4x + 5y + 6z = 6 \\n    5x + y + z  = 0\\n    x + y = 1  \\n The above simultaneous equation shall be inputed \\n  in the format below \\n { x{4, 5, 1}, y{5, 1, 1}, z{6, 1, 0} , k{ 6, 0, 1} } \\n The coefficients of each variable are arranged  accordingly and \\n seperated by a coma each , the result of the equation \\n is [-0.08  1.48 -1.08], x, y, z values  are seperated by spaces \\n within the square brackets  "
                            size_hint_y: None
                            color: (0, 0, 0, 1)
                            height: dp(220)
                            font_size: dp(10)
                                
                                
                MDToolbar:
                    title: "Enquiries"
                    specific_text_color: (1, 1, 1, 1)
                        
                    MDIconButton:
                        icon: "gmail"
                        
                                                        
                            
'''


class Simultaneous(MDGridLayout):
    pass


class Quadratic(MDGridLayout):
    pass


class Advanced(GridLayout):
    pass


class Numbers(GridLayout):
    pass


class Numerical_Op(GridLayout):
    pass

######################################################
##############ScreenManager and Screens ##################
class MyManager(ScreenManager):
    pass


class MainScreen(Screen):
    pass


class QuadraticScreen(Screen):
    pass


class SimultaneousScreen(Screen):
    pass


class MatrixScreen(Screen):
    pass


class Trig_Func(GridLayout):
    pass


class Matrix(MDGridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.softinput_mode = "below_target"


class Test(MDApp, App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Light"

    def build(self):
        max_iteration = 8
        return Builder.load_string(KV)

    def on_start(self):
        Num = MDExpansionPanel(
            content=Numbers(),
            panel_cls=MDExpansionPanelOneLine(
                text="1, 2, 3, 4, 5, 6, 7, ..."
            )
        )
        self.root.ids.box.add_widget(Num)

        NOS = MDExpansionPanel(
            content=Numerical_Op(),
            panel_cls=MDExpansionPanelOneLine(
                text=" +,   - ,  *,  ^,  √ ,   ... "
            )
        )

        self.root.ids.vox.add_widget(NOS)

        TRIG = MDExpansionPanel(
            content=Trig_Func(),
            panel_cls=MDExpansionPanelOneLine(
                text="sin,  cos,  tan, ..."))
        self.root.ids.hike.add_widget(TRIG)

        ADVANCED = MDExpansionPanel(
            content=Advanced(),
            panel_cls=MDExpansionPanelOneLine(
                text="Advanced Functions"))
        self.root.ids.tin.add_widget(ADVANCED)

        MATRIX = MDExpansionPanel(
            content=Matrix(),
            panel_cls=MDExpansionPanelOneLine(
                text="Matrix Input"))
        self.root.ids.mat.add_widget(MATRIX)

        QUADRATIC = MDExpansionPanel(
            content=Quadratic(),
            panel_cls=MDExpansionPanelOneLine(
                text="Quadratic x² ± x ± c  input"))
        self.root.ids.quad.add_widget(QUADRATIC)

        SIMULTANEOUS = MDExpansionPanel(
            content=Simultaneous(),
            panel_cls=MDExpansionPanelOneLine(
                text="Simultaneous eqn Input field"))
        self.root.ids.simulate.add_widget(SIMULTANEOUS)




    def Home(self):
        self.root.ids.manager.current = "main"

    #####################
    #####################
    ####### Numbers

    def one(self):
        try:
            prior = self.root.ids.textinput.text
            i = self.root.ids.textinput.cursor[0] - 1
            if prior == "0" or prior == "Math Error":
                self.root.ids.textinput.text = "1"

            elif prior[i] == ")":
                self.root.ids.textinput.insert_text("*1")

            else:
                self.root.ids.textinput.insert_text("1")
        except:
            pass

    def two(self):
        try:
            prior = self.root.ids.textinput.text
            i = self.root.ids.textinput.cursor[0] - 1

            if prior == "0" or prior == "Math Error":
                self.root.ids.textinput.text = "2"

            elif prior[i] == ")":
                self.root.ids.textinput.insert_text("*2")

            else:
                self.root.ids.textinput.insert_text("2")
        except:
            pass

    def three(self):
        try:
            prior = self.root.ids.textinput.text
            i = self.root.ids.textinput.cursor[0] - 1
            if prior == "0" or prior == "Math Error":
                self.root.ids.textinput.text = "3"

            elif prior[i] == ")":
                self.root.ids.textinput.insert_text("*3")

            else:
                self.root.ids.textinput.insert_text("3")
        except:
            pass

    def four(self):
        try:
            prior = self.root.ids.textinput.text
            i = self.root.ids.textinput.cursor[0] - 1
            if prior == "0" or prior == "Math Error":
                self.root.ids.textinput.text = "4"

            elif prior[i] == ")":
                self.root.ids.textinput.insert_text("*4")

            else:
                self.root.ids.textinput.insert_text("4")
        except:
            pass

    def five(self):
        try:
            prior = self.root.ids.textinput.text
            i = self.root.ids.textinput.cursor[0] - 1
            if prior == "0" or prior == "Math Error":
                self.root.ids.textinput.text = "5"

            elif prior[i] == ")":
                self.root.ids.textinput.insert_text("*5")

            else:
                self.root.ids.textinput.insert_text("5")
        except:
            pass

    def six(self):
        try:
            prior = self.root.ids.textinput.text
            i = self.root.ids.textinput.cursor[0] - 1
            if prior == "0" or prior == "Math Error":
                self.root.ids.textinput.text = "6"

            elif prior[i] == ")":
                self.root.ids.textinput.insert_text("*6")

            else:
                self.root.ids.textinput.insert_text("6")
        except:
            pass

    def seven(self):
        try:
            prior = self.root.ids.textinput.text
            i = self.root.ids.textinput.cursor[0] - 1
            if prior == "0" or prior == "Math Error":
                self.root.ids.textinput.text = "7"

            elif prior[i] == ")":
                self.root.ids.textinput.insert_text("*7")


            else:
                self.root.ids.textinput.insert_text("7")
        except:
            pass

    def eight(self):
        try:
            prior = self.root.ids.textinput.text
            i = self.root.ids.textinput.cursor[0] - 1
            if prior == "0" or prior == "Math Error":
                self.root.ids.textinput.text = "8"

            elif prior[i] == ")":
                self.root.ids.textinput.insert_text("*8")

            else:
                self.root.ids.textinput.insert_text("8")
        except:
            pass

    def nine(self):
        try:
            prior = self.root.ids.textinput.text
            i = self.root.ids.textinput.cursor[0] - 1
            if prior == "0" or prior == "Math Error":
                self.root.ids.textinput.text = "9"

            elif prior[i] == ")":
                self.root.ids.textinput.insert_text("*9")

            else:
                self.root.ids.textinput.insert_text("9")
        except:
            pass

    def zero(self):
        try:
            prior = self.root.ids.textinput.text
            i = self.root.ids.textinput.cursor[0] - 1
            if prior == "0" or prior == "Math Error":
                pass

            else:
                self.root.ids.textinput.insert_text("0")
        except:
            pass

    def dot(self):
        try:
            prior = self.root.ids.textinput.text
            i = self.root.ids.textinput.cursor[0] - 1
            if prior == "Math Error":
                pass

            else:
                self.root.ids.textinput.insert_text(".")
        except:
            pass

    def coma(self):
        try:
            prior = self.root.ids.textinput.text
            i = self.root.ids.textinput.cursor[0] - 1
            if prior == "Math Error":
                pass

            elif "log" in prior:
                self.root.ids.textinput.insert_text(",")
        except:
            pass

    def space(self):
        try:
            prior = self.root.ids.textinput.text
            i = self.root.ids.textinput.cursor[0] - 1
            if prior == "Math Error":
                pass
            else:

                self.root.ids.textinput.insert_text(" ")
        except:
            pass

    def clear(self):
        try:
            prior = self.root.ids.textinput.text
            self.root.ids.textinput.text = "0"
        except:
            pass

    def delete(self):
        try:
            prior = self.root.ids.textinput.text
            self.root.ids.textinput.text = prior[:-1]
        except:
            pass

    def answer(self):
        try:
            answer = self.ans_list[-1]
            prior = self.root.ids.textinput.text
            self.root.ids.textinput.insert_text(f"{str(answer)}")
        except:
            pass

    #####################################
    ###################################
    ########### EQUALS ####################

    def equals(self):

        self.ans_list = []
        prior = self.root.ids.textinput.text
        try:
            prior1 = prior.replace("π", "math.pi")
            prior2 = prior1.replace("^", "**")
            prior3 = prior2.replace("√(", "math.sqrt(")
            prior4 = prior3.replace("sin(r(", "math.sin(math.radians(")
            prior5 = prior4.replace("cos(r(", "math.cos(math.radians(")
            prior6 = prior5.replace("tan(r(", "math.tan(math.radians(")
            prior7 = prior6.replace("d(asin(", "math.degrees(math.asin(")
            prior8 = prior7.replace("d(acos(", "math.degrees(math.acos(")
            prior9 = prior8.replace("d(atan(", "math.degrees(math.atan(")
            prior9 = prior9.replace("exp(", "math.exp(")
            prior10 = prior9.replace("log", "np.log")
            prior10 = prior10.replace("!(", "math.factorial(")
            prior11 = prior10.replace("',", "")
            prior12 = prior11.replace(" ", "")
            prior13 = prior12.replace("÷", "/")

            Sum = eval(prior13)
            self.ans_list.append(Sum)
            self.root.ids.result.text = str(Sum)
            # speech(self.root.ids.textinput.text+"equals", "en")
            # speech(str(Sum), "en")

            History = TwoLineListItem(text=str(prior), secondary_text=(str(Sum)))
            self.root.ids.history_list.add_widget(History)


        except:
            self.root.ids.textinput.text = "Math Error"

    def left_bracket(self):
        try:
            prior = self.root.ids.textinput.text

            if prior == "Math Error" or prior == "0":
                self.root.ids.textinput.text = "("

            elif type(eval(prior[-1])) == int:
                self.root.ids.textinput.insert_text("*(")


            else:
                self.root.ids.textinput.insert_text("(")
        except:
            pass

    def right_bracket(self):
        try:
            prior = self.root.ids.textinput.text

            if prior == "Math Error" or prior == "0":
                self.root.ids.textinput.text = ")"

            else:
                self.root.ids.textinput.insert_text(")")
        except:
            pass

    def divide(self):
        try:
            prior = self.root.ids.textinput.text

            if prior == "Math Error":
                self.root.ids.textinput.text = "÷"

            else:
                self.root.ids.textinput.insert_text("÷")
        except:
            pass

    def addition(self):
        try:
            prior = self.root.ids.textinput.text

            if prior == "Math Error" or prior == "0":
                self.root.ids.textinput.text = "+"

            else:
                self.root.ids.textinput.insert_text("+")
        except:
            pass

    def multiply(self):
        try:
            prior = self.root.ids.textinput.text

            if prior == "Math Error":
                self.root.ids.textinput.text = "*"

            else:
                self.root.ids.textinput.insert_text("*")
        except:
            pass

    def subtract(self):
        try:
            prior = self.root.ids.textinput.text

            if prior == "Math Error" or prior == "0":
                self.root.ids.textinput.text = "-"

            else:
                self.root.ids.textinput.insert_text("-")
        except:
            pass

    def square_root(self):
        try:
            prior = self.root.ids.textinput.text

            if prior == "Math Error" or prior == "0":
                self.root.ids.textinput.text = "√("

            else:
                self.root.ids.textinput.insert_text("√(")
        except:
            pass

    def power(self):
        try:
            prior = self.root.ids.textinput.text

            if prior == "Math Error":
                self.root.ids.textinput.text = "^"

            else:
                self.root.ids.textinput.insert_text("^")
        except:
            pass

    def Pi(self):
        try:
            prior = self.root.ids.textinput.text

            if prior == "Math Error" or prior == "0":
                self.root.ids.textinput.text = "π"

            else:
                self.root.ids.textinput.insert_text("π")
        except:
            pass

    ###################################
    ########### Trigonometry input #########

    def Sin(self):
        try:
            prior = self.root.ids.textinput.text

            if prior == "Math Error" or prior == "0":
                self.root.ids.textinput.text = "sin(r("

            elif prior[-1] == ")":
                self.root.ids.textinput.insert_text("*sin(r(")

            elif prior[-1] == "+" or prior[-1] == "-" or prior[-1] == "÷" or prior[-1] == "*" or prior[-1] == "^" or \
                    prior[
                        -1] == "(":
                self.root.ids.textinput.insert_text("sin(r(")

            elif prior[-1] != "0" and type(eval(prior[-1])) == int:
                self.root.ids.textinput.insert_text("*sin(r(")

            else:
                self.root.ids.textinput.insert_text("sin(r(")
        except:
            pass

    def Cos(self):
        try:
            prior = self.root.ids.textinput.text

            if prior == "Math Error" or prior == "0":
                self.root.ids.textinput.text = "cos(r("


            elif prior[-1] == ")":
                self.root.ids.textinput.insert_text("*cos(r(")


            elif prior[-1] == "+" or prior[-1] == "-" or prior[-1] == "÷" or prior[-1] == "*" or prior[-1] == "^" or \
                    prior[
                        -1] == "(":
                self.root.ids.textinput.insert_text("cos(r(")


            elif type(eval(prior[-1])) == int and prior != "0":
                self.root.ids.textinput.insert_text("*cos(r(")


            else:
                self.root.ids.textinput.insert_text("cos(r(")
        except:
            pass

    def Tan(self):
        try:
            prior = self.root.ids.textinput.text

            if prior == "Math Error":
                self.root.ids.textinput.text = "tan(r("


            elif prior[-1] == ")":
                self.root.ids.textinput.insert_text("*tan(r(")


            elif prior[-1] == "+" or prior[-1] == "-" or prior[-1] == "÷" or prior[-1] == "*" or prior[-1] == "^" or \
                    prior[
                        -1] == "(":
                self.root.ids.textinput.insert_text("tan(r(")


            elif type(eval(prior[-1])) == int and prior != "0":
                self.root.ids.textinput.insert_text("*tan(r(")


            else:
                self.root.ids.textinput.insert_text("tan(r(")
        except:
            pass

    def ASin(self):
        try:
            prior = self.root.ids.textinput.text

            if prior == "Math Error":
                self.root.ids.textinput.text = "d(asin("

            elif prior[-1] == ")":
                self.root.ids.textinput.insert_text("*d(sin(")


            elif prior[-1] == "+" or prior[-1] == "-" or prior[-1] == "÷" or prior[-1] == "*" or prior[-1] == "^" or \
                    prior[
                        -1] == "(":
                self.root.ids.textinput.insert_text("d(asin(")


            elif type(eval(prior[-1])) == int and prior != "0":
                self.root.ids.textinput.insert_text("*d(asin(")


            else:
                self.root.ids.textinput.insert_text("d(asin(")
        except:
            pass

    def ACos(self):
        try:
            prior = self.root.ids.textinput.text

            if prior == "Math Error":
                self.root.ids.textinput.text = "d(acos("

            elif prior[-1] == ")":
                self.root.ids.textinput.insert_text("*d(acos(")

            elif prior[-1] == "+" or prior[-1] == "-" or prior[-1] == "÷" or prior[-1] == "*" or prior[-1] == "^" or \
                    prior[
                        -1] == "(":
                self.root.ids.textinput.insert_text("d(acos(")


            elif type(eval(prior[-1])) == int and prior != "0":
                self.root.ids.textinput.insert_text("*d(acos(")


            else:
                self.root.ids.textinput.insert_text("d(acos(")
        except:
            pass

    def ATan(self):
        try:
            prior = self.root.ids.textinput.text

            if prior == "Math Error":
                self.root.ids.textinput.text = "d(atan("


            elif prior[-1] == ")":
                self.root.ids.textinput.insert_text("*d(atan(")

            elif prior[-1] == "+" or prior[-1] == "-" or prior[-1] == "÷" or prior[-1] == "*" or prior[-1] == "^" or \
                    prior[
                        -1] == "(":

                self.root.ids.textinput.insert_text("d(atan(")

            elif type(eval(prior[-1])) == int and prior != "0":
                self.root.ids.textinput.insert_text("*d(atan(")

            else:
                self.root.ids.textinput.insert_text("d(atan(")
        except:
            pass

    ##################################
    ########## Advanced Functions ########

    def Log(self):
        try:
            prior = self.root.ids.textinput.text
            if prior == "0" or prior == "Math Error":
                self.root.ids.textinput.text = "logb(x)"

            elif prior[-1] == ")":
                self.root.ids.textinput.insert_text("*logb(x)")

            else:
                self.root.ids.textinput.insert_text("logb(x)")
        except:
            pass

    def Antilog(self):
        try:
            prior = self.root.ids.textinput.text
            if prior == "0" or prior == "Math Error":
                self.root.ids.textinput.text = "b^a"

            elif prior[-1] == ")":
                self.root.ids.textinput.insert_text("*b^a")

            else:
                self.root.ids.textinput.insert_text("b^a")
        except:
            pass

    def Factorial(self):
        try:
            prior = self.root.ids.textinput.text
            if prior == "0" or prior == "Math Error":
                self.root.ids.textinput.text = ("!(")

            elif prior[-1] == ")":
                self.root.ids.textinput.insert_text("*!(")
            else:
                self.root.ids.textinput.insert_text("!(")
        except:
            pass

    def Exponential(self):
        try:
            prior = self.root.ids.textinput.text
            if prior == "0" or prior == "Math Error":
                self.root.ids.textinput.text = ("exp(")

            elif prior[-1] == ")":
                self.root.ids.textinput.insert_text("*exp(")
            else:
                self.root.ids.textinput.insert_text("exp(")
        except:
            pass

    ######################################
    ########## matrix 1 input    ##############

    def m_one(self):
        try:
            prior = self.root.ids.uix.text
            if prior == "0" or prior == "Math Error":
                self.root.ids.uix.text = "1"

            else:
                self.root.ids.uix.insert_text("1")
        except:
            pass

    def m_two(self):
        try:
            prior = self.root.ids.uix.text
            if prior == "0" or prior == "Math Error":
                self.root.ids.uix.text = "2"

            else:
                self.root.ids.uix.insert_text("2")
        except:
            pass

    def m_three(self):
        try:
            prior = self.root.ids.uix.text
            if prior == "0" or prior == "Math Error":
                self.root.ids.uix.text = "3"

            else:
                self.root.ids.uix.insert_text("3")
        except:
            pass

    def m_four(self):
        try:
            prior = self.root.ids.uix.text
            if prior == "0" or prior == "Math Error":
                self.root.ids.uix.text = "4"

            else:
                self.root.ids.uix.insert_text("4")
        except:
            pass

    def m_five(self):
        try:
            prior = self.root.ids.uix.text
            if prior == "0" or prior == "Math Error":
                self.root.ids.uix.text = "5"

            else:
                self.root.ids.uix.insert_text("5")
        except:
            pass

    def m_six(self):
        try:
            prior = self.root.ids.uix.text
            if prior == "0" or prior == "Math Error":
                self.root.ids.uix.text = "6"

            else:
                self.root.ids.uix.insert_text("6")
        except:
            pass

    def m_seven(self):
        try:
            prior = self.root.ids.uix.text
            if prior == "0" or prior == "Math Error":
                self.root.ids.uix.text = "7"

            else:
                self.root.ids.uix.insert_text("7")
        except:
            pass

    def m_eight(self):
        try:
            prior = self.root.ids.uix.text
            if prior == "0" or prior == "Math Error":
                self.root.ids.uix.text = "8"

            else:
                self.root.ids.uix.insert_text("8")
        except:
            pass

    def m_nine(self):
        try:
            prior = self.root.ids.uix.text
            if prior == "0" or prior == "Math Error":
                self.root.ids.uix.text = "9"

            else:
                self.root.ids.uix.insert_text("9")
        except:
            pass

    def m_zero(self):
        try:
            prior = self.root.ids.uix.text
            if prior == "0" or prior == "Math Error":
                pass

            else:
                self.root.ids.uix.insert_text("0")
        except:
            pass

    def m_dot(self):
        try:
            prior = self.root.ids.uix.text
            if prior == "Math Error":
                pass

            else:
                self.root.ids.uix.insert_text(".")
        except:
            pass

    def m_coma(self):
        try:
            prior = self.root.ids.uix.text
            if prior == "Math Error":
                pass

            else:
                self.root.ids.uix.insert_text(",")
        except:
            pass

    def m_space(self):
        try:
            prior = self.root.ids.uix.text

            if prior == "Math Error":
                pass
            else:

                self.root.ids.uix.insert_text(" ")
        except:
            pass

    def m_clear(self):
        try:
            self.root.ids.uix.text = ""
        except:
            pass

    def m_delete(self):
        try:
            prior = self.root.ids.uix.text
            self.root.ids.uix.text = prior[:-1]
        except:
            pass

    def m_l_bracket(self):
        try:
            self.root.ids.uix.insert_text(" { ")
        except:
            pass

    def m_r_bracket(self):
        try:
            self.root.ids.uix.insert_text(" } ")
        except:
            pass

    def m_det(self):

        prior = self.root.ids.uix.text
        prior1 = prior.replace("{", "[")
        prior2 = prior1.replace("}", "]")
        prior3 = prior2.replace(" ", "")

        try:

            prior4 = ast.literal_eval(prior3)

            prior5 = np.linalg.det(prior4)

            self.root.ids.uix.text = f"\n{prior2} \n \n Determinat M1 = {str(prior5)}"
            History = TwoLineListItem(text=str(prior), secondary_text=(str(prior5)))
            self.root.ids.history_list.add_widget(History)

        except:

            self.root.ids.uix.text = "enter a valid square matrix"

    #####################################
    ########## matrix 2 input   #############

    def m2_one(self):
        try:
            prior = self.root.ids.uix2.text
            if prior == "0" or prior == "Math Error":
                self.root.ids.uix2.text = "1"

            else:
                self.root.ids.uix2.insert_text("1")
        except:
            pass

    def m2_two(self):
        try:
            prior = self.root.ids.uix2.text
            if prior == "0" or prior == "Math Error":
                self.root.ids.uix2.text = "2"

            else:
                self.root.ids.uix2.insert_text("2")
        except:
            pass

    def m2_three(self):
        try:
            prior = self.root.ids.uix2.text
            if prior == "0" or prior == "Math Error":
                self.root.ids.uix2.text = "3"

            else:
                self.root.ids.uix2.insert_text("3")
        except:
            pass

    def m2_four(self):
        try:
            prior = self.root.ids.uix2.text
            if prior == "0" or prior == "Math Error":
                self.root.ids.uix2.text = "4"

            else:
                self.root.ids.uix2.insert_text("4")
        except:
            pass

    def m2_five(self):
        try:
            prior = self.root.ids.uix2.text
            if prior == "0" or prior == "Math Error":
                self.root.ids.uix2.text = "5"

            else:
                self.root.ids.uix2.insert_text("5")
        except:
            pass

    def m2_six(self):
        try:
            prior = self.root.ids.uix2.text
            if prior == "0" or prior == "Math Error":
                self.root.ids.uix2.text = "6"

            else:
                self.root.ids.uix2.insert_text("6")
        except:
            pass

    def m2_seven(self):
        try:
            prior = self.root.ids.uix2.text
            if prior == "0" or prior == "Math Error":
                self.root.ids.uix2.text = "7"

            else:
                self.root.ids.uix2.insert_text("7")
        except:
            pass

    def m2_eight(self):
        try:
            prior = self.root.ids.uix2.text
            if prior == "0" or prior == "Math Error":
                self.root.ids.uix2.text = "8"

            else:
                self.root.ids.uix2.insert_text("8")
        except:
            pass

    def m2_nine(self):
        try:
            prior = self.root.ids.uix2.text
            if prior == "0" or prior == "Math Error":
                self.root.ids.uix2.text = "9"

            else:
                self.root.ids.uix2.insert_text("9")
        except:
            pass

    def m2_zero(self):
        try:
            prior = self.root.ids.uix2.text
            if prior == "0" or prior == "Math Error":
                pass

            else:
                self.root.ids.uix2.insert_text("0")
        except:
            pass

    def m2_dot(self):
        try:
            prior = self.root.ids.uix2.text
            if prior == "Math Error":
                pass

            else:
                self.root.ids.uix2.insert_text(".")
        except:
            pass

    def m2_coma(self):
        try:
            prior = self.root.ids.uix2.text
            if prior == "Math Error":
                pass

            else:
                self.root.ids.uix2.insert_text(",")
        except:
            pass

    def m2_space(self):
        try:
            prior = self.root.ids.uix2.text

            if prior == "Math Error":
                pass
            else:
                self.root.ids.uix2.insert_text(" ")
        except:
            pass

    def m2_clear(self):
        try:
            self.root.ids.uix2.text = ""
        except:
            pass

    def m2_delete(self):
        try:
            prior = self.root.ids.uix2.text
            self.root.ids.uix2.text = prior[:-1]
        except:
            pass

    def m2_l_bracket(self):
        try:
            self.root.ids.uix2.insert_text(" { ")
        except:
            pass

    def m2_r_bracket(self):
        try:
            self.root.ids.uix2.insert_text(" } ")
        except:
            pass

    def m2_det(self):

        prior = self.root.ids.uix2.text
        prior = prior.replace("{", "[")
        prior = prior.replace("}", "]")
        prior = prior.replace(" ", "")

        try:

            prior = ast.literal_eval(prior)

            prior1 = np.linalg.det(prior)

            self.root.ids.uix2.text = f"\n{prior} \n \n Determinat M1 = {prior1}"
            History = TwoLineListItem(text=str(prior), secondary_text=(str(prior1)))
            self.root.ids.history_list.add_widget(History)

        except:

            self.root.ids.uix2.text = "enter a valid square matrix"

    ########################################
    ############ matrix m1 and m2 operations #######

    def matrix_multiply(self):
        priorx1 = self.root.ids.uix.text
        priorx2 = priorx1.replace("{", "[")
        priorx3 = priorx2.replace("}", "]")
        priorx4 = priorx3.replace(" ", "")

        priory1 = self.root.ids.uix2.text
        priory2 = priory1.replace("{", "[")
        priory3 = priory2.replace("}", "]")
        priory4 = priory3.replace(" ", "")
        try:
            m1 = np.array(ast.literal_eval(priorx4))
            m2 = np.array(ast.literal_eval(priory4))
            prior = m1.dot(m2)
            self.root.ids.textinput.text = f" M1 * M2  \n {str(prior)}"
            History = TwoLineListItem(text=str(m1 * m2), secondary_text=(str(prior)))
            self.root.ids.history_list.add_widget(History)
        except:
            self.root.ids.textinput.text = "Enter a valid matrix "

    def matrix_addition(self):
        priorx1 = self.root.ids.uix.text
        priorx2 = priorx1.replace("{", "[")
        priorx3 = priorx2.replace("}", "]")
        priorx4 = priorx3.replace(" ", "")

        priory1 = self.root.ids.uix2.text
        priory2 = priory1.replace("{", "[")
        priory3 = priory2.replace("}", "]")
        priory4 = priory3.replace(" ", "")
        try:
            m1 = np.array(ast.literal_eval(priorx4))
            m2 = np.array(ast.literal_eval(priory4))
            prior = m1 + m2
            self.root.ids.textinput.text = f" M1 + M2  \n {str(prior)}"
            History = TwoLineListItem(text=str(m1 + m2), secondary_text=(str(prior)))
            self.root.ids.history_list.add_widget(History)
        except:
            self.root.ids.textinput.text = "Enter a valid matrix "

    def matrix_subtraction(self):
        priorx1 = self.root.ids.uix.text
        priorx2 = priorx1.replace("{", "[")
        priorx3 = priorx2.replace("}", "]")
        priorx4 = priorx3.replace(" ", "")

        priory1 = self.root.ids.uix2.text
        priory2 = priory1.replace("{", "[")
        priory3 = priory2.replace("}", "]")
        priory4 = priory3.replace(" ", "")
        try:
            m1 = np.array(ast.literal_eval(priorx4))
            m2 = np.array(ast.literal_eval(priory4))
            prior = m1 - m2
            self.root.ids.textinput.text = f" M1 - M2  \n {str(prior)}"
            History = TwoLineListItem(text=str(m1 - m2), secondary_text=(str(prior)))
            self.root.ids.history_list.add_widget(History)
        except:
            self.root.ids.textinput.text = "Enter a valid matrix "

    ################################
    ################################
    ######### Quadratic Input Buttons #####

    def q_one(self):
        try:
            self.root.ids.quadin.insert_text("1")
        except:
            pass

    def q_two(self):
        try:
            self.root.ids.quadin.insert_text("2")
        except:
            pass

    def q_three(self):
        try:
            self.root.ids.quadin.insert_text("3")
        except:
            pass

    def q_four(self):
        try:
            self.root.ids.quadin.insert_text("4")
        except:
            pass

    def q_five(self):
        try:
            self.root.ids.quadin.insert_text("5")
        except:
            pass

    def q_six(self):
        try:
            self.root.ids.quadin.insert_text("6")
        except:
            pass

    def q_seven(self):
        try:
            self.root.ids.quadin.insert_text("7")
        except:
            pass

    def q_eight(self):
        try:
            self.root.ids.quadin.insert_text("8")
        except:
            pass

    def q_nine(self):
        try:
            self.root.ids.quadin.insert_text("9")
        except:
            pass

    def q_zero(self):
        try:
            self.root.ids.quadin.insert_text("0")
        except:
            pass

    def q_dot(self):
        try:
            self.root.ids.quadin.insert_text(".")
        except:
            pass

    def q_coma(self):
        try:
            self.root.ids.quadin.insert_text(",")
        except:
            pass

    def q_x_power(self):
        try:
            self.root.ids.quadin.insert_text("x²")
        except:
            pass

    def q_delete(self):
        try:
            prior = self.root.ids.quadin.text
            self.root.ids.quadin.text = prior[:-1]
        except:
            pass

    def q_clear(self):
        try:
            self.root.ids.quadin.text = ""
        except:
            pass

    def q_x(self):
        try:
            self.root.ids.quadin.insert_text("X")
        except:
            pass

    def q_plus(self):
        try:
            self.root.ids.quadin.insert_text(" + ")
        except:
            pass

    def q_subtract(self):
        try:
            self.root.ids.quadin.insert_text(" - ")
        except:
            pass

    def q_equals(self):
        prior = self.root.ids.quadin.text

        try:
            c = []
            hint = self.root.ids.quadin.text
            h = hint.index("X")

            if hint[h - 1] == " ":
                hint = hint.replace("X", "1X")

            if hint[0] == "x" or hint[0] == "-":
                hint = hint.replace("x²", "1x²")
                hint = hint.replace("x2", "1x2")

            if hint[-1] == "X" or hint[-2] == "X":
                hint = hint.replace("X", "X + 0")
            hint = hint.replace("x²", "")
            hint = hint.replace("x2", "")
            hint = hint.replace("X", "")
            hint = hint.split(" ")
            px = 0
            py = 0

            for i in hint:
                if i != "":
                    c.append(i)
            hinta = c[0]
            hintb = c[2]
            hintc = c[4]

            if c[1] == "+" and c[3] == "+":
                a = eval(hinta)
                b = eval(hintb)
                c = eval(hintc)
                px = (-b + np.sqrt(b * b - (4 * a * c))) / (2 * a)
                py = (-b - np.sqrt(b * b - (4 * a * c))) / (2 * a)
                self.root.ids.quadin.text = f"{Fraction(prior)} \n \n x = {Fraction(px)} or \nx = {Fraction(py)}"

            elif c[1] == "+" and c[3] == "-":
                a = eval(hinta)
                b = eval(hintb)
                c = -eval(hintc)
                px = (-b + np.sqrt(b * b - (4 * a * c))) / (2 * a)
                py = (-b - np.sqrt(b * b - (4 * a * c))) / (2 * a)
                self.root.ids.quadin.text = f"{prior} \n \n x = {px} or \nx = {py}"

            elif c[1] == "-" and c[3] == "+":
                a = eval(hinta)
                b = -eval(hintb)
                c = eval(hintc)
                px = (-b + np.sqrt(b * b - (4 * a * c))) / (2 * a)
                py = (-b - np.sqrt(b * b - (4 * a * c))) / (2 * a)
                self.root.ids.quadin.text = f"{prior} \n \n x = {px} or \nx = {py}"

            elif c[1] == "-" and c[3] == "-":
                a = eval(hinta)
                b = -eval(hintb)
                c = -eval(hintc)
                px = (-b + np.sqrt(b * b - (4 * a * c))) / (2 * a)
                py = (-b - np.sqrt(b * b - (4 * a * c))) / (2 * a)
                self.root.ids.quadin.text = f"{prior} \n \n  x = {px} or \nx = {py}"

            History = TwoLineListItem(text=str(prior), secondary_text=(f"x = {px} or x = {py}"))
            self.root.ids.history_list.add_widget(History)

        except:
            self.root.ids.quadin.text = "Enter a valid quadratic equation of power '²' "

    #####################################
    #####################################
    ########## simulataneous equation input ######

    def s_v(self):
        try:
            self.root.ids.simulate1.insert_text("v")
        except:
            pass

    def s_x(self):
        try:
            self.root.ids.simulate1.insert_text("x")
        except:
            pass

    def s_y(self):
        try:
            self.root.ids.simulate1.insert_text("y")
        except:
            pass

    def s_z(self):
        try:
            self.root.ids.simulate1.insert_text("z")
        except:
            pass

    def s_k(self):
        try:
            self.root.ids.simulate1.insert_text("k")
        except:
            pass

    def s_l_bracket(self):
        try:
            self.root.ids.simulate1.insert_text("{ ")
        except:
            pass

    def s_r_bracket(self):
        try:
            self.root.ids.simulate1.insert_text(" } ")
        except:
            pass

    def s_zero(self):
        try:
            self.root.ids.simulate1.insert_text("0")
        except:
            pass

    def s_one(self):
        try:
            self.root.ids.simulate1.insert_text("1")
        except:
            pass

    def s_two(self):
        try:
            self.root.ids.simulate1.insert_text("2")
        except:
            pass

    def s_three(self):
        try:
            self.root.ids.simulate1.insert_text("3")
        except:
            pass

    def s_four(self):
        try:
            self.root.ids.simulate1.insert_text("4")
        except:
            pass

    def s_five(self):
        try:
            self.root.ids.simulate1.insert_text("5")
        except:
            pass

    def s_six(self):
        try:
            self.root.ids.simulate1.insert_text("6")
        except:
            pass

    def s_seven(self):
        try:
            self.root.ids.simulate1.insert_text("7")
        except:
            pass

    def s_eight(self):
        try:
            self.root.ids.simulate1.insert_text("8")
        except:
            pass

    def s_nine(self):
        try:
            self.root.ids.simulate1.insert_text("9")
        except:
            pass

    def s_plus(self):
        try:
            self.root.ids.simulate1.insert_text(" + ")
        except:
            pass

    def s_minus(self):
        try:
            self.root.ids.simulate1.insert_text(" - ")
        except:
            pass

    def s_dot(self):
        try:
            self.root.ids.simulate1.insert_text(".")
        except:
            pass

    def s_coma(self):
        try:
            self.root.ids.simulate1.insert_text(" , ")
        except:
            pass

    def s_clear(self):
        try:
            self.root.ids.simulate1.text = ""
        except:
            pass

    def s_delete(self):
        try:
            prior = self.root.ids.simulate1.text
            self.root.ids.simulate1.text = prior[:-1]
        except:
            pass

    #####################################
    #####################################
    ###### simultaneous equals ################

    def s_equals(self):
        prior = self.root.ids.simulate1.text

        try:
            prior = prior.replace("v", "")
            prior = prior.replace("x", "")
            prior = prior.replace("y", "")
            prior = prior.replace("z", "")
            prior = prior.replace("k", "")
            prior = prior.replace("{", "[")
            prior = prior.replace("}", "]")
            prior = prior.replace(" ", "")

            prior1 = ast.literal_eval(prior)

            prior2 = prior1[:-1]

            prior3 = prior1[-1]

            result = np.linalg.inv(prior2).dot(prior3)

            Length = len(prior2) - 1

            self.root.ids.simulate1.text = str(result)

            History = TwoLineListItem(text=str(prior), secondary_text=(str(result)))
            self.root.ids.history_list.add_widget(History)



        except:
            self.root.ids.simulate1.text = "check input order and try again"

    def delete_history(self):
        try:
            self.root.ids.history_list.clear_widgets()
        except:
            pass


Test().run()

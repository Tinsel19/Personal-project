from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import Clock
from kvdroid.tools import speech
import math
import numpy as np
import ast

Code = """
MDNavigationLayout:
	ScreenManager:
		Screen:
			MDBoxLayout:
				orientation: "vertical"
				md_bg_color: (.9, .9, .9, 1)
				spacing: dp(10)
				padding: dp(5)
				
				
				
				MDToolbar:
					title: "Calculator"
					specific_text_color: (1, .5, 0, 1)
					elevation: 10
					md_bg_color: (1, 1, 1, 1)
					left_action_items: [["menu" , lambda x: nav_drawer.set_state("toggle")]]
					right_action_items: [["help" ]]
					
					
						
						
				
				TextInput:
					text: "0"
					font_size: dp(40)
					color: (0, 0, 0, 1)
					background_normal: ""
					halign: "right"
					valign: "center"
					padding: dp(20), dp(20)
					size_hint: 1, .25
					id: textinput
					multiline: False
					#input_filter: "int"
					
				TextInput:
					text: "0"
					font_size: dp(60 - (len(self.text)*2))
					md_bg_color: (1, 1, 1, 1)
					halign: "right"
					padding: dp(20), dp(20)
					size_hint: 1, .2
					id: result
					readonly: True
					radius: dp(10)
				
				MDGridLayout:
					cols: 4
					rows: 5
					size_hint: 1, .5
					md_bg_color: (1, 1, 1, .5)
					radius: dp(20)
					
					MDGridLayout:
						rows: 1
						cols: 2
						size_hint: .25, .2
						MDFlatButton:
							text: "√"
							font_size: dp(25)
							size_hint: .5, 1
							on_press: app.square_root()
						
						MDFlatButton:
							text: "^"
							font_size: dp(25)
							size_hint: .5, 1
							on_press: app.power()
					
					
					MDGridLayout:
						rows: 1
						cols: 2
						size_hint: .25, .2
						MDFlatButton:
							text: "("
							font_size: dp(25)
							size_hint: .5, 1
							on_press: app.left_bracket()
						
						MDFlatButton:
							text: ")"
							font_size: dp(25)
							size_hint: .5, 1
							on_press: app.right_bracket()
					
					MDGridLayout:
						rows: 1
						cols: 2
						size_hint: .25, .2
					
						MDFlatButton:
							text: "C"
							font_size: dp(25)
							size_hint: .5, .1
							on_press: app.clear()
						
						MDFlatButton:
							text: "del"
							font_size: dp(20)
							size_hint: .5, .1
							on_press: app.delete()
					
					MDFlatButton:
						text: "÷"
						font_size: dp(25)
						size_hint: .25, .2
						on_press: app.divide()
					
					MDFlatButton:
						text: "7"
						font_size: dp(25)
						size_hint: .25, .2
						on_press: app.seven()
					
					MDFlatButton:
						text: "8"
						font_size: dp(25)
						size_hint: .25, .2
						on_press: app.eight()
					
					MDFlatButton:
						text: "9"
						font_size: dp(25)
						size_hint: .25, .2
						on_press: app.nine()
					
					MDFlatButton:
						text: "*"
						font_size: dp(25)
						size_hint: .25, .2
						on_press: app.multiply()
					
					MDFlatButton:
						text: "4"
						font_size: dp(25)
						size_hint: .25, .2
						on_press: app.four()
					
					MDFlatButton:
						text: "5"
						font_size: dp(25)
						size_hint: .25, .2
						on_press: app.five()
					
					MDFlatButton:
						text: "6"
						font_size: dp(25)
						size_hint: .25, .2
						on_press: app.six()
					
					MDFlatButton:
						text: "+"
						font_size: dp(25)
						size_hint: .25, .2
						on_press: app.addition()
					
					MDFlatButton:
						text: "1"
						font_size: dp(25)
						size_hint: .25, .2
						on_press: app.one()
					
					MDFlatButton:
						text: "2"
						font_size: dp(25)
						size_hint: .25, .2
						on_press: app.two()
					
					MDFlatButton:
						text: "3"
						font_size: dp(25)
						size_hint: .25, .2
						on_press: app.three()
					
					MDFlatButton:
						text: "-"
						font_size: dp(35)
						size_hint: .25, .2
						on_press: app.subtract()
					
					MDFlatButton:
						text: "0"
						font_size: dp(25)
						size_hint: .25, .2
						on_press: app.zero()
					
					MDFlatButton:
						text: "."
						font_size: dp(35)
						size_hint: .25, .2
						on_press: app.dot()
					
					MDFlatButton:
						text: "π"
						font_size: dp(25)
						size_hint: .25, .2
						on_press: app.Pi()
					
					MDFlatButton:
						text: "="
						font_size: dp(25)
						size_hint: .25, .2
						on_press: app.equals()
					
				
	MDNavigationDrawer:
		id: nav_drawer
		MDBoxLayout:
			orientation: "vertical"
			
			ScrollView:
				MDBoxLayout:
					
					orientation: "vertical"
					size_hint: 1, None
					height: self.minimum_height*12
					md_bg_color: (1, 1, 1, .5)
					spacing: dp(10)
					padding: dp(5)

									
					MDBoxLayout:
						orientation: "vertical"	
						MDToolbar:
							title: "matrix"
							specific_text_color: (1, .5, 0, 1)
							md_bg_color:  (1, 1, 1, 1)
							elevation: 10	
						
						MDGridLayout:
							rows: 7
							cols: 1	
							padding: dp(5)
							size_hint: .9, .6
							spacing: dp(10)
							pos_hint: {"center_x": .5, "center_y": .5}
							
								
							TextInput:
								id: M1
								size_hint: 1, .2
								hint_text: "  M1 \\nenter matrix in the format \\n  (a,  b), (c,  d)"
								font_size: dp(12)
								background_normal: ""
								halign: "center"
								canvas.before:
									Color: 
										rgba: 0, 0, 0, 1
									
									Line:
										rectangle: (*self.pos, *self.size)
										
							MDGridLayout:
								cols: 5
								rows: 3
								size_hint: 1, .3
								
								MDFlatButton:
									text: "("
									font_size: dp(10)
									on_press: app.m_l_bracket()
														
								MDFlatButton:
									text: ")"
									font_size: dp(10)
									on_press: app.m_r_bracket()
														
								MDFlatButton:
									text: "1"
									font_size: dp(10)
									on_press: app.m_one()
										
								MDFlatButton:
									text: "2"
									font_size: dp(10)
									on_press: app.m_two()
										
								MDFlatButton:
									text: "3"
									font_size: dp(10)
									on_press: app.m_three()
									
								MDFlatButton:
									text: "4"
									font_size: dp(10)
									on_press: app.m_four()
										
								MDFlatButton:
									text: "5"
									font_size: dp(10)
									on_press: app.m_five()
										
								MDFlatButton:
									text: "6"
									font_size: dp(10)
									on_press: app.m_six()
										
								MDFlatButton:
									text: "7"
									font_size: dp(10)
									on_press: app.m_seven()	
								
								MDFlatButton:
									text: "8"
									font_size: dp(10)
									on_press: app.m_eight()	
								
								MDFlatButton:
									text: "9"
									font_size: dp(10)
									on_press: app.m_nine()	
								
								MDFlatButton:
									text: "0"
									font_size: dp(10)
									on_press: app.m_zero()	
								
								MDFlatButton:
									text: "."
									font_size: dp(20)
									on_press: app.m_dot()	
								
								MDFlatButton:
									text: ","
									font_size: dp(18)
									on_press: app.m_coma()	
								
								MDFlatButton:
									text: "c"
									font_size: dp(10)
									on_press: app.m_clear()	
							
							MDGridLayout:
								rows: 1
								cols: 2
								size_hint: 1, .2
								
								MDFlatButton:
									text: "Transpose M1"
									on_press: app.Transpose1()
								
								MDFlatButton:
									text: "Det M1"
									on_press: app.Determinant1()
								
								
								
							TextInput:
								id: M2
								size_hint: 1, .2
								hint_text: "  M2   \\n enter matrix in the format \\n  (a,  b), (c,  d) "
								font_size: dp(12)
								background_normal: ""
								halign: "center"
								canvas.before:
									Color: 
										rgba: 0, 0, 0, 1
									
									Line:
										rectangle: (*self.pos, *self.size)
							
							MDGridLayout:
								cols: 5
								rows: 3
								size_hint: 1, .3
								
								MDFlatButton:
									text: "("
									font_size: dp(10)
									on_press: app.m2_l_bracket()
														
								MDFlatButton:
									text: ")"
									font_size: dp(10)
									on_press: app.m2_r_bracket()
														
								MDFlatButton:
									text: "1"
									font_size: dp(10)
									on_press: app.m2_one()
										
								MDFlatButton:
									text: "2"
									font_size: dp(10)
									on_press: app.m2_two()
										
								MDFlatButton:
									text: "3"
									font_size: dp(10)
									on_press: app.m2_three()
									
								MDFlatButton:
									text: "4"
									font_size: dp(10)
									on_press: app.m2_four()
										
								MDFlatButton:
									text: "5"
									font_size: dp(10)
									on_press: app.m2_five()
										
								MDFlatButton:
									text: "6"
									font_size: dp(10)
									on_press: app.m2_six()
										
								MDFlatButton:
									text: "7"
									font_size: dp(10)
									on_press: app.m2_seven()	
								
								MDFlatButton:
									text: "8"
									font_size: dp(10)
									on_press: app.m2_eight()	
								
								MDFlatButton:
									text: "9"
									font_size: dp(10)
									on_press: app.m2_nine()	
								
								MDFlatButton:
									text: "0"
									font_size: dp(10)
									on_press: app.m2_zero()	
								
								MDFlatButton:
									text: "."
									font_size: dp(20)
									on_press: app.m2_dot()	
								
								MDFlatButton:
									text: ","
									font_size: dp(18)
									on_press: app.m2_coma()	
								
								MDFlatButton:
									text: "c"
									font_size: dp(10)
									on_press: app.m2_clear()	
							
							MDGridLayout:
								rows: 1
								cols: 2
								size_hint: 1, .2
								
								MDFlatButton:
									text: "Transpose M2"
									on_press: app.Transpose2()
								
								MDFlatButton:
									text: "Det M2"
									on_press: app.Determinant2()
									
							
							MDGridLayout:
								rows: 1
								cols: 3
								size_hint: 1, .2
								
								MDFlatButton:
									text: "M1 + M2"
									on_press: app.Add_Matrix()
								
								MDFlatButton:
									text: "M1 * M2"
									on_press: app.Multiply_Matrix()
								
								MDFlatButton:
									text: "M1 - M2"
									on_press: app.Sub_Matrix()
		
					MDToolbar:
						md_bg_color: (1, 1 , 1, 1)
						elevation: 10
						title: "Advanced Functions"
						specific_text_color: (1, .5, 0, 1)
						
					#ScrollView:
					MDGridLayout:
						size_hint: 1, .4
						#height: dp(800)
						md_bg_color: (1, 1, 1, 1)
							
						cols: 4
						rows: 3
							
						MDFlatButton:
							text: "sin"
							font_size: dp(15)
							size_hint: .25, .2
							on_press: app.Sin()
								
						MDFlatButton:
							text: "cos"
							font_size: dp(15)
							size_hint: .25, .2
							on_press: app.Cos()
								
						MDFlatButton:
							text: "tan"
							font_size: dp(15)
							size_hint: .25, .2
							on_press: app.Tan()
								
						MDFlatButton:
							text: "asin"
							font_size: dp(15)
							size_hint: .25, .2
							on_press: app.ArcSin()
							
							
						MDFlatButton:
							text: "acos"
							font_size: dp(15)
							size_hint: .25, .2
							on_press: app.ArcCos()
								
						MDFlatButton:
							text: "atan"
							font_size: dp(15)
							size_hint: .25, .2
							on_press: app.ArcTan()
								
						MDFlatButton:
							text: "log"
							font_size: dp(15)
							size_hint: .25, .2
							on_press: app.Log()
								
						MDFlatButton:
							text: "alog"
							font_size: dp(15)
							size_hint: .25, .2
							on_press: app.AntiLog()
							
						MDFlatButton:
							text: "dc"
							font_size: dp(15)
							size_hint: .25, .2
							on_press: app.deep_clear()
						
						MDGridLayout:
							rows: 1
							cols: 2
							size_hint: .5, .2
							spacing: dp(5)
							
							MDFlatButton:
								text: " ( "
								font_size: dp(15)
								size_hint: .5, .2
								on_press: app.dot()
								
							MDFlatButton:
								text: " )"
								font_size: dp(15)
								size_hint: .5, .2
								on_press: app.dot()
							
								
						MDFlatButton:
							text: "1"
							font_size: dp(15)
							size_hint: .5, .2
							on_press: app.Pi()
								
						MDFlatButton:
							text: "2"
							font_size: dp(15)
							size_hint: .25, .2
							on_press: app.equals()
							
					
				

						
						
					
		

"""


class CalcApp(MDApp, App):
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		#max_iteration = 8
		
		#Clock.schedule_interval(self.update_result, 60)
		pass

	
	def build(self):
		builder = Builder.load_string(Code)
		
		return builder
		
########################
##### main interface

	def update_result(self, dt):
		prior = self.root.ids.textinput.text
		try:
		
			if "π" in prior:
				pi_prior =prior.replace("π", "math.pi")
				Sum  = eval(pi_prior)
				self.root.ids.result.text = str(Sum)
				
			else:
				Sum  = eval(prior)
				self.root.ids.result.text = str(Sum)
	
		except:
			self.root.ids.textinput.text = "Math Error"
		
		
		
	def square_root(self):
		prior = self.root.ids.textinput.text
		if prior == "0"   or prior =="Math Error":
			self.root.ids.textinput.text = str( "√()")
		
		
		elif prior[-1] == "(√" or "Math Error" in prior:
			pass
		
		else: 
			self.root.ids.textinput.insert_text("√()")
	
	
	
	
	
	def power(self):
		prior = self.root.ids.textinput.text
		if prior == "0"   or prior =="Math Error":
			self.root.ids.textinput.text = str( "^")
		
		
		elif prior[-1] == "^" or "Math Error" in prior:
			pass
		
		else: 
			self.root.ids.textinput.insert_text("^")
			
			
			
			
	
	def left_bracket(self):
		prior = self.root.ids.textinput.text
		if prior == "0"   or prior =="Math Error":
			self.root.ids.textinput.text = str( "(")
		
		
		elif prior[-1] == "(" or "Math Error" in prior:
			pass
		
		else: 
			self.root.ids.textinput.insert_text("(")
		
		
	
	def right_bracket(self):
		prior = self.root.ids.textinput.text
		if prior == "0"   or prior =="Math Error":
			self.root.ids.textinput.text = str( ")")
		
		elif "Math Error" in prior:
			pass
		
		else: 
			self.root.ids.textinput.insert_text(")")
	
	
	
	
	def clear(self):
		self.root.ids.textinput.text = "0"
		#self.root.ids.textinput.background_color = (1, .5, 0, 1)
	
	def deep_clear(self):
		self.root.ids.textinput.text = "0"
		self.root.ids.result.text = "0"
	
	
		
		
	
	
	def divide(self):
		prior = self.root.ids.textinput.text
		if prior == "0"   or prior =="Math Error":
			self.root.ids.textinput.text = str( "/")
		
		
		elif prior[-1] == "/" or  "Math Error" in prior:
			pass
		
		else: 
			self.root.ids.textinput.insert_text("/")
	
	
	
	def seven(self):
		prior = self.root.ids.textinput.text
		if prior == "0"   or prior =="Math Error":
			self.root.ids.textinput.text = str( "7")
		
		
		elif  "Math Error" in prior:
			pass
		
		else: 
			self.root.ids.textinput.insert_text("7")
	
	
	
	
	def eight(self):
		prior = self.root.ids.textinput.text
		if prior == "0"   or prior =="Math Error":
			self.root.ids.textinput.text = str( "8")
		
		
		elif  "Math Error" in prior:
			pass
		
		else: 
			self.root.ids.textinput.insert_text("8")
	
	
	
	def nine(self):
		prior = self.root.ids.textinput.text
		if prior == "0"   or prior =="Math Error":
			self.root.ids.textinput.text = str( "9")
		
		
		elif "Math Error" in prior:
			pass
		
		else: 
			
			self.root.ids.textinput.insert_text("9")
	
	
	
	
	def multiply(self):
		prior = self.root.ids.textinput.text
		if prior == "0"   or prior =="Math Error":
			self.root.ids.textinput.text = str( "*")
		
		
		elif prior[-1] == "*" or  "Math Error" in prior:
			pass
		
		else: 
			self.root.ids.textinput.insert_text("*")
			
			
			
	
	def four(self):
		prior = self.root.ids.textinput.text
		if prior == "0"   or prior =="Math Error":
			self.root.ids.textinput.text = str( "4")
		
		
		elif "Math Error" in prior:
			pass
		
		else: 
			self.root.ids.textinput.insert_text("4")
	
	
	
	def five(self):
		prior = self.root.ids.textinput.text
		if prior == "0"   or prior =="Math Error":
			self.root.ids.textinput.text = str( "5")
		
		
		elif "Math Error" in prior:
			pass
		
		else: 
			self.root.ids.textinput.insert_text("5")
	
	
	
	def six(self):
		prior = self.root.ids.textinput.text
		if prior == "0"   or prior =="Math Error":
			self.root.ids.textinput.text = str( "6")
		
		
		elif "Math Error" in prior:
			pass
		
		else: 
			self.root.ids.textinput.insert_text("6")

	
	
	
	def addition(self):
		prior = self.root.ids.textinput.text
		if prior == "0"   or prior =="Math Error":
			self.root.ids.textinput.text = str( "+")
		
		
		elif prior[-1] == "+" or  "Math Error" in prior:
			pass
		
		else: 
			self.root.ids.textinput.insert_text("+")
			
	
	
	
	def one(self):
		prior = self.root.ids.textinput.text
		if prior == "0"   or prior =="Math Error":
			self.root.ids.textinput.text = str( "1")
		
		
		elif "Math Error" in prior:
			pass
		
		else: 
			self.root.ids.textinput.insert_text("1")
	
	
	
	
	
	def two(self):
		prior = self.root.ids.textinput.text
		if prior == "0"   or prior =="Math Error":
			self.root.ids.textinput.text = str( "2")
		
		
		elif "Math Error" in prior:
			pass
		
		else: 
			self.root.ids.textinput.insert_text("2")
	
	
	
	
	
	def three(self):
		prior = self.root.ids.textinput.text
		if prior == "0"   or prior =="Math Error":
			self.root.ids.textinput.text = str( "3")
		
		
		elif "Math Error" in prior:
			pass
		
		else: 
			self.root.ids.textinput.insert_text("3")
	
	
	
	
	
	
	def subtract(self):
		prior = self.root.ids.textinput.text
		if prior == "0"   or prior =="Math Error":
			self.root.ids.textinput.text = str( "-")
		
		
		elif prior[-1] == "+" or  "Math Error" in prior:
			pass
		
		else: 
			self.root.ids.textinput.insert_text("-")
	
	
	
	
	
	def zero(self):
		prior = self.root.ids.textinput.text
		if prior == "0"   or prior =="Math Error":
			self.root.ids.textinput.text = str( "0")
		
		
		elif "Math Error" in prior:
			pass
		
		else: 
			self.root.ids.textinput.insert_text("0")
	
	
	
	
	
	def dot(self):
		prior = self.root.ids.textinput.text
		#if prior == "0":
		#	self.root.ids.textinput.text = str( ".")
		
		
		if prior[-1] == "." or  "Math Error" in prior:
			pass
		
		else: 
			self.root.ids.textinput.insert_text(".")
		
		
		
		
		
	def Pi(self):
		prior = self.root.ids.textinput.text
		if prior == "0"   or prior =="Math Error":
			self.root.ids.textinput.text = str( "π")
		
		
		elif prior[-1] == "π" or  "Math Error" in prior:
			pass
		
		else: 
			self.root.ids.textinput.insert_text("π")
	

	
	def equals(self):
		prior = self.root.ids.textinput.text
		try:
		
			prior1 = prior.replace("π", "math.pi")
			prior2 = prior1.replace("^", "**")
			prior3 = prior2.replace("√(", "math.sqrt(")
			
			prior4 = prior3.replace("sin(", "math.sin(")
			prior5 = prior4.replace("cos(", "math.cos(")
			prior6 = prior5.replace("tan(", "math.tan(")
			prior7 = prior6.replace("r(", "math.radians(")
			prior8 = prior7.replace("d(", "math.degrees(")
			prior9 = prior8.replace("log", "math.log")
			
				
						
			
			Sum  = eval(prior9)
			self.root.ids.result.text = str(Sum)
			speech(self.root.ids.textinput.text+"equals", "en")
			speech(str(Sum), "en")
			
		
		except:
			self.root.ids.textinput.text = "Math Error"

#####################
#####################
####### toggle interface  

	def Sin(self):
		prior = self.root.ids.textinput.text
		if prior == "0"   or prior =="Math Error":
			self.root.ids.textinput.text = str( "sin(r())")
		
		
		elif  "Math Error" in prior:
			pass
		
		else: 
			self.root.ids.textinput.insert_text("sin(r())")
			
		
		
		
	def Cos(self):
		prior = self.root.ids.textinput.text
		if prior == "0"   or prior =="Math Error":
			self.root.ids.textinput.text = str( "cos(r())")
		
		
		elif "Math Error" in prior:
			pass
		
		else: 
			self.root.ids.textinput.insert_text("cos(r())")
			
			
			
		
	def Tan(self):
		prior = self.root.ids.textinput.text
		if prior == "0" or prior =="Math Error":
			self.root.ids.textinput.text = str( "tan(r())")
		
		
		elif  "Math Error" in prior:
			pass
		
		else: 
			self.root.ids.textinput.insert_text("tan(r())")
			
			

	def delete(self):
		prior = self.root.ids.textinput.text
		prior = prior[:-1]
		self.root.ids.textinput.text = prior
		
	
	def ArcSin(self):
		pass
		
		
	
	def ArcCos(self):
		pass
		
		
	
	def ArcTan(self):
		pass
		
	
	def Log(self):
		prior = self.root.ids.textinput.text
		if prior == "0" or prior =="Math Error":
			self.root.ids.textinput.text = str( "log(x, b)")
		
		
		elif  "Math Error" in prior:
			pass
		
		else: 
			self.root.ids.textinput.insert_text("log(x, b)")
			
	
	
	
	def AntiLog(self):
		pass


#####################
#####################
###### matrix 1


	
	def Transpose1(self):
		
		prior = self.root.ids.M1.text
		
		try:
			
			prior = ast.literal_eval(prior)
			

			prior1 = np.transpose([prior])		
			
			
			self.root.ids.textinput.text = f"  {prior1}"
			
		except:
			self.root.ids.M1.text = "enter a valid square matrix"
	
	
	
	
	
	def Determinant1(self):
		
		prior = self.root.ids.M1.text
		
		try:
			
			prior = ast.literal_eval(prior)
			

			prior1 = np.linalg.det([prior])		
			
			
			self.root.ids.M1.text = f"\n{prior} \n \n Determinat M1 = {prior1}"
			
		except:
			
			self.root.ids.M1.text = "enter a valid square matrix"




####################
####################
#### matrix 1 keyboard			
	
	def m_l_bracket(self):
		self.root.ids.M1.insert_text("(")
		
	
	def m_r_bracket(self):
		self.root.ids.M1.insert_text(")")
	
	
	def m_one(self):
		self.root.ids.M1.insert_text("1")	
	
	def m_two(self):
		self.root.ids.M1.insert_text("2")
	
	def m_three(self):
		self.root.ids.M1.insert_text("3")
		
	def m_four(self):
		self.root.ids.M1.insert_text("4")
	
	def m_five(self):
		self.root.ids.M1.insert_text("5")
	
	def m_six(self):
		self.root.ids.M1.insert_text("6")
	
	def m_seven(self):
		self.root.ids.M1.insert_text("7")
	
	def m_eight(self):
		self.root.ids.M1.insert_text("8")
	
	def m_nine(self):
		self.root.ids.M1.insert_text("9")
	
	def m_zero(self):
		self.root.ids.M1.insert_text("0")
	
	def m_dot(self):
		self.root.ids.M1.insert_text(".")
	
	def m_coma(self):
		self.root.ids.M1.insert_text(",")
	
	
	def m_clear(self):
		prior = self.root.ids.M1.text
		self.root.ids.M1.text = prior[:-1]
	
	
	
	
	
	
####################
####################
####### matrix 2
	
	def Transpose2(self):
		
		prior = self.root.ids.M2.text
		
		try:
			
			prior = ast.literal_eval(prior)
			

			prior1 = np.transpose([prior])		
			
			
			self.root.ids.M1.text = f"\n{prior} \n \n Transpose M2 = {prior1}"
			
		except:
			self.root.ids.M1.text = "enter a valid square matrix"
	
	
	
	def Determinant2(self):
		prior = self.root.ids.M2.text
		try:
			
			
			prior = ast.literal_eval(prior)

			prior1 = np.linalg.det([prior])		
			
			
			self.root.ids.M2.text = f"\n{prior} \n \nDeterminat M1 = {prior1}"
		except:
			self.root.ids.M2.text = "enter a valid square matrix"
	
#################
#################
####### matrix 2 keyboard

	def m2_l_bracket(self):
		self.root.ids.M2.insert_text("(")
		
	
	def m2_r_bracket(self):
		self.root.ids.M2.insert_text(")")
	
	
	def m2_one(self):
		self.root.ids.M2.insert_text("1")	
	
	def m2_two(self):
		self.root.ids.M2.insert_text("2")
	
	def m2_three(self):
		self.root.ids.M2.insert_text("3")
		
	def m2_four(self):
		self.root.ids.M2.insert_text("4")
	
	def m2_five(self):
		self.root.ids.M2.insert_text("5")
	
	def m2_six(self):
		self.root.ids.M2.insert_text("6")
	
	def m2_seven(self):
		self.root.ids.M2.insert_text("7")
	
	def m2_eight(self):
		self.root.ids.M2.insert_text("8")
	
	def m2_nine(self):
		self.root.ids.M2.insert_text("9")
	
	def m2_zero(self):
		self.root.ids.M2.insert_text("0")
	
	def m2_dot(self):
		self.root.ids.M2.insert_text(".")
	
	def m2_coma(self):
		self.root.ids.M2.insert_text(",")
	
	
	def m2_clear(self):
		prior = self.root.ids.M2.text
		self.root.ids.M2.text = prior[:-1]	
	
	
	def Add_Matrix(self):
		pass
	
	def Sub_Matrix(self):
		pass
	
	
	def Multiply_Matrix(self):
		pass
	





CalcApp().run()
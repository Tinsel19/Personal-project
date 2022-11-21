
from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kvdroid.tools.audio import Player

Code = """

MDBoxLayout:
	id: my_layout
	orientation: "vertical"
	md_bg_color: (1, .5,  0, 1)
	
	Image:
		id: my_image
		source: ""
	
	
	MDGridLayout:
		rows: 3
		cols: 1
		size_hint: 1, .2
		
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
			cols: 4
			size_hint: .9, 1
			padding: dp(20)
			spacing: dp(50)
			pos_hint: {"center_x":.5}
			md_bg_color: (1, .5, 0, 1)
			radius: dp(40)
			
			
			MDIconButton:
				icon: "arrow-left"
				theme_text_color: "Custom"
				text_color: ( 1, 1, 1, 1)
				on_press: app.previous()
			
			
			MDIconButton:
				icon: "pause"
				theme_text_color: "Custom"
				text_color: ( 1, 1, 1, 1)
				on_press: app.pause()
			
			MDIconButton:
				icon: "play"
				theme_text_color: "Custom"
				text_color: ( 1, 1, 1, 1)
				on_press: app.Play()
			
			MDIconButton:
				icon: "arrow-right"
				theme_text_color: "Custom"
				text_color: ( 1, 1, 1, 1)
				on_press: app.next()
		
	
	FileChooserListView:
		id: file_chooser
		on_selection: app.selected(file_chooser.selection)
		filters: ["*.mp3", "*.m4a", "*.jpg", "*.png"]
		

"""


class FileManagerApp(MDApp, App):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.prior = ""
		pass
	
	def build(self):
		builder = Builder.load_string(Code)
		return builder
	
	def selected(self, filename):
		
		try:
			
			if "jpg" in filename[0] or "png" in filename[0]:
				
				self.root.ids.my_image.source = filename[0]
				
				
			if "mp3" in filename[0] or "m4a" in filename[0] :
				
				player = Player()
				player.play(filename[0])
				self.root.ids.name.text = filename[0]
			
			
		except:
			pass
	
	def Play(self,):
		
		pass
	
	def previous(self):
		pass
		
	
	def pause(self):
		pass
		
		
	def next(self):
		pass
		
		
FileManagerApp().run()
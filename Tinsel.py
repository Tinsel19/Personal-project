from kivymd.app import MDApp
from kivy.lang import Builder

kv = '''
BoxLayout:
    RV:
        id:rv1
    RV:
        id:rv2
<RV@RecycleView>:
    #viewclass is the widget to be used as the children
    viewclass:'TwoLineListItem'
    RecycleBoxLayout:
        orientation:'vertical'
        #set size hint y to None or more than 1 to enable scrolling
        size_hint_y:None
        #If size hint y is None then set the height to use the minimum height available based on the number of children
        height:self.minimum_height
'''

class app(MDApp):
    
    def build(self):
        return Builder.load_string(kv)
           
    def on_start(self):
          #Adding children to recycleview which is the root in this case. The data is a list containing a dictionary with the properties 9f the children defined
          data = [{'text':'Title','secondary_text':'Secondary text','size_hint_x':1,'on_press':lambda x=i:print(i)} for i in range(740)]
          self.root.ids.rv1.data = data
          self.root.ids.rv2.data = data
          
app().run()
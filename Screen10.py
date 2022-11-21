
#####
#######  MAINAPP PAGE

Screen10 = """

Screen:
    name: "Page10"
    GridLayout:
        rows: 6
        cols: 1
        padding: "15dp"
        spacing: dp(20)
        
        GridLayout:
            rows: 1
            cols: 3
            size_hint: 1, .2
            
            
            GridLayout:
                rows: 2
                cols: 1
                size_hint: .25, .5
                
                Label:
                    text:  "ARTSA"
                    color: 0, 0, 0, 1
                    bold: True
                    canvas.before:
                        Color: 
                            rgba: 1, 1, 1, 1
                        Rectangle:
                            size: root.size
                    
                Label:
            Label:
                size_hint: .6, 1
                
            GridLayout:
                rows: 2
                cols: 1
                size_hint: .15, 1
                
                MDIconButton:
                    icon: "undraw_forgot_password_re_hxwm 2.png"
                    
    
                Label:
                    text: "Kurt Weller"
                    color: 0, 0, 0, 1
                    size_hint: .5, 1
        GridLayout:
            rows: 1
            cols: 2
            spacing: "15dp"
            size_hint: 1, .18
            TextInput:
                size_hint: .9, .5
                hint_text: "  Search e.g popular art"
                icon_left: "google"
                color_active: 1, 1, 1, 1
                line_color: 1, 1, 1, 1
                background_normal : ""
                font_name: "bahnschrift.ttf"
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1
                    Line: 
                        width: 2
                        rectangle: (*self.pos, *self.size)
            
            MDIconButton:
                icon: "zodiac-leo"
                size_hint: .1, 1
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1
                
        ScrollView:
            GridLayout:
                rows: 1
                cols: 4
                size_hint: None, 1
                width: root.width*4
                spacing: dp(20)
                
                Button:
                    canvas:
                        Rectangle:
                            source: "FB_IMG_1581933389997.jpg"
                            size: self.size
                Button:
                    color:0, 0, 0, 1
                Button:
                    color:0, 1, 0, 1
                    
                Button:
                    color:0, 0, 1, 1

        Button:
            adaptive_width: True
            text: "Refer and earn free coupon to buy an art    >>"
            color: 1, 1, 1, 1
            background_color: 0, 0, 0, 1
            bold: True
            size_hint: 1, .2
            font_name: "bahnschrift.ttf"
                    

                        
        ScrollView:
            
            MDList:
                TwoLineListItem:
                    text: "Ongoing"
                    font_name: "bahnschrift.ttf"
                    
                    secondary_text: "Art Auction"
                    font_name: "bahnschrift.ttf"
                    bold: True
                    ImageRightWidget: 
                        source: "FB_IMG_1581933389997.jpg"
                        
                TwoLineListItem:
                    font_name: "bahnschrift.ttf"
                    text: "Upcoming "
                    secondary_text: "Art Auction"
                TwoLineListItem:
                    font_name: "bahnschrift.ttf"
                    text: "Art Product"
                    
                TwoLineListItem:
                    font_name: "bahnschrift.ttf"
                    text: "Art Of The Week"
         
        
        GridLayout:
            rows: 1
            cols: 4
            size_hint: 1, .2
            spacing: dp(20)
            MDIconButton:
                icon: "home"
                size_hint: .25, 1
                
                
            MDIconButton:
                icon: "bell"
                size_hint: .25, 1
                opacity: .8
                
            MDIconButton:
                icon: "cart"
                size_hint: .25, 1
                opacity: .8
                
            MDIconButton:
                icon: "account"
                size_hint: .25, 1
                opacity: .8
            
<RoundedButton@Button>:
    background_color: 0, 0, 0, 0
    background_normal: ""
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        RoundedRectangle: 
            size: self.size
            pos: self.pos
            radius: [100]
"""
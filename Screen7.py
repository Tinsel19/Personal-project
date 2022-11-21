Screen7 = """
#FORGOT PASSWORD PAGE           
Screen:
    name: "Page7"
    GridLayout:
        #orientation: "vertical"
        #padding: "25dp"
        rows: 4
        cols: 1
        GridLayout:
            rows: 2
            cols: 1
            size_hint: 1, .4
            padding: "10dp"
            MDToolbar:
                title: "               ARTSA"
                md_bg_color: 0, 0, 0, .001
                specific_text_color: 0, 0, 0, 1
                font_name: "bahnschrift.ttf"
                use_overflow: True
                opposite_color: False
                halign: "center"
                left_action_items: [["backburger", lambda x: app.back_six()]]
            
            Image:
                source: "undraw_forgot_password_re_hxwm 2.png"
                allow_stretch: True
                keep_ratio: True
        GridLayout:
            rows: 2
            cols: 1
            size_hint: 1, .1
            MDLabel:
                text: "Forgot  Password?"
                halign: "center"
                bold: True
                font_name: "bahnschrift.ttf"
                font_size: "25dp"
                size_hint: 1, .5
            
            MDLabel:
                text: "Enter your email below, an OTP code \\n will be sent to you shortly"
                halign: "center"
                bold: True
                font_name: "bahnschrift.ttf"
                size_hint: 1, .5
                #font_size: "10dp"
                #bold: False
        
        GridLayout:
            rows: 3
            cols: 1    
            padding: "20dp"
            spacing: "40dp"
            size_hint: 1, .25
            
            TextInput:
                hint_text: "Enter your email address"
                foreground_color: "blue"
                size_hint: 1, None
                height: dp(40)
                background_normal: ""
                multiline: False
                font_name: "bahnschrift.ttf"
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1
                    Line: 
                        width: 1
                        rectangle: (*self.pos, *self.size)
            GridLayout:
                cols: 3
                rows: 1
                size_hint: 1, .5
                Label:
                    size_hint: .2, 1
                Button:
                    text: "Proceed"
                    pos_hint: {"x": .8}
                    font_name: "bahnschrift.ttf"
                    size_hint: .6, None
                    height: dp(35)
                    background_color: 0, 0, 0, 1
                    on_release: 
                        app.root.current = "Page8"
                        root.manager.transition.direction = "left"
                        
                    
                Label:
                    size_hint: .2, 1
"""
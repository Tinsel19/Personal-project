Screen9 = """
#SET UP A NEW PASSWORD PAGE

Screen:       
    name: "Page9"
    GridLayout:
        rows: 2
        cols: 1
        GridLayout:
            rows: 7
            cols: 1
            size_hint: 1, .85
            padding: "20dp"
            spacing: "20dp"
            MDToolbar:
                title: "               ARTSA"
                md_bg_color: 1, 1, 1, 1
                specific_text_color: 0, 0, 0, 1
                font_name: "bahnschrift.ttf"
                use_overflow: True
                left_action_items: [["backburger", lambda x: app.back_eight()]]
                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 1
                    Rectangle:
                        size: root.size
            Label:
                
            Label:
                text: "Set Up A New\\n Password"
                halign: "center"
                font_size: "40dp"     
                color: 0, 0, 0, 1
                bold: True
                font_name: "bahnschrift.ttf"
                
            Label:
                text: "Enter your email below, an OTP code\\n  will be sent to you shortly"
                color: 0, 0, 0, 1
                bold: True
                halign: "center"
                font_name: "bahnschrift.ttf"
                

            TextInput:
                hint_text: "Enter your Password"
                foreground_color: "blue"
                background_normal: ""
                size_hint: 1, None
                height: dp(40)
                multiline: False
                font_name: "bahnschrift.ttf"
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1
                    Line: 
                        width: 1
                        rectangle: (*self.pos, *self.size)
                        
            TextInput:
                hint_text: "Confirm your Password"
                foreground_color: "blue"
                background_normal: ""
                multiline: False
                size_hint: 1, None
                height: dp(40)
                font_name: "bahnschrift.ttf"
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1
                    Line: 
                        width: 1
                        rectangle: (*self.pos, *self.size)
            GridLayout:
                size_hint: 1, .7
                rows: 1
                cols: 3
                Label:
                    size_hint: .1, 1
                Button:
                    text: "Reset"
                    color: 1, 1, 1, 1
                    background_color: 0, 0, 0, 1
                    size_hint: .8, None
                    height: dp(50)
                    font_name: "bahnschrift.ttf"
                    on_release: app.root.current = "Page6"
                Label:
                    size_hint: .1, 1
            
            Label:
        Label:
            size_hint: 1, .15

"""
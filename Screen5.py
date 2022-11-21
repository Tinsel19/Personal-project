Screen5 = """
#SIGN UP PAGE
Screen:
    id: Page
    name: "Page5"
    GridLayout:
        #orientation: 'vertical'
        #spacing: "40dp"
        #padding: "20dp"
        rows: 3
        cols: 1
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            Rectangle:
                size: root.size
        GridLayout:
            rows: 2
            cols: 1
            size_hint: 1, .5
            MDToolbar:
                title: "                   ARTSA"
                md_bg_color: 1, 1, 1, 1
                specific_text_color: 0, 0, 0, 1
                font_name: "arialbd.ttf"
                use_overflow: True
                opposite_color: False
                left_action_items: [["backburger", lambda x: app.back_four()]]
                
                
            Label:
                text: "Welcome Onboard"
                color: 0, 0, 0, 1
                size_hint: 1, .2
                font_size: "35dp"
                font_name: "bahnschrift.ttf"
        GridLayout:
            rows: 4
            cols: 1
            spacing: "10dp"
            padding: "20dp"
            size_hint_y: None
            height: dp(240)
            TextInput:
                hint_text: "Enter your username"
                foreground_color: "blue"
                background_normal: ""
                multiline: False
                id: text1
                font_name: "bahnschrift.ttf"
                radius: 4
                padding: 10, 5
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1
                    Line: 
                        width: 1
                        rectangle: (*self.pos, *self.size)
                
            TextInput:
                hint_text: "Enter email address"
                foreground_color: "blue"
                background_normal: ""
                multiline: False
                id: text2                                   
                font_name: "bahnschrift.ttf"
                padding: 10, 5
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1
                    Line: 
                        width: 1
                        rectangle: (*self.pos, *self.size)
            TextInput:
                hint_text: "Enter your password"
                foreground_color: "blue"
                background_normal: ""
                multiline: False
                id: text3
                font_name: "bahnschrift.ttf"
                padding: 10, 5
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1
                    Line: 
                        width: 1
                        rectangle: (*self.pos, *self.size)
            TextInput:
                hint_text: "Confirm your password"
                foreground_color: "blue"
                background_normal: ""
                multiline: False
                id: text4
                font_name: "bahnschrift.ttf"
                padding: 10, 5
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1
                    Line: 
                        width: 1
                        rectangle: (*self.pos, *self.size)
        
        GridLayout:
            rows: 4
            cols: 1
            padding: "40dp"
            size_hint: 1, 1
            MDRectangleFlatButton:
                text: "Sign Up"
                font_size: "13dp"
                md_text_color: "Custom"
                text_color: 1, 1, 1, 1
                md_bg_color: 0, 0, 0, 1
                background_color: 0, 0, 0, 1
                size_hint: .5, None
                
                height: dp(30)
                pos_hint: {"center_x":.5}
                font_name: "bahnschrift.ttf"
                radius: dp(5)
                on_release: 
                    app.root.current = "Page6"
                    root.manager.transition.direction = "left"
                #on_press: app.reset_text_five()
            
            Label:
                text: " Or \\n Sign up with"
                size_hint: .5, .7
                color: 0, 0, 0, 1
                halign: "center"
                font_size: "13dp"
            GridLayout:
                rows: 1
                cols: 5
                size_hint: .7, .4
                spacing: "10dp"
                Label:
                    size_hint: .1, .2
                MDIconButton:
                    icon: "youtube"
                    theme_text_color: "Custom"
                    text_color: 1, 0, 0, 1
                    md_bg_color: 0, 0, 0, .1
                MDIconButton:
                    icon: "twitter"
                    theme_text_color: "Custom"
                    text_color: 0, 0, 1, 1
                    md_bg_color: 0, 0, 0, .1
                MDIconButton:
                    icon: "google"
                    md_bg_color: 0, 0, 0, .1
                Label:
                    size_hint: .1, .2
            GridLayout:
                rows: 1
                cols: 2
                GridLayout:
                    rows: 2
                    cols: 1
                    Label:
                    Label:
                        text: "Don't have an account yet ?"
                        color: 0, 0, 0, 1
                        valign: "bottom"
                        size_hint: 1, .3
                        font_name: "bahnschrift.ttf"
                MDTextButton:
                    text: "sign in"
                    bold: True
                    
"""
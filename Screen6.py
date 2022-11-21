Screen6 = """
#LOG IN PAGE AFTER FIRST SIGN IN
#: import webbrowser webbrowser
Screen:
    name: "Page6"
    GridLayout:
        #orientation: 'vertical'
        #spacing: "40dp"
        #padding: "20dp"
        rows: 5
        cols: 1
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            Rectangle:
                size: root.size
        GridLayout:
            rows: 2
            cols: 1
            size_hint: 1, .6
            MDToolbar:
                title: "                 ARTSA"
                md_bg_color: 1, 1, 1, 1
                specific_text_color: 0, 0, 0, 1
                font_name: "arialbd.ttf"
                use_overflow: True
                opposite_color: False
                left_action_items: [["backburger", lambda x: app.back_four()]]
                #elevation: 10
            
            Label:
                text: "Welcome Back !"
                font_name: "bahnschrift.ttf"
                font_size: "40dp"
                halign: "center"
                size_hint: 1, .15
                color: 0, 0, 0, 1
                
        GridLayout:
            rows: 2
            cols: 1
            spacing: "20dp"
            padding: "20dp"
            size_hint: 1, None
            height: dp(140)
            TextInput:
                hint_text: "Enter your email address"
                foreground_color: "blue"
                background_normal: ""
                size_hint: 1, 1
                multiline: False
                font_name: "bahnschrift.ttf"
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1
                    Line: 
                        width: 1
                        rectangle: (*self.pos, *self.size)
            TextInput:
                hint_text: "Enter your password"
                foreground_color: "blue"
                size_hint: 1, 1
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
            rows: 1
            cols: 2
            size_hint: 1, .15
            Label:
                   
            MDTextButton:
                text: "Forgot password?"
                size_hint: .7, .2
                font_name: "bahnschrift.ttf"
                font_size: "15dp"
                bold: True
                on_release: 
                    app.root.current = "Page7"
                    root.manager.transition.direction = "left"
                
        GridLayout:
            rows: 4
            cols: 1
            padding: "60dp"
            size_hint: 1, 1
            
            MDRectangleFlatButton:
                text: "Log in"
                font_size: "14dp"
                md_text_color: "Custom"
                text_color: 1, 1, 1, 1
                md_bg_color: 0, 0, 0, 1
                background_color: 0, 0, 0, 1
                size_hint: .5, None
                height: dp(30)
                pos_hint: {"center_x":.2}
                font_name: "bahnschrift.ttf"
                on_release: app.root.current = "Page10"
            
            Label:
                text: "Or Log in with"
                size_hint: .5, .4
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
                    on_release: webbrowser.open("https://youtube.com/")
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
                    text: "sign up"
                    bold: True
        Label:
            size_hint: 1, .2
      
      
"""
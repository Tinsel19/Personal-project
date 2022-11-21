Screen4 = """
Screen:
    name: "Page4"
    BoxLayout:
        orientation: "vertical"
        spacing: "20dp"
        Screen:
        Button:
            text: "Log in"
            size_hint: .8, None
            height: dp(50)
            pos_hint: {"top": .6, "x": .1}
            background_color: 0, 0, 0, 1
            bold: True
            on_release: 
                app.root.current = "Page6"
                root.manager.transition.direction = "left"
            
    
        MDRectangleFlatButton:
            text: "Sign Up"
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1
            size_hint: .8, .14
            pos_hint: {"top": .6, "x": .1}
            line_color: 0, 0, 0, 1
            background_color: 1, 1, 1, 0
            line_width: 1.26
            bold_text: True
            font_name: "arialbd.ttf"
            on_release: 
                app.root.current = "Page5"
                root.manager.transition.direction = "left"
        Screen:

"""
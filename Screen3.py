Screen3 = """

Screen:
    name: "Page3"
    BoxLayout:
        orientation: "vertical"
        padding: "25dp"
        Label:
            size_hint: 1, .1
        Image:
            source: "undraw_location_tracking_re_n3ok 2.png"
            allow_stretch: True
            keep_ratio: True
            size_hint_x: .8
            pos_hint: {"center_x": .5}
            size_hint_y: 1

            
        MDLabel:
            text: "Get notified of upcoming art auction from  \\n the corner of your home. "
            halign: "center"
            bold: True
            font_name: "bahnschrift.ttf"
            size_hint_y: None
            height: dp(150)
        
        GridLayout:
            cols: 3
            rows: 1
            size_hint: 1, .15
            MDTextButton:
                text: "previous"
                pos_hint: {"x": .8}
                font_name: "bahnschrift.ttf"
                on_release: 
                    app.root.current = "Page2"
                    root.manager.transition.direction = "right"
            Label:
                size_hint: .5, 1
            
            MDTextButton:
                text: "start"
                pos_hint: {"x": .8}
                font_name: "bahnschrift.ttf"
                on_release: 
                    app.root.current = "Page4"
                    root.manager.transition.direction = "left"
        Screen:
            size_hint: 1, .06
            

"""
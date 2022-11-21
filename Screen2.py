Screen2 = """
Screen:
    name: "Page2"
    BoxLayout:
        orientation: "vertical"
        padding: "25dp"
        Label:
            size_hint: 1, .1
        Image:
            source: "undraw_making_art_re_ee8w 2.png"
            allow_stretch: True
            keep_ratio: True
            size_hint_x: .8
            pos_hint: {"center_x": .5}
            size_hint_y: 1

            
        MDLabel:
            text: "Get art product of your choice anytime  \\nand track the order from the corner of\\n your home."
            halign: "center"
            bold: True
            font_name: "bahnschrift.ttf"
            size_hint: 1, None
            height: dp(150)
        
        GridLayout:
            cols: 3
            rows: 1
            size_hint: 1, .15
            MDTextButton:
                text: "previous "
                pos_hint: {"x": .8}
                font_name: "bahnschrift.ttf"
                on_release: 
                    app.root.current = "Page1"
                    root.manager.transition.direction = "right"
            Label:
                background_normal: ""
                size_hint: .5, 1
            MDTextButton:
                text: "next"
                pos_hint: {"x": .8}
                font_name: "bahnschrift.ttf"
                on_release: 
                    app.root.current = "Page3"
                    root.manager.transition.direction = "left"
        Screen:
            size_hint: 1, .06

"""
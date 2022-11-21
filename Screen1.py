Screen1 = """
Screen:
    name: "Page1"
    BoxLayout:
        orientation: "vertical"
        padding: "25dp"
        #spacing: dp(20)
        Label:
            size_hint: 1, .1
        Image:
            source: "undraw_art_lover_re_fn8g 2.png"
            allow_stretch: True
            keep_ratio: True
            size_hint_x: .8
            pos_hint: {"center_x": .5}
            size_hint_y: 1

        MDLabel:
            text: "Easy way to attend art auction and  \\nPurchase art product from the corner of\\n your home."
            halign: "center"
            bold: True
            font_name: "bahnschrift.ttf"
            size_hint_y: None
            height: dp(150)

		GridLayout:
			cols: 2
			rows:1
			size_hint: 1, .15
			Label:
				size_hint: 1, 1
            MDTextButton:
                text: "skip"
                #pos_hint: {"x": .8}
                font_name: "bahnschrift.ttf"
                size_hint_x: None
                width: dp(50)
                on_release: 
                    app.root.current = "Page2"
                    root.manager.transition.direction = "left"


        Screen:
            size_hint: 1, .06



"""
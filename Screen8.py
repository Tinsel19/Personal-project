Screen8 = """
#PASSWORD FORGOTTEN VERIFICATION PAGE
Screen:    
    name: "Page8"
    GridLayout:
        rows: 2
        padding: "10dp"
        cols: 1
        GridLayout:
            rows: 9
            cols: 1
            size_hint: 1, .4
            padding: "10dp"
            spacing: "10dp"
            MDToolbar:
                title: "               ARTSA"
                md_bg_color: 1, 1, 1, 1
                specific_text_color: 0, 0, 0, 1
                font_name: "arialbd.ttf"
                use_overflow: True
                left_action_items: [["backburger", lambda x: app.back_seven()]]
                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 1
                    Rectangle:
                        size: root.size
                
                
            Label:
                
            
            Image: 
                source: ""
                allow_stretch: True
                keep_ratio: True
            
            Label:
                text: "Verification"
                halign: "center"
                bold: True
                color: 0, 0, 0, 1
                font_size: "35dp"
            
            Label:
                text: "Enter the OTP sent to your email"
            
            GridLayout:
                rows: 1
                cols: 4
                spacing: "10dp"
                TextInput:
                    elevation: "10dp"
                    multiline: False
                    color: 1, 1, 1, 1
                    halign: "center"
                    valign: "center"
                    font_size: "30dp"
                    on_text: 
                        if len(self.text.strip()) >= 1: self.readonly = True
                    on_double_tap: self.readonly = False
            
                    
                TextInput:
                    multiline: False
                    color: 1, 1, 1, 1
                    halign: "center"
                    valign: "center"
                    font_size: "30dp"
                    on_text: 
                        if len(self.text.strip()) >= 1: self.readonly = True
                    on_double_tap: self.readonly = False
            
                    
                TextInput
                    multiline: False
                    color: 1, 1, 1, 1
                    halign: "center"
                    valign: "center"
                    font_size: "30dp"
                    
                    on_text: 
                        if len(self.text.strip()) >= 1: self.readonly = True
                    on_double_tap: self.readonly = False
            
                    
                TextInput:
                    multiline: False
                    color: 1, 1, 1, 1
                    halign: "center"
                    valign: "center"
                    font_size: "30dp"
                    on_text: 
                        if len(self.text.strip()) >= 1: self.readonly = True
                    on_double_tap: self.readonly = False
            Label:
                size_hint: 1, .4
            GridLayout:
                rows: 1
                cols: 3
                Label:
                    size_hint: .2, 1
                Button:
                    text: "Verify"
                    size_hint: .6, 1
                    background_color: 0, 0, 0, 1
                    color: 1, 1, 1, 1
                    bold: True
                    on_release: 
                        app.root.current = "Page9"
                        root.manager.transition.direction = "left"
                Label:
                    size_hint: .2, 1
            
            GridLayout:
                rows: 1
                cols: 4
                padding: "20dp"
                Label:
                    size_hint: .6, 1
                GridLayout:
                    cols: 1
                    rows: 2
                    Label:
                        size_hint: 1, .3
                    
                    Label:
                        text: "Don't get a code?"
                        color: 0, 0, 0, 1
                        valign: "top"
                        size_hint: 1, .7
                        
                    
                MDTextButton:
                    text: "Resend"
                    bold: True
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1                
                    
                Label:
                    size_hint:  .6, 1
                
        Screen:
            size_hint: 1 , .1   


"""
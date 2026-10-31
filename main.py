from kivy.app import App
from kivy.uix.label import Label

class LabApp(App):
    def build(self):
        return Label(text="CYBER SECURITY LAB\nEducational Demo Only", font_size=28, halign="center")

LabApp().run()

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
Builder.load_file('libs/components/Me.kv')

class MeScreen(Screen):
    def __init__(self, **kwargs):
        super(MeScreen, self).__init__(**kwargs)
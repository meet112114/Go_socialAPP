from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
Builder.load_file('libs/components/Ee.kv')

class EeScreen(Screen):
    def __init__(self, **kwargs):
        super(EeScreen, self).__init__(**kwargs)
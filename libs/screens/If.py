from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
Builder.load_file('libs/components/If.kv')

class IfScreen(Screen):
    def __init__(self, **kwargs):
        super(IfScreen, self).__init__(**kwargs)
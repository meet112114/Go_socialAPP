from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
Builder.load_file('libs/components/errorscreen.kv')

class ErrorScreen(Screen):
    def __init__(self, **kwargs):
        super(ErrorScreen, self).__init__(**kwargs)
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
Builder.load_file('libs/components/Ej.kv')

class EjScreen(Screen):
    def __init__(self, **kwargs):
        super(EjScreen, self).__init__(**kwargs)
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_file('libs/components/users.kv')

class UsersScreen(Screen):
    def __init__(self, **kwargs):
        super(UsersScreen, self).__init__(**kwargs)
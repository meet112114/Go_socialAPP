from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_file('libs/components/user_profile.kv')

class UserProScreen(Screen):
    def __init__(self, **kwargs):
        super(UserProScreen, self).__init__(**kwargs)
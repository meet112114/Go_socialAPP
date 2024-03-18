from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_file('libs/components/addpost.kv')

class AddPostScreen(Screen):
    def __init__(self, **kwargs):
        super(AddPostScreen, self).__init__(**kwargs)
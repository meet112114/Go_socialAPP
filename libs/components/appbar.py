from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.app import App


class AppBar1(MDBoxLayout):

    def gotohome(self):
        app = App.get_running_app()
        screen_manager = app.root
        screen_manager.current = 'pre_home'
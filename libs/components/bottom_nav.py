from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.app import App


class BottomNav(MDBoxLayout):
    avatar = StringProperty()

    def addpost(self):
        app = App.get_running_app()
        screen_manager = app.root
        screen_manager.current = 'add_post'
    
    def users(self):
        app = App.get_running_app()
        screen_manager = app.root
        screen_manager.current = 'users'

    def UserProfile(self):
        app = App.get_running_app()
        screen_manager = app.root
        screen_manager.current = 'UserProfile'
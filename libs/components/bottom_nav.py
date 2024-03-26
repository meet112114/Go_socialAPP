from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.app import App


class BottomNav(MDBoxLayout):
    avatar = StringProperty()

    def EE(self):
        app = App.get_running_app()
        screen_manager = app.root
        screen_manager.current = 'Ee'
    
    def CO(self):
        app = App.get_running_app()
        screen_manager = app.root
        screen_manager.current = 'Co'

    def EJ(self):
        app = App.get_running_app()
        screen_manager = app.root
        screen_manager.current = 'Ej'

    def ME(self):
        app = App.get_running_app()
        screen_manager = app.root
        screen_manager.current = 'Me'

    def IF(self):
        app = App.get_running_app()
        screen_manager = app.root
        screen_manager.current = 'If'

from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from libs.components.list import List
import requests
Builder.load_file('libs/components/Ee.kv')

class EeScreen(MDScreen):
    def on_enter(self): 
        self.list_announce()

    def list_announce(self):
        api_url = "http://localhost:8000/announce/get/ee/"
        response = requests.get(api_url)
        print(response.text)
        if response.status_code == 200:
            Lists = response.json()
            announcements_layout = self.ids.announcements
            announcements_layout.clear_widgets() 
            for list in Lists:
                print(list['created_at'])
                self.ids.announcements.add_widget(List(
                    created_at=list['created_at'],
                    text=list['text']
                    ))
        else:
            print("Failed to fetch posts:", response.text)
        
    def go_to_home(self):
        app = App.get_running_app()
        screen_manager = app.root
        screen_manager.current = 'home'
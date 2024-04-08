from kivy.uix.screenmanager import Screen
import requests
from kivy.app import App
from kivy.lang import Builder
from libs.components.Leclist import LecList
Builder.load_file('libs/components/iflec.kv')

class IfLec(Screen):

    def on_enter(self): 
        self.GetData()
    
    def GetData(self):
        api_url = "http://localhost:8000/lecture/get/if/"
        response = requests.get(api_url)
        print(response.text)
        if response.status_code == 200:
            Lists = response.json()
            LectureList_layouyt = self.ids.lectureList
            LectureList_layouyt.clear_widgets() 
            for list in Lists:
                print(list['title'])
                self.ids.lectureList.add_widget(LecList(
                    title = list['title'],
                    link = list['link'],
                    time = list['time'],
                    password = list['password']
                    ))
        else:
            print("Failed to fetch posts:", response.text)
        
    def open_link(self, link):
        import webbrowser
        webbrowser.open(link)
        
    def go_to_home(self):
        app = App.get_running_app()
        screen_manager = app.root
        screen_manager.current = 'pre_home'
from kivymd.uix.screen import MDScreen
import json
from kivy.uix.screenmanager import Screen
import requests
from libs.components.post_card import PostCard
from kivy.storage.jsonstore import JsonStore
store = JsonStore('config.json')

class HomePage(MDScreen):
    profile_pic = 'assets/images/NES.jpg'
   
    def on_enter(self): 
        self.list_posts()
    
  

    def list_posts(self):
        api_url = "http://192.168.0.116:8000/posts/"
        response = requests.get(api_url)

        if response.status_code == 200:
            posts = response.json() 
            announcements_layout = self.ids.timeline
            announcements_layout.clear_widgets() 
            for post in posts:

                userid = post['user']
                api_url1 = f"http://192.168.0.116:8000/user/{userid}/"
                response1 = requests.get(api_url1)
                response_dict = json.loads(response1.text)
                username = response_dict['username']

                self.ids.timeline.add_widget(PostCard(
                    profile_pic = self.profile_pic,
                    username = username,
                    caption=post['title'],
                    post=post['image'],
                    post_id = post['id']
                    ))
        else:
            print("Failed to fetch posts:", response.text)
    

    
    
    
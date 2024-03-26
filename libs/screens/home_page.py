from kivymd.uix.screen import MDScreen
import json
from kivy.uix.screenmanager import Screen
import requests
from libs.components.post_card import PostCard
from kivy.storage.jsonstore import JsonStore
store = JsonStore('config.json')

class HomePage(MDScreen):
    profile_pic = 'assets/images/defaultUser-min.jpg'
   
    def on_enter(self): 
        self.list_posts()
                
    

    def list_posts(self):
        api_url = "http://localhost:8000/posts/"
        response = requests.get(api_url)

        if response.status_code == 200:
            posts = response.json() 
            for post in posts:
                userid = post['user']
                api_url = f"http://localhost:8000/user/{userid}"
                response = requests.get(api_url)
                response_dict = json.loads(response.text)
                username = response_dict['username']
                auth_token = store.get('user')['token']
                headers = {'Authorization': f'Token {auth_token}'}
                like_url = f"http://localhost:8000/post/like/{post['id']}/"
                response1 = requests.get(like_url,headers=headers)
                print(response1.text)
                response_dict2 = json.loads(response1.text)
                likes = response_dict2['likes_count']

                self.ids.timeline.add_widget(PostCard(
                    profile_pic = self.profile_pic,
                    username=username,
                    caption=post['title'],
                    post=post['image'],
                    post_id = post['id'],
                    likes=f"{likes}"
                    ))
        else:
            print("Failed to fetch posts:", response.text)
    

    
    
    
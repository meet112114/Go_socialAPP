from kivymd.uix.card import MDCard
from kivy.properties import StringProperty ,NumericProperty
import requests
import json
from kivy.storage.jsonstore import JsonStore
store = JsonStore('config.json')

class PostCard(MDCard):
    profile_pic = StringProperty()
    username = StringProperty()
    post = StringProperty()
    caption = StringProperty()
    likes = StringProperty()
    post_id = NumericProperty()
    liked = NumericProperty()
    

    def  get_like_post(self , **kwargs):
        auth_token = store.get('user')['token']
        headers = {'Authorization': f'Token {auth_token}'}
        like_url = f"http://localhost:8000/post/Getlike/{self.post_id}/"
        response = requests.get(like_url , headers=headers)
        response_dict = json.loads(response.text)
        self.liked = response_dict['is_liked']

    def get_likescount(self , **kwargs):
        like_url = f"http://localhost:8000/post/like/{self.post_id}/"
        auth_token = store.get('user')['token']
        headers = {'Authorization': f'Token {auth_token}'}
        likes_response = requests.get(like_url , headers=headers)
        response_dict1 = json.loads(likes_response.text)
        self.likes = str(response_dict1['likes_count']) 
       
    
    def like_post(self):
        auth_token = store.get('user')['token']
        headers = {'Authorization': f'Token {auth_token}'}
        like_url = f"http://localhost:8000/post/like/{self.post_id}/"
        response = requests.post(like_url , headers=headers)
        if response.status_code == 200: # Toggle the liked property
            self.liked = 0 if self.liked == 1 else 1
            self.icon = 'heart' if self.liked == 1 else 'heart-outline'


            auth_token = store.get('user')['token']
            headers = {'Authorization': f'Token {auth_token}'}
            like_url = f"http://localhost:8000/post/like/{self.post_id}/"
            likes_response = requests.get(like_url , headers=headers)
            if likes_response.status_code == 200:
               self.get_likescount()
            else:
                print("Failed to fetch updated likes for the post:", likes_response.text)
        else:
            print("Failed to toggle like for the post:", response.text)

    
    def __init__(self, **kwargs):
        super(PostCard, self).__init__(**kwargs)
        self.get_like_post()
        self.get_likescount()
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
    post_id = NumericProperty()
    

    def __init__(self, **kwargs):
        super(PostCard, self).__init__(**kwargs)
       
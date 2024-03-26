from kivymd.uix.card import MDCard
from kivy.properties import StringProperty  ,NumericProperty
from kivy.storage.jsonstore import JsonStore
store = JsonStore('config.json')

class List(MDCard):
    text = StringProperty()
    created_at = StringProperty()

    def __init__(self, **kwargs):
        super(List, self).__init__(**kwargs)
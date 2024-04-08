from kivymd.uix.card import MDCard
from kivy.properties import StringProperty  
from kivy.storage.jsonstore import JsonStore
store = JsonStore('config.json')

class LecList(MDCard):
    title = StringProperty()
    link = StringProperty()
    time = StringProperty()
    password = StringProperty()

    def __init__(self, **kwargs):
        super(LecList, self).__init__(**kwargs)
    
    def open_link(self, link):
        import webbrowser
        webbrowser.open(link)
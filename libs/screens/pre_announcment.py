from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
Builder.load_file('libs/components/pre_announcement.kv')

class PreAnnouncement(Screen):
    
    def gotoco(self):
        self.manager.current = ('Co')

    def gotoee(self):
        self.manager.current = ('Ee')

    def gotome(self):
        self.manager.current = ('Me')

    def gotoif(self):
        self.manager.current = ('If')

    def gotoej(self):
        self.manager.current = ('Ej')
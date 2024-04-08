from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
Builder.load_file('libs/components/lecture.kv')

class Lecture(Screen):
    
    def gotoco(self):
        self.manager.current = ('colec')
    
    def gotoee(self):
        self.manager.current = ('eelec')
    
    def gotoej(self):
        self.manager.current = ('ejlec')

    def gotoif(self):
        self.manager.current = ('iflec')

    def gotome(self):
        self.manager.current = ('melec')
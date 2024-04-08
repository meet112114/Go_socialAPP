from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
Builder.load_file('libs/components/pre_home.kv')
import webbrowser

class PreHomePage(Screen):
    
    def on_enter(self): 
        pass

    def gotoweb(self):
        webbrowser.open("https://www.navjeevanedu.com/poly/polytechnic.html")

    def gotolecture(self):
        self.manager.current = ('lecture')
    
    def gotohome(self):
        self.manager.current = ('home')

    def gotopreann(self):
        self.manager.current = ('preann')
    
    def gotosports(self):
        self.manager.current = ('sports')

    def gotocomplaint(self):
        self.manager.current = ('complaint')
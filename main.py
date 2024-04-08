from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager
from libs.screens.home_page import HomePage 
from libs.screens.login import LoginScreen
from libs.screens.register import CreateAccountScreen
from libs.screens.errorscreen import ErrorScreen
from libs.screens.Co import CoScreen
from libs.screens.If import IfScreen
from libs.screens.Me import MeScreen
from libs.screens.Ee import EeScreen
from libs.screens.Ej import EjScreen
from libs.screens.pre_home import PreHomePage
from libs.screens.lectures import Lecture
from libs.screens.colec import Colec
from libs.screens.melec import Melec
from libs.screens.iflec import IfLec
from libs.screens.eelec import EeLec
from libs.screens.ejlec import EjLec
from libs.screens.pre_announcment import PreAnnouncement
from libs.screens.sports import Sports
from libs.screens.complain import Complaint


class GoSocialApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Cyan"
        Window.size = [300, 600] 
        self.load_all_kv_files()
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(CreateAccountScreen(name='create_account'))
        sm.add_widget(HomePage(name='home')) 
        sm.add_widget(ErrorScreen(name='error'))
        sm.add_widget(CoScreen(name='Co')) 
        sm.add_widget(IfScreen(name='If'))
        sm.add_widget(MeScreen(name='Me'))
        sm.add_widget(EeScreen(name='Ee'))
        sm.add_widget(EjScreen(name='Ej'))
        sm.add_widget(PreHomePage(name='pre_home'))
        sm.add_widget(Lecture(name='lecture'))
        sm.add_widget(Colec(name='colec'))
        sm.add_widget(Melec(name='melec'))
        sm.add_widget(IfLec(name='iflec'))
        sm.add_widget(EeLec(name='eelec'))
        sm.add_widget(EjLec(name='ejlec'))
        sm.add_widget(PreAnnouncement(name="preann"))
        sm.add_widget(Sports(name='sports'))
        sm.add_widget(Complaint(name = 'complaint'))
        return sm
    
    def load_all_kv_files(self):
        Builder.load_file('libs/screens/home_page.kv')
        Builder.load_file('libs/components/appbar.kv')
        Builder.load_file('libs/components/appbar2.kv')
        Builder.load_file('libs/components/appbar3.kv')
        Builder.load_file('libs/components/bottom_nav.kv')
        Builder.load_file('libs/components/post_card.kv')
        Builder.load_file('libs/components/list.kv')
        Builder.load_file('libs/components/leclist.kv')
        Builder.load_file('libs/components/appbars.kv')
    


if __name__ == "__main__":
    GoSocialApp().run()
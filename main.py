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
        return sm
    
    def load_all_kv_files(self):
        Builder.load_file('libs/screens/home_page.kv')
        Builder.load_file('libs/components/appbar.kv')
        Builder.load_file('libs/components/appbar2.kv')
        Builder.load_file('libs/components/bottom_nav.kv')
        Builder.load_file('libs/components/post_card.kv')
        Builder.load_file('libs/components/list.kv')
    


if __name__ == "__main__":
    GoSocialApp().run()
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager
from libs.screens.home_page import HomePage 
from libs.screens.login import LoginScreen
from libs.screens.register import CreateAccountScreen
from libs.screens.addpost import AddPostScreen
from libs.screens.users import UsersScreen
from libs.screens.user_profile import UserProScreen


class GoSocialApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Cyan"
        Window.size = [300, 600]
        self.load_all_kv_files()
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(CreateAccountScreen(name='create_account'))
        sm.add_widget(HomePage(name='home')) 
        sm.add_widget(AddPostScreen(name='add_post')) 
        sm.add_widget(UsersScreen(name='users'))
        sm.add_widget(UserProScreen(name='UserProfile'))
        return sm
    
    def load_all_kv_files(self):
        Builder.load_file('libs/screens/home_page.kv')
        Builder.load_file('libs/components/appbar.kv')
        Builder.load_file('libs/components/bottom_nav.kv')
        Builder.load_file('libs/components/post_card.kv')
    


if __name__ == "__main__":
    GoSocialApp().run()
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.dialog import MDDialog
import requests
from kivymd.uix.button import MDFlatButton
import json


Builder.load_file('libs/components/login.kv')
store = JsonStore('config.json')

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)



    def login(self):
        
        email = self.ids.email.text
        password = self.ids.passwd.text
        url = 'http://localhost:8000/user/login/' 
        payload = {'email': email, 'password': password}
        try:
            response = requests.post(url, data=payload)

            if response.status_code == 200:
                response_data = json.loads(response.text)
            
                if response_data["message"] ==  "incorrect password":
                    invalid_credentials_dialog = MDDialog(
                    title="Wrong Password ",
                    text="Please enter password.",
                    buttons=[
                        MDFlatButton(
                            text="OK",
                            on_release=lambda *args: invalid_credentials_dialog.dismiss()
                        )
                    ]
                    )
                    invalid_credentials_dialog.open()

                elif response_data["message"] ==  "User does not exists":
                    invalid_credentials_dialog = MDDialog(
                    title="Invalid Email ",
                    text="Please enter valid email.",
                    buttons=[
                        MDFlatButton(
                            text="OK",
                            on_release=lambda *args: invalid_credentials_dialog.dismiss()
                        )
                    ]
                    )
                    invalid_credentials_dialog.open()

                else:
                    Token = response_data["message"]
                    print(Token)
                    store.put('user', token = Token)
                    self.manager.current = 'home'

            else:
                print("Login failed. Please check your credentials.")

        # except ConnectionError:
        #     self.manager.current = 'error'
        except requests.ConnectionError:
             self.manager.current = 'error'
           
    def go_to_create_account(self):
        self.manager.current = 'create_account'
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
        # Get the username and password from the text fields
        email = self.ids.email.text
        password = self.ids.passwd.text
        # Make a request to the backend with the username and password
        url = 'http://localhost:8000/user/login/'  # Replace with your actual backend URL
        payload = {'email': email, 'password': password}
        response = requests.post(url, data=payload)

        # Process the response from the backend
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

    def go_to_create_account(self):
        self.manager.current = 'create_account'
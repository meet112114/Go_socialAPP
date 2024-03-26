from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import requests


Builder.load_file('libs/components/register.kv')

class CreateAccountScreen(Screen):
    def __init__(self, **kwargs):
        super(CreateAccountScreen, self).__init__(**kwargs)
        
        

    def create_account(self):
       # Get the username and password from the text fields
        first_name = self.ids.fname.text
        last_name = self.ids.lname.text
        username = self.ids.uname.text
        bio = self.ids.bio.text
        email = self.ids.email.text
        password = self.ids.passwd.text
        
        # Make a request to the backend with the username and password
        url = 'http://192.168.0.116:8000/user/create/'  # Replace with your actual backend URL
        payload = {'first_name':first_name ,'last_name' : last_name , 'username' : username , 'bio':bio ,  'email': email, 'password': password}
        response = requests.post(url, data=payload)

        # Process the response from the backend
        if response.status_code == 200 or 201:
            print("account created")
            print(response.text)
            self.manager.current = 'login'
            # Navigate to the next screen or perform other actions as needed
        else:
            print(response.status_code)

    def go_to_login_page(self):
        self.manager.current = 'login'
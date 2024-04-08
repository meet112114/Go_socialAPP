from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import requests
from kivy.uix.label import Label
from kivy.uix.popup import Popup


Builder.load_file('libs/components/complaint.kv')

class Complaint(Screen):
    def __init__(self, **kwargs):
        super(Complaint, self).__init__(**kwargs)
        
        

    def apply(self):
        name = self.ids.name.text
        enrollmentId = self.ids.enrollmentId.text
        yearAndDept = self.ids.yearAndDept.text
        sport = self.ids.Complaint.text
        
        url = 'http://localhost:8000/complaint/create/'  
        payload = {'name':name ,'enrollmentId' : enrollmentId , 'yearAndDept' : yearAndDept , 'Complaint':Complaint }
        response = requests.post(url, data=payload)

        
        if response.status_code == 200 or 201:
            print("account created")
            print(response.text)
            self.ids.name.text = ''
            self.ids.enrollmentId.text = ''
            self.ids.yearAndDept.text = ''
            self.ids.Complaint.text = ''
            
        else:
            print(response.status_code)
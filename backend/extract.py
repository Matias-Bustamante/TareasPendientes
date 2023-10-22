import pandas as pd 
import requests

class Extract: 
   
    url="https://script.google.com/macros/s/AKfycbxV-fOu1gyP_b66EUOhp82YZcGiqYHEzrjvkvlLHpD5OoMybzWhVByY0vfs6fJwFH60GA/exec"; 
    data:dict(); 
    def extract_data(self): 
        response=requests.get(url=self.url)
        if (response.status_code==200): 
            self.data=response.json(); 
            return self.data; 
        else: 
            print("Ocurrió un error de red")
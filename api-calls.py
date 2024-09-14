import requests
import json

def getMaze():
    url = "http://api.milabs.xyz/api-docs/v1/mazes"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = json.loads(response.json())
            print(data)
        
        else:
            print('Error', response.status_code)
            return None
        
    except requests.exceptions.RequestException as e:
        print('Error', e)
        return None
    
getMaze()
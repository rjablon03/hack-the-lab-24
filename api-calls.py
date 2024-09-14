import requests
import json

def getMaze():
    url = "http://api.milabs.xyz/v1/mazes"

    headers = {
        'X-Api-Key': "781200B275164705"
    }

    response = requests.get(url, headers=headers)

    return response.content

print(getMaze())
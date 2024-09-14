import requests

def getMazes():
    url = "http://api.milabs.xyz/v1/mazes"

    headers = {
        'X-Api-Key': "781200B275164705"
    }

    response = requests.get(url, headers=headers)

    return response.json()

def mazeSandbox(mazeId):
    url = f"http://api.milabs.xyz/v1/maze/{mazeId}"

    headers = {
        'X-Api-Key': "781200B275164705"
    }

    response = requests.get(url=url, headers=headers)

    return response.json()

def ratLocation(mazeId):
    url = f"https://api.milabs.xyz/v1/rat/{mazeId}/surroundings"

    headers = {
        'X-Api-Key': "781200B275164705"
    }

    response = requests.get(url,headers=headers)

    return response.json()

mazes = getMazes()
print(mazeSandbox(mazes[0]['id']))
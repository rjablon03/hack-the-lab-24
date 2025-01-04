import requests

def getMazes():
    url = "http://api.milabs.xyz/v1/mazes"

    headers = {
        'X-Api-Key': ""
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

def ratSurroundings(mazeId):
    url = f"http://api.milabs.xyz/v1/rat/{mazeId}/surroundings"

    headers = {
        'X-Api-Key': "781200B275164705"
    }

    response = requests.get(url, headers=headers)

    return response.json()

def moveRat(mazeId):
    url = f"http://api.milabs.xyz/v1/rat/move"

    headers = {
        'X-Api-Key': "781200B275164705"
    }
    payload = {
        "mazeId": mazeId,
        "direction": "NORTH"
    }
    print(ratSurroundings(mazeId)['type'])
    if ratSurroundings(mazeId)['type'] == 'Start':
        print(1)
        response = requests.post(url, headers=headers, json=payload)
        return response.json()

def exitMaze(mazeId):
    url = f"http://api.milabs.xyz/v1/rat/exit"

    headers = {
        'X-Api-Key': "781200B275164705"
    }

    payload = {
        "mazeId": mazeId
    }

    if ratSurroundings(mazeId)['type'] == "Exit":
        response = requests.post(url, headers=headers,json=payload)
        return response
    
    return "Error of some sort"




mazes = getMazes()
print(ratSurroundings(mazes[0]['id']))
print(moveRat(mazes[0]['id']))
print(ratSurroundings(mazes[0]['id']))

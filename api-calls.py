import requests

def getMazes():
    url = ""

    headers = {
        'X-Api-Key': ""
    }

    response = requests.get(url, headers=headers)

    return response.json()

def mazeSandbox(mazeId):
    url = f""

    headers = {
        'X-Api-Key': ""
    }

    response = requests.get(url=url, headers=headers)

    return response.json()

def ratSurroundings(mazeId):
    url = f""

    headers = {
        'X-Api-Key': ""
    }

    response = requests.get(url, headers=headers)

    return response.json()

def moveRat(mazeId):
    url = f""

    headers = {
        'X-Api-Key': ""
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
    url = f""

    headers = {
        'X-Api-Key': ""
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

import requests

API = 'https://futuramaapi.com/api/characters/'

def getCharacters(id):
    return requests.get(API+str(id)).json()
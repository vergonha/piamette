import requests
import json

def monsterByName(name):
    url = 'https://ragnarokapi.bravan.cloudns.cl/monsters/find/'
    action = {'search':name}
    resultsName = []
    resultsId = []

    r=requests.get(url,params=action)
    r=json.loads(r.content)
    for name in r:
        resultsName.append(name['name']['en'])

    for ids in r:
        resultsId.append(ids['id'])
    
    monsterList = list(zip(resultsName, resultsId))
    return monsterList





import requests
import json
import ragIdItem
from decouple import config

def checkMonster(id):
    apiKey = config('apiKey')
    url = f'https://www.divine-pride.net/api/database/monster/{id}?apiKey={apiKey}'
    r = requests.get(url)
    r = json.loads(r.content)
    monsterName = r['name']
    spawn = []
    drops = []
    dropsName = []
    for maps in r['spawn']:
        spawn.append(maps['mapname'])
    for itens in r['drops']:
        drops.append(itens['itemId'])
    for item in drops:
        name = ragIdItem.checkItemId(item)
        dropsName.append(name)

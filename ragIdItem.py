import requests
import json
import re
from decouple import config

def checkItemId(id, server='bRO'):
  apiKey = config('apiKey')
  try:
      url = f'https://www.divine-pride.net/api/database/Item/{id}?apiKey={apiKey}'
      r = requests.get(url)
      r = json.loads(r.content)
      desc = re.sub(r'\^([0-9A-Fa-f]{6})', '', r['description'])
      name = re.sub(r'\^([0-9A-Fa-f]{6})', '', r['name'])
      return name
  except:
    return "Could not locate the monster."
    

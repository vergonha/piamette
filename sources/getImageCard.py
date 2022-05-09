import requests
from bs4 import BeautifulSoup

def getImage(card):
    r = requests.get(f'https://www.divine-pride.net/database/item/{card}/').text
    if '<font color="#808080">Card</font>' in r:
        r = requests.get(f'https://static.divine-pride.net/images/items/cards/{card}.png')
        return r.content
    else:
        return 'This ID is not a card.'
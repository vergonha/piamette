from discord.ext import commands
import requests
import json
from bs4 import BeautifulSoup
import discord
from io import StringIO

class Item(commands.Cog):
    @commands.command()
    async def name(self, ctx, type, *name):
        if type.lower() == 'monster':
            name = " ".join(name)
            url = 'https://ragnarokapi.bravan.cloudns.cl/monsters/find/'
            action = {'search':name.lower()}
            resultsName = []
            resultsId = []
            try:
                r=requests.get(url,params=action)
                r=json.loads(r.content)
            except:
                await ctx.send('Could not fetch name.')
                return

            for name in r:
                resultsName.append(name['name']['en'])
            for ids in r:
                resultsId.append(ids['id'])
            
            monsterList = list(zip(resultsName, resultsId))
            monster = ''
            try:
                for i in range(0, len(monsterList)):
                    monster += f'\n**Name:** {monsterList[i][0]}\n**ID:**{monsterList[i][1]}\n'
                await ctx.send(f'**Matchs:**\n{monster}\n')
            except:
                await ctx.send('Could not fetch name.')
            
        elif type.lower() == 'item':
            name = ' '.join(name)
            url = f'https://db.irowiki.org/db/search/?quick={name[:-4]}&type=1'
            print(url)
            r = requests.get(url)
            soup = BeautifulSoup(r.content, 'html.parser')
            table = soup.findAll('table', attrs={'class':'bgLtTable'})
            records = ''
            name = []
            ids = []
            for item in table:
              records = item.findAll('a')
            for i in records:
              name.append(i.get_text())
            for i in records:
              i = i['href']
              i = i.replace('/db/item-info/', '')
              ids.append(i[:-1])

            itemList = list(zip(name, ids))
            item = ''
            try:
                for i in range(0, len(itemList)):
                    item += f'\n**Name:** {itemList[i][0]}\n**ID:**{itemList[i][1]}\n'
                if len(item) > 2000:
                    f = StringIO(item)
                    await ctx.send(file=discord.File(f, 'result.txt'))
                else:
                    await ctx.send(f'**Matchs:**\n{item}\n')
            except Exception as e:
                await ctx.send('Please, be more specific.')
                print(e)

                


     
def setup(client):
  client.add_cog(Item(client))
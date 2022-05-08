from discord.ext import commands
import requests
import json

class Item(commands.Cog):
    @commands.command()
    async def name(self, ctx, name):
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
        await ctx.send(monsterList)

     
def setup(client):
  client.add_cog(Item(client))
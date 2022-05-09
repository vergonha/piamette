from discord.ext import commands
import requests
import json

class Item(commands.Cog):
    @commands.command()
    async def name(self, ctx, name):
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

     
def setup(client):
  client.add_cog(Item(client))
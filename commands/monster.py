from discord.ext import commands
import requests
import json
import ragIdItem
from decouple import config


class Item(commands.Cog):
    @commands.command()
    async def monster(self, ctx, id):
        apiKey = config('apiKey')
        url = f'https://www.divine-pride.net/api/database/monster/{id}?apiKey={apiKey}'
        try:
          r = requests.get(url)
          r = json.loads(r.content)
        except:
            await ctx.send('Could not locate monster.')
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
        spawn = ', '.join(map(str, spawn)) 
        dropsName = ', '.join(map(str, dropsName))
        await ctx.send(f'\n\n{monsterName}\n\nSpawn: {spawn}\nDrops: {dropsName}')
     
def setup(client):
  client.add_cog(Item(client))
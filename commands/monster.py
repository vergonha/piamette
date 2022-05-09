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
        dropsChance = []
        amount = []
        for amounts in r['spawn']:
            amount.append(amounts['amount'])
        for drop in r['drops']:
            dropsChance.append(int(drop['chance'])/100)
        for maps in r['spawn']:
            spawn.append(maps['mapname'])
        for itens in r['drops']:
            drops.append(itens['itemId'])
        for item in drops:
            name = ragIdItem.checkItemId(item)
            dropsName.append(name)  
        dropNames = ''
        spawnList = ''
        for i in range(0, len(spawn)):
            spawnList += f'{spawn[i]} - *[{amount[i]}]*\n'
        for i in range(0, len(dropsName)):
            dropNames += f'{dropsName[i]} - *[{dropsChance[i]}%]*\n'
        await ctx.send(f'\n\n**{monsterName}**\n\n**Spawn:** \n{spawnList}\n**Drops:**\n{dropNames}')
     
def setup(client):
  client.add_cog(Item(client))
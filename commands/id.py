import re
from discord.ext import commands
import requests
import json
from decouple import config


class Item(commands.Cog):
  @commands.command()
  async def id(self, ctx, id, server=None):
    apiKey = config('apiKey')
    try:
      if server:
        servers = ['aro', 'bro', 'fro', 'idro', 'iro', 'jro', 'kro', 'kroz', 'mro', 'pro', 'ruro', 'thro', 'twro', 'cro', 'iroc']
        if server.lower() not in servers:
          await ctx.send('Invalid server.')
          return
        url = f'https://www.divine-pride.net/api/database/Item/{id}?apiKey={apiKey}&server={server}'
      else:
        url = f'https://www.divine-pride.net/api/database/Item/{id}?apiKey={apiKey}'
      r = requests.get(url)
      r = json.loads(r.content)
      desc = re.sub(r'\^([0-9A-Fa-f]{6})', '', r['description'])
      name = re.sub(r'\^([0-9A-Fa-f]{6})', '', r['name'])
      if name in "¼­´Ã¤Âï" or desc in "¼­´Ã¤Âï":
        await ctx.send("Try specifying the server.")
      else:
        await ctx.send(f'\n{name}\n\n{desc}')
        if 'Card' in name:
          await ctx.send(f'https://static.divine-pride.net/images/items/cards/{id}.png')
    except Exception as e:
      await ctx.send('Could not find the item.')
      print(e)

    
def setup(client):
  client.add_cog(Item(client))
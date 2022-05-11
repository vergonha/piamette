import re
from discord.ext import commands
import discord
import requests
import json
from decouple import config



class Item(commands.Cog):
  async def errorEmbed(self):
    url_image = 'https://thumbs.gfycat.com/LiquidPerkyBoaconstrictor-max-1mb.gif'

    embed = discord.Embed(
        description = f"Invalid syntax or missing item!",
        color=0xed377d,
    )

    embed.set_author(name=f"An error has occurred...")
    embed.add_field(name='-='*25, value=f"Please rewrite the command as follows:\n\n'**@id** [item id]'\n\n" + 'If you dont know the ID, try "@name item [name]" or "@name monster [name]"')
    embed.set_thumbnail(url=url_image)
    embed.set_footer(text=f"\nGithub.com/yuriwithdaggers") #Please, keep the credits.

    return embed

  async def embedItem(self, name, desc, img=''):
    url_image = img
    icon = 'https://static.ragnaplace.com/db/npc/gif/2257.gif'

    embed = discord.Embed(
        description = f"**Item name: {name}**",
        color=0x5cfa77,
    )

    embed.set_author(name=f"{name}", icon_url=icon)
    embed.add_field(name='-='*25, value=f'\n{desc}\n\n')
    embed.set_thumbnail(url=url_image)
    embed.set_footer(text=f"\nGithub.com/yuriwithdaggers") #Please, keep the credits.

    return embed

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
        if 'Card' in name:
          await ctx.send(embed=await self.embedItem(name, desc, f'https://static.divine-pride.net/images/items/cards/{id}.png'))
        else:
          await ctx.send(embed=await self.embedItem(name, desc, f'https://www.divine-pride.net/img/items/collection/iRO/{id}'))
    except Exception as e:
      await ctx.send(embed=await self.errorEmbed())
      print(e)

    
def setup(client):
  client.add_cog(Item(client))
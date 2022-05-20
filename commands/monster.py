from discord.ext import commands
import requests
import json
import ragIdItem
from decouple import config
import discord


class Item(commands.Cog):
    async def errorEmbed(self):
      url_image = 'https://thumbs.gfycat.com/LiquidPerkyBoaconstrictor-max-1mb.gif' 
      embed = discord.Embed(
          description = f"Invalid ID!",
          color=0xed377d,
      ) 
      embed.set_author(name=f"An error has occurred...")
      embed.add_field(name='-='*25, value=f'Please, verify if the ID you entered makes any sense...')
      embed.set_thumbnail(url=url_image)
      embed.set_footer(text=f"\nGithub.com/yuriwithdaggers") #Please, keep the credits. 
      return embed

    async def embedMonster(self, monsterName, spawnList, dropNames, img): 
        icon = 'https://static.ragnaplace.com/db/npc/gif/2257.gif'
        embed = discord.Embed(
            description = f"**Monster:**",
            color=0x5cfa77,
        )
        url_image = img
        embed.set_author(name=f"Search result:", icon_url=icon)
        embed.add_field(name='-='*25, value=f'**{monsterName}**\n\n**Spawn:** \n{spawnList}\n**Drops:**\n{dropNames}')
        embed.set_thumbnail(url=url_image)
        embed.set_footer(text=f"\nGithub.com/yuriwithdaggers") #Please, keep the credits.    
        return embed


    @commands.command()
    async def monster(self, ctx, id):
        apiKey = config('apiKey')
        url_icon = f'https://db.irowiki.org/image/monster/{id}.png'
        url = f'https://www.divine-pride.net/api/database/monster/{id}?apiKey={apiKey}'
        try:
          r = requests.get(url)
          r = json.loads(r.content)
        except:
            await ctx.send(embed=await self.errorEmbed())
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
        await ctx.send(embed=await self.embedMonster(monsterName, spawnList, dropNames, url_icon))
     
def setup(client):
  client.add_cog(Item(client))
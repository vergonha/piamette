from discord.ext import commands
import requests
import json
from bs4 import BeautifulSoup
import discord
from decouple import config
import urllib.request
import urllib.parse


class Item(commands.Cog):
    async def errorEmbed(self):
        url_image = 'https://thumbs.gfycat.com/LiquidPerkyBoaconstrictor-max-1mb.gif' 
        embed = discord.Embed(
            description = f"Invalid syntax or missing item!",
            color=0xed377d,)
        
        embed.set_author(name=f"An error has occurred...")
        embed.add_field(name='-='*25, value=f"Please rewrite the command as follows:\n\n'**@name** monster [monster name] \nor\n**name** item [item name]'\n\n")
        embed.set_thumbnail(url=url_image)
        embed.set_footer(text=f"\nGithub.com/yuriwithdaggers") #Please, keep the credits        
        return embed


    async def embedItem(self, desc): 
        icon = 'https://static.ragnaplace.com/db/npc/gif/2257.gif'
        embed = discord.Embed(
            description = f"**Matchs:**",
            color=0x5cfa77,
        )    
        embed.set_author(name=f"Search result:", icon_url=icon)
        embed.add_field(name='-='*25, value=f'\n{desc}\n\n')
        embed.set_footer(text=f"\nGithub.com/yuriwithdaggers") #Please, keep the credits.    
        return embed


    @commands.command()
    async def name(self, ctx, type, *name):
        pastebin = config('pastebinApi')
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
                await ctx.send(embed=await self.embedItem(monster))
            except:
                await ctx.send(embed=await self.errorEmbed())
            
        elif type.lower() == 'item':
            name = ' '.join(name)
            url = f'https://db.irowiki.org/db/search/?quick={name}&type=1'
            r = requests.get(url)
            if 'Item Info</div>' in r.text:
                redirectUrl = r.url
                redirectUrl = redirectUrl.replace('https://db.irowiki.org/db/item-info/', '')
                soup = BeautifulSoup(r.content, 'html.parser')
                idItem = redirectUrl[:-1]
                title = soup.find('table', attrs={'class':'bgMdTitle'})
                title = title.get_text().replace(f'\n', '')
                match = f'\n**Name:** {title}\n**ID:**{idItem}\n'
                await ctx.send(embed=await self.embedItem(match))
                return
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
                    site = 'https://pastebin.com/api/api_post.php'
                    our_data = urllib.parse.urlencode({"api_dev_key": pastebin, "api_option": "paste", "api_paste_code": item, 'api_paste_expire_date': '5M'})
                    our_data = our_data.encode()
                    request = urllib.request.Request(site, method='POST')
                    resp = urllib.request.urlopen(request, our_data)
                    resp = str(resp.read(), 'utf-8')
                    await ctx.send(embed=await self.embedItem(resp))
                else:
                    await ctx.send(embed=await self.embedItem(item))
            except Exception as e:
                await ctx.send(embed=await self.errorEmbed())
                print(e)

                


     
def setup(client):
  client.add_cog(Item(client))
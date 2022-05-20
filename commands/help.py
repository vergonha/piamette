import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def helpEmbed(self):
        url_image = 'https://thumbs.gfycat.com/LiquidPerkyBoaconstrictor-max-1mb.gif' 
        embed = discord.Embed(
            title = 'Commands:',
            description = f"Description of all commands:",
            color=0x26acff,
        )
        embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTSXY81Cv0-Z4Vyr1xEH6VoNEkhMfHS9kQkHWeFkUjZTE4jcrXut3Rr-M7U5yFxb_aHc60&usqp=CAU")
        embed.add_field(name='@id [item ID]', value=f"You need to send an item ID, if you don't know, use another command. Returns item information by ID.\n", inline=False)
        embed.add_field(name='@monster [monster ID]', value=f"You need to send an monster ID, if you don't know, use another command. Returns monster information by ID.\n", inline=False)
        embed.add_field(name='@name monster/item [name]', value=f'If you want a monster ID, use "name monster [name]", if you want an item, use "name item [name]\n', inline=False)
        return embed

    @commands.command()
    async def help(self, ctx):
        await ctx.send(embed=await self.helpEmbed())


def setup(client):
    client.remove_command("help")
    client.add_cog(Help(client))
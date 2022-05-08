import os
import discord
from discord.ext import commands
from decouple import config


client = commands.Bot(command_prefix="$")

@client.event
async def on_ready():
  print("Ragnarok.")


for filename in os.listdir('./commands'):
  if filename.endswith('.py'):
    client.load_extension(f'commands.{filename[:-3]}')  
  
TOKEN=config('TOKEN')
client.run(TOKEN)

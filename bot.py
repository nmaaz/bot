import discord
from discord.ext import commands
import os 

TOKEN = os.environ.get('TOKEN')
client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='DM FOR HELP \nwww.omegaesports.net \nprefix=!'))
    print("bot is ready")

@client.command()
async def ping(ctx):
    await ctx.send('pong :ping_pong:')
    
@client.command()
async def info(ctx):
    await ctx.send('**This bot is developed by Maaz#2031 , for any suggestion or problem DM \nBot language:Python** \n **prefix**=`!`')
    




@client.command()
async def staff(ctx):
    embed = discord.Embed(
      title ='Omega eSports Staff',
      description = 'Here is Omega eSports Staff',
      colour = discord.Colour.green()
    )

    embed.set_footer(text = 'Bot developed by maaz#2031')
    embed.add_field(name='Leader & Founder', value='AAsuitedAA', inline=False)
    embed.add_field(name= 'Administrator & Team Manager', value='Megha', inline=False)
    embed.add_field(name='Tournament Manager', value='Mr_Emix', inline=False)
    embed.add_field(name='International Clan Director', value='AhmedDiaa', inline=False)
    embed.add_field(name='CR Clans Director', value='Vianini', inline=False)
    embed.add_field(name='Comunication Directors', value='Alex \nAmicoMariom', inline=False)
    embed.add_field(name='Web Master', value='Matteo', inline=False)
    embed.add_field(name='Graphic designers', value='Matteo \nFlash', inline=False)
    embed.add_field(name='Social Managers', value='Matteo \nFeib')
    embed.add_field(name='Discord Manager', value='Maaz', inline=False)

    await ctx.send(embed=embed)

client.run(TOKEN)

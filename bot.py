import discord
from discord.ext import commands
import os

TOKEN = os.environ.get('TOKEN')
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("bot is ready")

@client.command()
async def ping():
    embed=discord.Embed(
    title='Ping!', 
    description='**Pong** :ping_pong:', 
    colour=discord.Colour.blue()
    )
    await client.say(embed=embed)


@client.command()
async def info():
    await client.say('**This bot is developed by Maaz#2031 , for any suggestion or problem DM \nBot language:Python** \n **prefix**=`.`')

@client.command()
async def staff():
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

    await client.say(embed=embed)


@client.command()
async def clans():
    embed=discord.Embed(
    title='Omega eSports Clans', 
    description='First of all please select the game you would like to see the clans', 
    colour=discord.Colour.red()
    )
    embed.add_field(name='```.cr```', value='To see all the omega Clash Royale Clans', inline=False)
    embed.add_field(name='```.ftn ```', value='To see the Omega Fortnite Clans', inline=False)
    embed.add_field(name='```.bs```', value='To see the Omega Brawl stars Clans', inline=False)
    embed.add_field(name='```.wh```', value='to see the Omega War Heroes Clans', inline=False)
    embed.add_field(name='```.tb```', value='To see all the Omega Toon Blast Clans', inline=False)
    await client.say(embed=embed)

@client.command()
async def cr():
    embed=discord.Embed(
    title='Omega eSports Clash Royale Clans', 
    description='First of all select the country you want to see the clans, to do so, use the following commands:',
    colour=discord.Colour.purple()
    )
    embed.add_field(name='```.INT```', value='To see all the Omega International clans', inline=False)
    embed.add_field(name='```.IT```', value='To see all the Omega Italian clans', inline=False)
    embed.add_field(name='```.EG```', value='To see all the Omega Egyptian Clans', inline=False)
    embed.add_field(name='```.JOR```', value='To see all the Omega Jordan Clans', inline=False)
    embed.add_field(name='```.GR```', value='To see all the omega Greek Clans', inline=False)
    embed.add_field(name='```.IND```', value='To see all the Omega Indian Clans', inline=False)
    embed.add_field(name='```.ES```', value='To see all the Omega Spanish Clans', inline=False)
    embed.add_field(name='```.MEX```', value='To see all the Omega Latam Clans', inline=False)
    await client.say(embed=embed)

@client.command()
async def INT():
    embed=discord.Embed(
    title='Omega eSports International Clans',
    description='Here are the Omega esports International Clans', 
    colour=discord.Colour.orange()
    )
    embed.add_field(name='Omega eSports', value='Omega eSports is the main clan that is used for the competitions and Omega tournaments.', inline=False)
    embed.add_field(name='Omega Request', value='Omega Request is the main Omega Req and Leave clan \n clan tag:**8C9UG2QG**', inline=False)
    await client.say(embed=embed)

@client.command()
async def IT():
    embed=discord.Embed(
    title='Omega eSports Italian Clans',
    description='Here are the Omega Italian Clans',
    colour=discord.Colour.green()
    )
    embed.add_field(name='Omega IT Legends', value='Omega ITLegends clans info \nClan Tag: **#8GUJ9J8G**\nClan trophies:46,875 Trophies, required trophies:4,300 \n***Link to view clan in-game***:arrow_right:https://link.clashroyale.com/?clanInfo?id=8GUJ9J8G :arrow_left: ***To do this you should open this link in your browswer.*** \nOmega ITLegends Accademies:\nItalianLegends2 | #8GC2LR92\nItalianLegends3 | #VGPY9PP3\nItalianLegends4 | #VLY0PYY4\nItalianLegends5 | #PGR2LPL')
    await client.say(embed=embed)
    
client.run(TOKEN)
    
    

import discord
from discord.ext import commands 
import os

client = commands.Bot(command_prefix= '>')
#events
@client.event
async def on_ready():
	await client.change_presence(game=discord.Game(name='www.omegaesports.net'))
	print('Bot is Online')
	print('-------------------')


#basic commands
@client.command(alises=["PING", "Ping"])
async def ping():
	embed=discord.Embed(
	title='Ping!',
	description='did you say **Ping**? i say **PONG** :ping_pong: ',
	colour=discord.Colour.green()		
	)
	await client.say(embed=embed)
@client.command(pass_context=True)
async def say(ctx, *, echo):
	if ctx.message.author.server_permissions.administrator:
		await client.delete_message(ctx.message)
		await client.say(echo)
	else:
		embed=discord.Embed(
		title='Permission Denied',
		description='Only an administrator can make me say something',
		colour=discord.Colour.red()	
		)
		await client.say(embed=embed)
#info command 
@client.command()
async def info():
	embed=discord.Embed(
	title='Bot info', 
	description='This bot is developed by <@375365255448231937> (maaz#2031), for any info or suggestion feel free to DM me',
	colour=discord.Colour.blue()
	)
	await client.say(embed=embed)
#moderation commands
#clear command
@client.command(pass_context=True)
async def clear(ctx, amount=0):
    if ctx.message.author.server_permissions.manage_messages:
        channel = ctx.message.channel
        messages = []
        async for message in client.logs_from(channel , limit= int(amount)):
    
            messages.append(message)
           
        await client.delete_messages(messages)
        await client.say(str(amount) + '`Messages Deleted`' )
  

     	
     	
      
#kick command
@client.command(pass_context=True)
async def kick(ctx, userName : discord.User):
	if ctx.message.author.server_permissions.kick_members:
		await client.kick(userName)
		await client.say('__**Succesfully kicked user**__')
	else:
		embed=discord.Embed(
		title='Permission Denied',
		description='You do not have the permission to kick someone :x: ', 
		colour=discord.Colour.red()
		)
		await client.say(embed=embed)
#ban command
@client.command(pass_context=True)
async def ban(ctx, member : discord.Member, days: int = 1 ):
	if ctx.message.author.server_permissions.ban_members:
		await client.ban(member, days)
		await client.say('succesfully banned member')
	else:
		embed=discord.Embed(
		title='Permission denied', 
		description='You do not have the permission to ban someone :x: ',
		colour=discord.Colour.red()				
		)
		await client.say(embed=embed)





















#staff command
@client.command(aliases=["STAFF", "Staff"])
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
#clans command
#main command
@client.command(aliases=["Clans", "CLANS"])
async def clans():
    embed=discord.Embed(
    title='Omega eSports Clans',
    description='First of all please select the game you would like to see the clans by using the following commands:',
    colour=discord.Colour.red()
    )
    embed.set_footer(text='my prefix is >')
    embed.add_field(name='```>ClashRoyale```', value='To see all the omega Clash Royale Clans', inline=False)
    embed.add_field(name='```>Fortnite ```', value='To see the Omega Fortnite Clans', inline=False)
    embed.add_field(name='```>BrawlStars```', value='To see the Omega Brawl stars Clans', inline=False)
    embed.add_field(name='```>WarHeroes```', value='to see the Omega War Heroes Clans', inline=False)
    embed.add_field(name='```>ToonBlast```', value='To see all the Omega Toon Blast Clans', inline=False)
    await client.say(embed=embed)
#clash royale
@client.command(aliases=["CLASHROYALE","clashroyale"])
async def ClashRoyale():
    embed=discord.Embed(
    title='Omega eSports Clash Royale Clans',
    description='First of all select the country you want to see the clans, to do so, use the following commands:',
    colour=discord.Colour.purple()
    )
    embed.add_field(name='```>International```', value='To see all the Omega International clans', inline=False)
    embed.add_field(name='```>Italy```', value='To see all the Omega Italian clans', inline=False)
    embed.add_field(name='```>Egypt```', value='To see all the Omega Egyptian Clans', inline=False)
    embed.add_field(name='```>Jordan```', value='To see all the Omega Jordan Clans', inline=False)
    embed.add_field(name='```>Greece```', value='To see all the omega Greek Clans', inline=False)
    embed.add_field(name='```>India```', value='To see all the Omega Indian Clans', inline=False)
    embed.add_field(name='```>Spain```', value='To see all the Omega Spanish Clans', inline=False)
    embed.add_field(name='```>Mexico```', value='To see all the Omega Latam Clans', inline=False)
    await client.say(embed=embed)
#CR INT
@client.command(aliases=["INTERNATIONAL","international"])
async def International():
    embed=discord.Embed(
    title='Omega eSports International Clans',
    description='Here are the Omega esports International Clans',
    colour=discord.Colour.orange()
    )
    embed.add_field(name='Omega eSports', value='Omega eSports is the main clan that is used for the competitions and Omega tournaments.', inline=False)
    embed.add_field(name='Omega Request', value='Omega Request is the main Omega Req and Leave clan \n clan tag:**8C9UG2QG**', inline=False)
    await client.say(embed=embed)
#CR IT
@client.command(aliases=["ITALY", "italy"])
async def Italy():
    embed=discord.Embed(
    title='Omega eSports Italian Clans',
    description='Here are the Omega Italian Clans',
    colour=discord.Colour.green()
    )
    embed.add_field(name='Omega IT Legends', value='Omega ITLegends Clans info \nClan Tag: **#8GUJ9J8G** \nClan trophies:46,875 Trophies, required trophies:4,300 \nOmega ITLegends Accademies:\nItalianLegends2 | #8GC2LR92\nItalianLegends3 | #VGPY9PP3\nItalianLegends4 | #VLY0PYY4\nItalianLegends5 | #PGR2LPL', inline=False)
    embed.add_field(name='Omega ITC', value='Omega ITC clans info \n Clan Tag:***#90G8Y8GP*** \nClan Trophhies:44,550 Trophies, required trophies:4,300 \nOmega ITC Accademies: \nOmega ITC 2 | #8RUVQ99R \nIT Champions | #L9Q88 \n ITMiniChampions | #8YURV2J \nITMegaChampions | #UJUVYRR \n ITBatsChampions | #GCCGG00',inline=False)
    embed.add_field(name='Omega Mugiwara', value='Omega Mugiwara Clans info \nClan Tag:**#90RR92PJ** \nClan trophies:45,274 Trophies, required trophies:4,300 \nOmega Mugiwara Accademies: \nOmega Mugiwara2 | #8QU0Q9GJ', inline=False)
    embed.add_field(name='Omega Napoles', value='Omega Napoles Clans Info \nClan Tag:**#8C98CGJR** \n Clan trophies: 43,771 Trophies, required trophies:4,000 \nOmega Napoles Accademies: \nOmega Napoles 2 | #8RJ9LVCP', inline=False)
    embed.add_field(name='Omega Eclipse', value='Omega Eclipse Clans info \nClan Tag:**#8RUPU2UR** \n Clan trophies:45,002 Trophies, required trophies:4,300 \nOmega Eclipse Accademies: \nSnack Away | #QGVQC2Y \nOmega Eclipse2 | #8UYL2GGQ', inline=False)
    embed.add_field(name='Omega Fighters', value='Omega Fighters Clans Info \nClan Tag:**#8Q2JV0QV** \n Clan trophies:45,238 Trophies, required trophies:4,300 \nOmega Fighters Accademies:Omega Fighters1 | #8R9GO9Q9 \nOmega Fighters2 | #8QV98G8J', inline=False)
    embed.add_field(name='Omega Insane', value='Omega Insane Clans info \nClan Tag:**#8VUU8RLJ** \n Clan trophies:44,185 Trophies, required trophies:4,300 \nOmega Insane Accademies: \nOmega Insane 2 | #9L9UQJ2U', inline=False)
    await client.say(embed=embed)
#CR EG
@client.command(aliases=["EGYPT", "egypt"])
async def Egypt():
    embed=discord.Embed(
    title='Omega eSports Egyptian clans',
    description='Here are the Omega Egyptian Clans',
    colour=discord.Colour.dark_green()
    )
    embed.add_field(name='Egypt Omega', value='Egypt Omega Clans info \nClan Tag:**#8ULC0LR2** \n Clan trophies: 45,713 Trophies , required trophies:4,300 \nEgypt Omega Accademies: \nEgypt Omega 1 (4600) \nEgypt Omega 2 (4300) \nEgypt Omega 3 (4000) \nEgypt Omega 4 (3800) \nEgypt Omega 5 (3600) \nEgypt Omega 6 (3400) \nEgypt Omega 7 (3200)', inline=False)
    await client.say(embed=embed)
#CR JOR
@client.command(aliases=["jordan", "JORDAN"])
async def Jordan():
    embed=discord.Embed(
    title='Omega eSports Jordan Clans',
    description='Here ere the Omega Jordan Clans',
    colour=discord.Colour.gold()
    )
    embed.add_field(name='Omega Jo', value='Omega Jo Clans info \nclan Tag:**#9GQJ2G0G** \nClan trophies:42,422 Trophies, required trophies:4,300 \nOmega Jo Accademies: \nOmega™ Jo II | #92RL0R8U \nOmega™ Jo III | #998LVPY8', inline=False)
    await client.say(embed=embed)
#CR GR    
@client.command(aliases=["GREECE", "greece"])
async def Greece():
    embed=discord.Embed(
    title='Omega esports Greek Clans',
    description='Here are the Omega Greek clans',
    colour=discord.Colour.red()
    )
    embed.add_field(name='Omega Hellas', value='Omega Hellas clans info \nClan tag:**#9PR0Y2L9**\nClan trophies:44,165 Trophies, required trophies:4,300 \nOmega Hellas Accademies: \nOmega™ Hellas2 | #PGVJJY8', inline=False)
    await client.say(embed=embed)
 #CR IND
@client.command(aliases=["INDIA", "india"])
async def India():
    embed=discord.Embed(
    title='Omega eSports Indian Clans',
    description='here are the Omega India Clans',
    colour=discord.Colour.orange()
    )
    embed.add_field(name='Omega India', value='Omega India Clans info \nClan Tag:**#9YPPJVQU** \nClan trophies:45,279 Trophies, required trophies:4,300 \nOmega India Accademies: \nOmega™ India ♥️ | #9PYGCJ28 \nOmega™ India ♠️ | #9P80G9VY \nOmega™ India ♦️ | #P8PU098P \nOmega™ India ♣️ | #9U00UV28 \nOmega™ IND FuZe | #P8LV082', inline=False)
    await client.say(embed=embed)
#CR LATAM
@client.command(aliases=["mexico", "MEXICO"])
async def Mexico():
    embed=discord.Embed(
    title='Omega eSports LATAM Clans',
    description='Here are the Omega LATAM Clans',
    colour=discord.Colour.dark_orange()
    )
    embed.add_field(name='Omega Latam', value='Omega Latam Clans info \nClan Tag:**#9Y0PLURU** \n Clan trophies:46,472 Trophies, required trophies:4,300 \nOmega Latam Accademies: \n Omega™ Masters | #9Y8Q0QVY', inline=False)
    await client.say(embed=embed)
 #CR SPAIN
@client.command(aliases=["SPAIN", "spain"])
async def Spain():
    embed=discord.Embed(
    title='Omega eSports Spanish Clans',
    description='Here are the Omega Spanish Clans',
    colour=discord.Colour.gold()
    )
    embed.add_field(name='Omega GSD Spain', value='Omega GSD Spain Clans info \nClan tag:**#9P82PUCU** \nClan trophies:44,494 Trophies, required trophies: 4,300 \nOmega GSD Spain Accademies: \nOmega GSD Spn 1 | #P8QCC8GO \nOmega GSD Spn 2 | #9L89YQ9Q \nOmega GSD Spn 3 | #P8QYGRJG \nOmega GSD Spn 4 | #9UOCQCRY', inline=False)
    await client.say(embed=embed)
#FORTNITE
@client.command(aliases=["FORTNITE", "fortnite"])
async def Fortnite():
    embed=discord.Embed(
    title='Omega eSports Fortnite Clans',
    description='Here are the Omega Fortnite Clans',
    colour=discord.Colour.blue()
    )
    embed.add_field(name='Omega fortnite', value='Members: \nOmega BeaMix \nOmega-Kirin0 \nOmega-WhiteSmoke \nOmega-Dragon19 \nOmega-Jack \nOmega-Justzako \nOmega Vava \nOmega Pikko1 \nOmega_Smart \nOmega-Jacopotto \nOmega-junder \nOmega_Giogio \nOmega Micene \nOmega-Princee \nOmega M4sk \nOmega-KingBosee \nOmega-Pusher \nOmega-Krybe \nOmega-Ovlasfire \nOmega-Cavity', inline=False)
    await client.say(embed=embed)
#BRAWLSTARS
@client.command(aliases=["BRAWLSTARS", "brawlstars"])
async def BrawlStars():
    embed=discord.Embed(
    title='Omega eSports Brawl Stars Clans',
    description='Here are the Omega Brawl Stars Clans',
    colour=discord.Colour.purple()
    )
    embed.add_field(name='Omega eSports', value='Omega eSports clan info \nBand Tag:**#Q80UQRL** \nRequired Trophies:5500', inline=False)
    await client.say(embed=embed)
#WAR HEROES
@client.command(aliases=["WARHEROES", "warheroes"])
async def WarHeroes():
    embed=discord.Embed(
    title='Omega eSports War Heroes Clans',
    description='Here are the Omega War Heroes Clans',
    colour=discord.Colour.green()
    )
    embed.add_field(name='Omega Heroes', value='Omega Heroes Clan info \n Clan Medals:36.000, required medals:3500 \nOmega Heroes Accademies:\n ★ITA HEROES★ \n★ITA HEROES 2★ \n★ITA HEROES 2★',inline=False)
    await client.say(embed=embed)
#TOON BLAST
@client.command(aliases=["TOONBLAST", "toonblast"])
async def ToonBlast():
    embed=discord.Embed(
    title='Omega eSports Toon Blast Clans',
    description='Here are the Omega Toon Blast Clans',
    colour=discord.Colour.magenta()
    )
    embed.add_field(name='Omega eSports', value='required Level:350')
    await client.say(embed=embed)




client.run(os.environ.get('TOKEN'))

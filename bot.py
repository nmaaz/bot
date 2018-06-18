import discord
from discord.ext import commands
import os 

client=commands.Bot(command_prefix='.')
@client.event
async def on_ready():
	print('Bot is Online')
	await client.change_presence(game=discord.Game(name='Modern Gaming'))
@client.event
async def on_member_join(member):
	if member.server.id=="439171643349139496":
		msg= member.mention+', Welcome to **Modern Gaming League** \n\nFirst of all please read our **rules** in <#439172562371739698> \n\nLook at <#439172731611643904> for more info about Modern Gaming League and important news \n\nYou want to submit a project , want to sponsor us or ask questions about our organisation ?**Contact the admins!** \n\nFollow us! \nwww.twitter.com/GamModern \nEnjoy your time here!'
		await client.send_message(client.get_channel("439171643349139498"), msg)
@client.command()
async def ping():
	await client.say('Pong! :ping_pong:')
client.run(os.environ.get('TOKEN'))

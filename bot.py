import discord
from discord.ext import commands
import os 

client=commands.Bot(command_prefix='.')
client.remove_command('help')
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

	
@client.command()
async def invite():
	embed=discord.Embed(
	title='Modern Gaming server invite link',
	colour=discord.Colour.green()	
	)
	embed.add_field(name='Open the invite link', value='To open the invite link click [here](https://discord.gg/ZsmVZxq)', inline=False)
	embed.add_field(name='Copy the invite link', value='To copy the invite link you can use the following command`.dminvite`')
	await client.say(embed=embed)

@client.command(pass_context=True)
async def dminvite(ctx):
	author=ctx.message.author
	inv='https://discord.gg/ZsmVZxq'
	await client.send_message(author, inv)
	await client.say('Invite link sent in DM ')
	
@client.command(pass_context=True)
async def mute(ctx, member : discord.Member):
	if ctx.message.author.server_permissions.administrator:
		role = discord.utils.get(member.server.roles, name='Muted')
		await client.add_roles(member, role)
		await client.say('**Succesfully Muted user**')
	else:
		embed=discord.Embed(
		title='Permission Denied',
		description='You do not have the permission to mute :x: ',
		colour=discord.Colour.red()
		)
		await client.say(embed=embed)
		
@client.command(pass_context=True)
async def unmute(ctx, member : discord.Member):
	if ctx.message.author.server_permissions.administrator:
		role= discord.utils.get(member.server.roles, name='Muted')
		await client.remove_roles(member, role)
		await client.say('**Successfully unmuted user**')
	else:
		embed=discord.Embed(
		title='Permission Denied',
		description='You do not have the permission to unmute :x: ',
		colour=discord.Colour.red()
		
		)
		await client.say(embed=embed)
		
@client.command(pass_context=True)
async def kick(ctx, userName : discord.User):
	if ctx.message.author.server_permissions.kick_members:
		await client.kick(userName)
		await client.say('**Succesfully kicked user**')
	else:
		embed=discord.Embed(
		title='Permission Denied',
		description='You do not have the permission to kick someone :x: ', 
		colour=discord.Colour.red()
		)
		await client.say(embed=embed)
	


	
	
client.run(os.environ.get('TOKEN'))

 		
@client.command(pass_context=True)
async def say(ctx, *, echo):
	if ctx.message.author.server_permissions.administrator:
		await client.delete_message(ctx.message)
		await client.say(echo)
	else:
		embed=discord.Embed(
		title='Permission Denied',
		description='You do not have the permission :x: ',
		colour=discord.Colour.red()	
		)
		await client.say(embed=embed)
		
		
@client.command(pass_context=True)
async def announce(ctx, *, msg):
	if ctx.message.author.server_permissions.administrator:
		
		await client.say('@everyone '+msg)
		await client.delete_message(ctx.message)
	else:
		embed=discord.Embed(
		title='Permission Denied',
		description='You do not have the permission :x: ',
		colour=discord.Colour.red()
		
		
		)
		await client.say(embed=embed)
@client.command()
async def modern():
	await client.say('Noob')
	
@client.command()
async def diego():
	await client.say('gayyyyyy')
	
@client.command()
async def düster():
	await client.say('german pro player')
	
@client.command(pass_context=True)
async def status(ctx, *, status):
	if ctx.message.author.id == '375365255448231937':
		await client.change_presence(game=discord.Game(name=status))
		await client.say('Status changes to: '+status)
	else:
		await client.say('Hahah Noob, you cannnot command me :new_moon_with_face:  ')
 


@client.command(pass_context=True)
async def bot(ctx, *, text):
	list = ['Yes', 'No', 'Maybe']
	await client.say(random.coice(list))
	

		
	
	


	
	
client.run(os.environ.get('TOKEN'))


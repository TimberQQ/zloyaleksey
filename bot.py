import discord
from discord.ext import commands
client = commands.Bot ( command_prefix = ';' )

@client.event

async def on_ready():
	print ( 'Bot connected' )

@client.command( pass_context = True )
@commands.has_permissions( administrator = True)
async def stream(ctx):
	await ctx.send('**@everyone Начался стрим https://www.twitch.tv/zloyaleksey**' )

@client.command( pass_context = True )
@commands.has_permissions( administrator = True)
async def clear ( ctx, amount = 100 ):
	await ctx.channel.purge ( limit = amount )
	
@client.command( pass_context = True )
async def say(ctx,arg):

	await ctx.send(arg)
	
client.run ('NzIyOTA1ODYwNTAxNjY3OTA1.Xutalw.jFBL-PT4_c4NMP8yGRjgyKCXMTA')
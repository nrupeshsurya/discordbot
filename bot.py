import os
import discord
from discord.ext import commands
import random 
import unoscript
import script

TOKEN = 'enter_token'
GUILD = 'enter_guild_name'
client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event 
async def on_member_join(member):
    print(f'{member} has joined the server.')

@client.event 
async def on_member_remove(member):
    print(f'{member} has left the server.')

@client.command()
async def marco(ctx):
    await ctx.send('Polo!')

@client.command(aliases=['8ball'])
async def _8ball(ctx,*,question):
    answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes Signs point to yes', 'Reply hazy', 'try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(answers)}')

@client.command()
async def spotify(ctx,*,link):
    url = unoscript.func(link)
    await ctx.send(url)

@client.command()
async def ytmusic(ctx,*,link):
    url = script.func(link)
    await ctx.send(url)
    
client.run(TOKEN)

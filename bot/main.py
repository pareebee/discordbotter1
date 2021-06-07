import discord
import os
import random
import server
import aiohttp
from discord.ext import commands

names = []
intents = discord.Intents(messages=True, guilds=True)

Client = commands.Bot(command_prefix = '/', intents = discord.Intents.all())
TOKEN = os.getenv("DISCORD_TOKEN")


@Client.event
async def on_ready():
    print('Bot is ready.')
    for guild in Client.guilds:
          for member in guild.members:
            name = member.name 
            print (name)
            names.append(name)

@Client.command(name="minutes")
async def some_crazy_function_name(ctx):
  name = random.choice(names)
  await ctx.channel.send("The notetaker for today's meeting is "+ name + ":)")


@Client.command (name="link") 
async def link(ctx): 
        embed = discord.Embed(
            color= discord.Colour.orange() # or any color you want
        )
        embed.add_field(name='Click here to join the meeting' ,value='[Zoom Meeting]( https://mit.zoom.us/j/93236606772 )', inline=False)
        await ctx.send(embed=embed)
       
@Client.command(pass_context=True)
async def cat(ctx):
    embed = discord.Embed(title="", description="")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/lolcats/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)

server.server()
Client.run(TOKEN)

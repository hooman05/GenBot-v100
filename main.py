
# imports

# discord.py
# import discord
from discord import Embed
from discord.ext import commands

# misc
import os
import brainfuck
import json
# end of imports

MyID    = 627107225109790730
bfWiki  = "https://en.wikipedia.org/wiki/Brainfuck"
bfengi  = "https://github.com/DismissedGuy/brainfuck-interpreter"

os.chdir('./')
print('current working direcotry:\n'+os.getcwd())

bot = commands.Bot(command_prefix='//')  # bot prefix
bot.remove_command('help')

# initally loading extentions
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

# inital setting

"""=========== STARTUP =========="""
@bot.event
async def on_ready():
    print('main booted!')
    print('starting cogs...\n===============================')
"""========== FINISHED ==========="""

# load and unload cogs
@bot.command()
async def cog(ctx, action, extention):
    if ctx.message.author.id == MyID:
        if action == 'load':
            bot.load_extension(f'cogs.{extention}')
            print(f'{extention} was Loaded')
        elif action == 'unload':
            bot.unload_extension(f'cogs.{extention}')
            print(f'{extention} was Loaded')
        elif action == 'reload':
            bot.unload_extension(f'cogs.{extention}')
            bot.load_extension(f'cogs.{extention}')
            print(f'{extention} was reloaded')
        else:
            ctx.send('thats not a valid action')
    else:
        ctx.send('only the bot owner can use this...')

@bot.command()
async def pingmain(ctx):
    await ctx.send(f'I am running at: {round(bot.latency * 1000)}ms Ping')
    print("bot latency checked")

@bot.command()
async def brainf(ctx, *, code):
    output = brainfuck.evaluate(code)
    embed  = Embed(title="Here is your result", color=0x00e1ff)
    embed.add_field(name="the output of your code is:", value=f"```{output}```", inline=False)
    embed.add_field(name="the input code was:", value="```"+code+"```", inline=False)
    embed.set_footer(text="requested by <@{}>".format(ctx.message.author.id))
    await ctx.send(embed=embed)

@bot.command()
async def brainfhelp(ctx):
    embed = Embed(title="need help?", color=0x00e1ff)
    embed.add_field(name="try checking the wiki:",           value=f"[Brainf wiki]({bfWiki})",          inline=False)
    embed.add_field(name="enterpreter engine github page:",  value=f"[Go to github page]({bfengi})",    inline=False)
    await ctx.send(embed=embed)

"""
file = open('./token.txt', 'r')
Token = file.read()
print('token: ' + Token)
# bot.run(Token)
"""
with open('data.json') as json_file:
    data = json.load(json_file)
    bot.run(data['token'])

    bot.run(data['token'])

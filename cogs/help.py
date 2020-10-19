from discord.ext import commands
from discord import Embed
import json

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Help ------------- online')

    @commands.command()
    async def help(self, ctx):
        with open('help.json') as file:
            jsondat = json.load(file)
            embed = Embed(title=jsondat['title'], color=jsondat['color'], description=jsondat['description'])
            await ctx.author.send(embed=embed)

            # templates
            # Embed(title=jsondat['fields'][ ]['name'], color=jsondat['color'], description=jsondat['fields'][ ]['value'])
            # add_field(name=jsondat['fields'][ ]['name'], value=jsondat['fields'][ ]['value'], inline=False)

            # Miscilanous commands
            misch = Embed(title=jsondat['fields'][0]['name'], color=jsondat['color'], description=jsondat['fields'][0]['value'])
            misch.add_field(name=jsondat['fields'][1]['name'], value=jsondat['fields'][1]['value'], inline=False)  # brainfuck
            misch.add_field(name=jsondat['fields'][2]['name'], value=jsondat['fields'][2]['value'], inline=False)  # brainfuck resources
            misch.add_field(name=jsondat['fields'][5]['name'], value=jsondat['fields'][5]['value'], inline=False)  # tex rendering
            await ctx.author.send(embed=misch)

            # Moderation commands
            modh = Embed(title=jsondat['fields'][3]['name'], color=jsondat['color'], description=jsondat['fields'][3]['value'])
            modh.add_field(name=jsondat['fields'][4]['name'], value=jsondat['fields'][4]['value'], inline=False)  # purge
            await ctx.author.send(embed=modh)

            await ctx.send(f'<@{ctx.author.id}> Check your dms, for your command cheat-sheet.')

def setup(bot):
    bot.add_cog(help(bot))

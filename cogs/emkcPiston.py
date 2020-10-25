from discord.ext import commands
import aiohttp
import re
import discord

api = 'https://emkc.org/api/v1/piston/execute'

""" Payload |
    Base    : https://emkc.org/api/v1/piston
    Send to : /execute with POST

{
    "language": "js",
    "source": "console.log(process.argv)",
    "args": [
        "1",
        "2",
        "3"
    ]
}

"""

regex  = re.compile(r'(?s)//run(?: +(?P<language>\S*)\s*|\s*)```(?:(?P<syntax>\S+)\n\s*|\s*)(?P<source>.*)```')
Colour = 0xa72e1

class PistonAPI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('piston ----------- online')

    async def APIrequest(self, Input):
        async with aiohttp.ClientSession() as session:
            async with session.post(api, json=Input) as req:
                req.raise_for_status()
                recieved = await req.json()
                # recieved = json.loads(recieved)
                # print(recieved)
                if "ran" in recieved:
                    return recieved

    @commands.command()
    async def run(self, ctx):
        await ctx.send('please wait while the request is processed...')
        async with ctx.message.channel.typing():
            match = regex.search(ctx.message.content)
            lang, syn, src = match.groups()

            data = {'language': lang, 'source': src}

            result = await self.APIrequest(data)

            embed = discord.Embed(
                title="here is your output:",
                colour=discord.Colour(Colour)
            )
            embed.add_field(name="the output of your code is:", value=f"```{result['output']}```", inline=False)
            embed.add_field(
                name="details:",
                value=f"```md\n<language: {result['language']}>\n<version: {result['version']}>```",
                inline=False
            )
            await ctx.send(embed=embed)


r'''
# await ctx.send(f'lang: {lang}\ncode: {code}')
# await ctx.send(ctx.message.content)
content = ctx.message.content
# extract data from message content
m = re.search(regex, content)
language = re.group(0)
syntax   = re.group(1)
code     = re.group(3)
await ctx.send(f'language: {language}\nMD syntax: {syntax}\ncode: {code}')
'''

def setup(bot):
    bot.add_cog(PistonAPI(bot))

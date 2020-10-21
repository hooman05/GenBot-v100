from discord.ext import commands
import aiohttp
import re

""" Payload
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

# some code is sampled from https://github.com/engineer-man/piston-bot/

# regex; sampled from pistonBot by engineer man
regex = r'(?s)/(?:edit_last_)?run(?: +(?P<language>\S*)\s*|\s*)```(?:(?P<syntax>\S+)\n\s*|\s*)(?P<source>.*)```' 

# i removed the args section as i dont need it right now, i may try to use it in the future.

class PistonAPI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def APIrequest(self, Input):

    @commands.command()
    async def run(self, ctx):
        # await ctx.send(f'lang: {lang}\ncode: {code}')
        # await ctx.send(ctx.message.content)
        content = ctx.message.content
        # extract data from message content
        m = re.search(regex, content)
        language = re.group(0)
        syntax   = re.group(1)
        code     = re.group(3)
        await ctx.send(f'language: {language}\nMD syntax: {syntax}\ncode: {code}')

def setup(bot):
    bot.add_cog(PistonAPI(bot))

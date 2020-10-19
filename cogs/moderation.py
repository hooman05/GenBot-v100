from discord.ext import commands
from discord.ext.commands import has_permissions

import time
# varibles
RenderingServer = "http://rtex.probablyaweb.site/api/v2"
DocStart        = r"\documentclass{article}\usepackage{xcolor}\begin{document}\color{white}"
DocEnd          = r"\pagenumbering{gobble}\end{document}"

Colour          = 0xa72e1

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('mooderation ------ online')

    @commands.command()
    @has_permissions(manage_messages=True)
    async def purge(self, ctx, amount):
        limit = int(amount)
        limit += 1
        await ctx.channel.purge(limit=limit)
        await ctx.send(f'deleted {amount}, messages')
        time.sleep(1)
        await ctx.channel.purge(limit=1)

def setup(bot):
    bot.add_cog(Moderation(bot))

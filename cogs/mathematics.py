import discord
from discord.ext import commands

import typing
import aiohttp
import aiofiles

# varibles
RenderingServer = "http://rtex.probablyaweb.site/api/v2"
DocStart        = r"\documentclass{article}\usepackage{xcolor}\begin{document}\color{white}"
DocEnd          = r"\pagenumbering{gobble}\end{document}"

Colour          = 0xa72e1

class MathModule(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def RetrieveImage(self, InputCode):
        payload = {
            'code': InputCode,
            'format': 'png',
            'quality': 50,
            'density': 300
        }
        # print(payload)
        async with aiohttp.ClientSession() as session:
            async with session.post(RenderingServer, json=payload) as request:
                request.raise_for_status()
                data = await request.json()
                if data['status'] == 'error':
                    # print(data['log'])
                    data['log'] = '...'
                    # print(data)
                    # print('Something happend')
                    filelink = 'https://raw.githubusercontent.com/hooman05/ImageDump/master/Error.png'

                elif data['status'] == 'success':
                    filelink = RenderingServer + '/' + data['filename']

            async with session.get(filelink, timeout=3) as GetImage:
                GetImage.raise_for_status()
                if GetImage.status == 200:
                    bucket = await aiofiles.open('./tmp/RenderdImage.png', mode='wb')
                    await bucket.write(await GetImage.read())
                    await bucket.close()

    @commands.Cog.listener()
    async def on_ready(self):
        print('Maths ------------ online')

    @commands.command()
    async def pingMath(self, ctx):
        await ctx.send(f'MathModule is running at: {round(self.bot.latency * 1000)}ms Ping!')

    @commands.command()
    async def tex(self, ctx, advancedopt: typing.Optional[str], *, code=r'input somthing.'):
        await ctx.send('please wait while the request is processed...')
        async with ctx.message.channel.typing():
            if advancedopt == 'hard':
                # dataIn =
                await self.RetrieveImage(code)
                embed = discord.Embed(
                    title='here is your output:',
                    colour=discord.Colour(Colour)
                )
                try:
                    file = discord.File("./tmp/RenderdImage.png", "rtex.png")
                    embed.set_image(url="attachment://rtex.png")
                    embed.set_footer(text='Setting the page colour is recommended in hard mode.')
                except FileNotFoundError():
                    file = discord.File("./tmp/Error.png", "err.png")
                    embed.set_image(url="attachment://err.png")

            elif advancedopt == 'easy':
                simpleCode = DocStart + code + DocEnd
                # print("\n===============================")
                # print(simpleCode)
                # print("===============================")
                await self.RetrieveImage(simpleCode)
                embed = discord.Embed(
                    title="here is your output:",
                    colour=discord.Colour(Colour)
                )
                file = discord.File("./tmp/RenderdImage.png", "rtex.png")
                embed.set_image(url="attachment://rtex.png")
            else:
                pass
        await ctx.channel.purge(limit=1)
        try:
            await ctx.send(file=file, embed=embed)
        except FileNotFoundError():
            await ctx.send('somthing happend :(')

def setup(bot):
    bot.add_cog(MathModule(bot))

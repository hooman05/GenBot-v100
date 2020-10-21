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

class PistonAPI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.languages = {
            'asm': 'nasm',
            'asm64': 'nasm64',
            'awk': 'awk',
            'bash': 'bash',
            'bf': 'brainfuck',
            'brainfuck': 'brainfuck',
            'c': 'c',
            'c#': 'csharp',
            'c++': 'cpp',
            'cpp': 'cpp',
            'cs': 'csharp',
            'csharp': 'csharp',
            'deno': 'deno',
            'denojs': 'deno',
            'denots': 'deno',
            'duby': 'ruby',
            'el': 'emacs',
            'elisp': 'emacs',
            'emacs': 'emacs',
            'elixir': 'elixir',
            'haskell': 'haskell',
            'hs': 'haskell',
            'go': 'go',
            'java': 'java',
            'javascript': 'javascript',
            'jelly': 'jelly',
            'jl': 'julia',
            'julia': 'julia',
            'js': 'javascript',
            'kotlin': 'kotlin',
            'lua': 'lua',
            'nasm': 'nasm',
            'nasm64': 'nasm64',
            'node': 'javascript',
            'perl': 'perl',
            'php': 'php',
            'php3': 'php',
            'php4': 'php',
            'php5': 'php',
            'py': 'python3',
            'py3': 'python3',
            'python': 'python3',
            'python2': 'python2',
            'python3': 'python3',
            'r': 'r',
            'rb': 'ruby',
            'ruby': 'ruby',
            'rs': 'rust',
            'rust': 'rust',
            'sage': 'python3',
            'swift': 'swift',
            'ts': 'typescript',
            'typescript': 'typescript',
        }

    async def checkSyn(self, input):
        if input.message.content.count('```') != 2:
            await input.send('bad input. missing codeblocks')

    @commands.command()
    async def run(self, ctx):
        # await ctx.send(f'lang: {lang}\ncode: {code}')
        await ctx.send(ctx.message.content)

def setup(bot):
    bot.add_cog(PistonAPI(bot))

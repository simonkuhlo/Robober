import discord
import settings
from dotenv import get_key
from termcolor import colored
from logger import log
from logger.res import DefaultLogLevels
from discord.ext import commands
from colorama import just_fix_windows_console
just_fix_windows_console()

class ReelBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        intents.message_content = True
        super().__init__(command_prefix=commands.when_mentioned_or(settings.command_trigger), intents=intents)

    #async def setup_hook(self) -> None:
        #self.tree.copy_global_to(guild=discord.Object(id=v.GUILD))
        #await self.tree.sync(guild=discord.Object(id=v.GUILD))

    async def on_ready(self):
        message = colored(colored('LOGGED IN', 'white', 'on_green', ['bold'])+' as '+colored(f"{self.user}", 'blue')+f' (ID: {self.user.id})')
        log(message, DefaultLogLevels.INFO)

bot = ReelBot()

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(get_key(".env",'BOT_TOKEN'))
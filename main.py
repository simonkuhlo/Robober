import discord
import settings
import PluginHandler
import asyncio
from dotenv import get_key
from Logger import log, color_templates as colors
from Logger.res import DefaultLogLevels
from discord.ext import commands

class ReelBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        intents.message_content = True
        super().__init__(command_prefix=commands.when_mentioned_or(settings.command_trigger), intents=intents)

    async def setup_hook(self) -> None:
        self.tree.copy_global_to(guild=discord.Object(id=settings.debug_server_id))
        await self.tree.sync(guild=discord.Object(id=settings.debug_server_id))

    async def on_ready(self):
        message = colors.success('LOGGED IN')+' as '+colors.highlight(f"{self.user}")+f' (ID: {self.user.id})'
        log(message, DefaultLogLevels.INFO)

bot = ReelBot()

@bot.hybrid_command()
async def ping(ctx):
    await ctx.send('pong! Log level: ' + str(settings.log_level))

# --- Main Async Entrypoint ---
async def main():
    PluginHandler.on_bot_startup()
    # Start the Discord bot (this call is blocking)
    await bot.start(get_key(".env",'BOT_TOKEN'))

if __name__ == "__main__":
    asyncio.run(main())

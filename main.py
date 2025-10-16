import settings
import PluginHandler as plugin_handler
import asyncio
from dotenv import get_key
from reelbot import ReelBot

bot = ReelBot()

@bot.hybrid_command()
async def ping(ctx):
    await ctx.send('pong! Log level: ' + str(settings.log_level))

# --- Main Async Entrypoint ---
async def main():
    plugin_handler.start(bot)
    # Start the Discord bot (this call is blocking)
    await bot.start(get_key(".env",'BOT_TOKEN'))

if __name__ == "__main__":
    asyncio.run(main())

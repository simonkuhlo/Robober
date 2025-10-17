import settings
import PluginHandler as plugin_handler
import asyncio
from dotenv import get_key
from Main.reelbot import ReelBot

bot = ReelBot()

@bot.hybrid_command()
async def ping(ctx):
    await ctx.send('pong! Log level: ' + str(settings.log_level))

async def main():
    plugin_handler.start(bot)
    await bot.start(get_key(".env",'BOT_TOKEN'))

if __name__ == "__main__":
    asyncio.run(main())

from SimonsPluginResources.Main.access_share import AccessShare
from SimonsPluginResources.Main.plugin_host import PluginHost
from SimonsPluginResources.Main.settings import SettingsManager
import core_settings
import asyncio
from dotenv import get_key
from Main.reelbot import ReelBot

settings = SettingsManager()
bot = ReelBot()
access_share = AccessShare(settings, bot)
plugin_host:PluginHost = PluginHost(access_share)

@bot.hybrid_command()
async def ping(ctx):
    await ctx.send('pong! Log level: ' + str(core_settings.log_level))

async def main():
    plugin_host.add_plugin(webinterface_plugin.get_plugin())
    plugin_host.start()
    await bot.start(get_key(".env",'BOT_TOKEN'))

if __name__ == "__main__":
    asyncio.run(main())

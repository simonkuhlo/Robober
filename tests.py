from SimonsPluginResources.Main.core import CoreApp
from dotenv import get_key
from Plugins.ChannelCloner.plugin import plugin as channel_cloner_plugin

app = CoreApp()
app.bot_token = get_key(".env",'BOT_TOKEN')
app.plugin_host.add_plugin(channel_cloner_plugin)
app.start()
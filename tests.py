from SimonsPluginResources.Main.core import CoreApp
from dotenv import get_key
from Plugins.ChannelCloner.plugin import get_plugin as get_channel_cloner_plugin

app = CoreApp()
app.bot_token = get_key(".env",'BOT_TOKEN')
app.plugin_host.add_plugin(get_channel_cloner_plugin(app.access_share))
app.start()
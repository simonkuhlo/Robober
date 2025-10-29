from SimonsPluginResources.core import CoreApp
from dotenv import get_key
from Plugins.ChannelCloner.plugin import get_plugin as get_channel_cloner_plugin
from Plugins.WebInterface.plugin import get_plugin as get_web_interface_plugin

app = CoreApp()
app.bot_token = get_key(".env",'BOT_TOKEN')
app.plugin_host.add_plugin(get_channel_cloner_plugin(app.environment))
app.plugin_host.add_plugin(get_web_interface_plugin(app.environment))
app.start()
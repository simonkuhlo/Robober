from PluginResources.access_share import AccessShare
from PluginResources.settings_connector import SettingsConnector
from reelbot import ReelBot
from .res.plugin_host import PluginHost
from Plugins.WebInterface import plugin as webinterface

plugin_host:PluginHost

def start(bot:ReelBot):
    access_share:AccessShare = AccessShare(SettingsConnector(),bot)
    global plugin_host
    plugin_host = PluginHost(access_share)
    plugin_host.add_plugin(webinterface.plugin)
    plugin_host.start()
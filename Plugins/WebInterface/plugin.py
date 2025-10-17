from SimonsPluginResources.Main import Plugin
from . import main

plugin = Plugin("WEBINTERFACE")
plugin.name = "Webinterface"
plugin.desc = "Webinterface"
plugin.version = 0
plugin.used_backend_version = 0

main.plugin_ref = plugin
plugin.starting.connect(main.on_startup)
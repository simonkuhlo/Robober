from WebInterface.plugin import WebInterfacePlugin
from Plugins.ChannelCloner.plugin import ChannelClonerPlugin
from SimonsPluginResources.launcher import Launcher
from core_settings import initial_settings

launcher = Launcher(initial_plugins=[WebInterfacePlugin, ChannelClonerPlugin], initial_settings=initial_settings)
launcher.run_blocking()

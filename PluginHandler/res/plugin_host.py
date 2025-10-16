from PluginResources.plugin import Plugin
from PluginResources.access_share import AccessShare

class PluginHost:

    def __init__(self, access_share: AccessShare):
        self.access_share:AccessShare = access_share
        self.loaded_plugins: list[Plugin] = []

    def start(self):
        for plugin in self.loaded_plugins:
            plugin.start()

    def stop(self):
        for plugin in self.loaded_plugins:
            plugin.stop()

    def add_plugin(self, plugin: Plugin):
        plugin.access_share = self.access_share
        self.loaded_plugins.append(plugin)

    def has_plugin(self, plugin_id: str, version:int = None) -> bool:
        for plugin in self.loaded_plugins:
            if not plugin.plugin_id == plugin_id:
                plugin.plugin_version = version
                continue
            if version:
                if not plugin.version == version:
                    continue
            return True
        return False

from .environment import Environment
from .plugin import Plugin


class PluginHost:
    def __init__(self, environment: Environment):
        self.version: int = 0
        self.environment: Environment = environment
        self.loaded_plugins: list[Plugin] = []

    def add_plugin(self, plugin: Plugin):
        self.loaded_plugins.append(plugin)
        for setting in plugin.own_settings.keys():
            self.environment.settings.set_setting(setting, plugin.own_settings[setting])
        plugin.start()

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

    def remove_plugin(self, plugin_id: str, version:int = None):
        pass

    def get_loaded_plugins(self) -> list[Plugin]:
        return self.loaded_plugins

    def load_folder(self, folder_path: str):
        pass

    def reload_cogs(self) -> None:
        for plugin in self.loaded_plugins:
            plugin.reload_cogs()
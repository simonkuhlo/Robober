from SimonsPluginResources.environment import Environment
from SimonsPluginResources.plugin import Plugin
from SimonsPluginResources.settings import Setting
from SimonsPluginResources.settings.models.scope import ScopePlugin
from .cog import ChannelCloner
from . import channel_authority_manager

class ChannelClonerPlugin(Plugin):
    def __init__(self, environment: Environment):
        super().__init__(plugin_id = "CHANNELCLONER",
                         environment= environment,
                         name = "Channelcloner",
                         description = "Enables normal members to create and customize their own temporary voice channels. Has integration for: Friend System, Webinterface, Event System",
                         version = 0,
                         used_host_version= 0,
                         cogs = [ChannelCloner],
                         )

    def get_settings(self) -> list[Setting]:
        return [
                Setting(rel_path="origin_channel.id", default_value="963376060672647169", scope=ScopePlugin(plugin_id=self.plugin_id)),
                Setting(rel_path="temp_category.id", default_value="1361792521226948650", scope=ScopePlugin(plugin_id=self.plugin_id)),
                ]

    def get_active_channel_ids(self) -> list[int]:
        return channel_authority_manager.get_active_channel_ids()

def get_plugin(environment: Environment) -> Plugin:
    return ChannelClonerPlugin(environment)
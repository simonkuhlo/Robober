from SimonsPluginResources.environment import Environment
from SimonsPluginResources.plugin import Plugin
from SimonsPluginResources.settings.setting import Setting
from SimonsPluginResources.settings.scopes import PluginScope
from SimonsPluginResources.settings.type_filters import filters
from .cog import ChannelCloner

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
        self.origin_channel_setting: Setting = Setting(
                                                    "origin_channel",
                                                    "id",
                                                    "Channelcloner",
                                                    type_filter=filters.INT,
                                                    scope=PluginScope(self.plugin_id),
                                                    default_value="963376060672647169"
                                                    )
        self.temp_category_setting: Setting = Setting(
                                                    "temp_channel_category",
                                                    "id",
                                                    "Channelcloner",
                                                    type_filter=filters.INT,
                                                    scope=PluginScope(self.plugin_id),
                                                    default_value="1361792521226948650"
                                                    )

    def get_settings(self) -> list[Setting]:
        return [self.origin_channel_setting, self.temp_category_setting]

def get_plugin(environment: Environment) -> Plugin:
    return ChannelClonerPlugin(environment)
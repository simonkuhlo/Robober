from SimonsPluginResources.environment import Environment
from SimonsPluginResources.plugin import Plugin
from .cog import ChannelCloner

class ChannelClonerPlugin(Plugin):
    def __init__(self, environment: Environment):
        super().__init__(_plugin_id = "CHANNELCLONER",
                         _environment= environment,
                         _name = "Channelcloner",
                         _description = "Channelcloner",
                         _version = 0,
                         _used_host_version= 0,
                         _cogs = [ChannelCloner],
                         _own_settings = {
                             "channelcloner.origin_channel.id": "963376060672647169",
                             "channelcloner.temp_channel_category.id": "1361792521226948650"
                         }
                         )

def get_plugin(environment: Environment) -> Plugin:
    return ChannelClonerPlugin(environment)
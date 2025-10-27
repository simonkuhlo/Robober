from SimonsPluginResources.Main import AccessShare
from SimonsPluginResources.Main import Plugin
from .cog import ChannelCloner

class ChannelClonerPlugin(Plugin):
    def __init__(self, access_share: AccessShare):
        super().__init__("CHANNELCLONER", access_share)
        self.name = "Channelcloner"
        self.desc = "Channelcloner"
        self.version = 0
        self.used_backend_version = 0
        self.cogs = [ChannelCloner]
        self.own_settings = {"channelcloner.origin_channel.id" : "963376060672647169",
                             "channelcloner.temp_channel_category.id": "1361792521226948650"
                             }

def get_plugin(access_share: AccessShare):
    return ChannelClonerPlugin(access_share)
from SimonsPluginResources.Main import AccessShare
from SimonsPluginResources.Main import Plugin

class ChannelClonerPlugin(Plugin):
    def __init__(self, access_share: AccessShare):
        super().__init__("WEBINTERFACE", access_share)
        self.name = "Webinterface"
        self.desc = "Webinterface"
        self.version = 0
        self.used_backend_version = 0
        self.own_settings = {
                            "webinterface.host_address" : "localhost",
                             }

    def _start(self) -> None:
        pass

def get_plugin(access_share: AccessShare):
    return ChannelClonerPlugin(access_share)
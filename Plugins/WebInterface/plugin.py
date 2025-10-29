from SimonsPluginResources.environment import Environment
from SimonsPluginResources.plugin import Plugin
from . import main

class WebInterfacePlugin(Plugin):
    def __init__(self, environment: Environment):
        super().__init__(_plugin_id = "WEBINTERFACE",
                         _environment = environment,
                         _name = "Webinterface",
                         _description = "Webinterface",
                         _version = 0,
                         _used_host_version = 0,
                         _own_settings = {"webinterface.host_address" : "localhost"}
                         )
    def _start(self) -> None:
        main.on_startup(self.environment)

def get_plugin(environment: Environment):
    return WebInterfacePlugin(environment)
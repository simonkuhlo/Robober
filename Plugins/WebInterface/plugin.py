from SimonsPluginResources.environment import Environment
from SimonsPluginResources.plugin import Plugin
from SimonsPluginResources.plugin_request import PluginRequest
from SimonsPluginResources.settings.scopes import PluginScope
from SimonsPluginResources.settings.setting import Setting
from . import main

class WebInterfacePlugin(Plugin):
    def __init__(self, environment: Environment):
        super().__init__(plugin_id = "WEBINTERFACE",
                         environment = environment,
                         name = "Webinterface",
                         description = "Webinterface",
                         version = 0,
                         used_host_version = 0,
                         plugin_connections=[PluginRequest("HOST", 0, True)]
                         )

    def _start(self) -> None:
        main.on_startup(self.environment)

    def get_settings(self) -> list[Setting]:
        return [
            Setting("webinterface",
                    "host_address",
                    "Networking",
                    scope=PluginScope(self.plugin_id),
                    default_value="localhost",
                    )
        ]

def get_plugin(environment: Environment):
    return WebInterfacePlugin(environment)
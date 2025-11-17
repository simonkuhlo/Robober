from typing import Optional, TYPE_CHECKING, Type
from discord.ext import commands
from SimonsPluginResources.asyncio_task_wrapper import AsyncTask
from SimonsPluginResources.plugin import Plugin, PluginMeta
from SimonsPluginResources.settings import Setting
from SimonsPluginResources.settings.models.scope import ScopePlugin
from .cog import ChannelCloner
if TYPE_CHECKING:
    from SimonsPluginResources.plugin_host import PluginHost

class ChannelClonerPluginMeta(PluginMeta):
    def __init__(self):
        super().__init__(plugin_id = "channelcloner")
        self.name = "Channel cloner"
        self.description = "No description provided"
        self.version = 2
        self.used_backend_version = 10
        self.connection_requests = None
        self.settings = [
            Setting(rel_path="origin_channel.id", default_value="963376060672647169", scope=ScopePlugin(plugin_id=self.plugin_id)),
            Setting(rel_path="temp_category.id", default_value="1361792521226948650", scope=ScopePlugin(plugin_id=self.plugin_id)),
        ]

class ChannelClonerPlugin(Plugin):
    def __init__(self, host: "PluginHost"):
        super().__init__(host, ChannelClonerPluginMeta())

    @property
    def tasks(self) -> Optional[list[AsyncTask]]:
        return

    @property
    def cogs(self) -> Optional[list[Type[commands.Cog]]]:
        return [ChannelCloner]
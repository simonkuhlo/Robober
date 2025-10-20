import asyncio
from discord.ext import commands
from SimonsPluginResources.Main.plugin import Plugin
from SimonsPluginResources.Main.access_share import AccessShare
from Logger import logger, DefaultLogLevels


class PluginHost:

    def __init__(self, access_share: AccessShare):
        self.started: bool = False
        self.access_share:AccessShare = access_share
        self.system_cogs: list[commands.Cog] = [PluginHostCog(access_share.bot, self)]
        self.loaded_plugins: list[Plugin] = []

    def start(self):
        logger.log("Starting plugin host", DefaultLogLevels.INFO)
        self.started = True
        for plugin in self.loaded_plugins:
            plugin.start()

    def stop(self):
        logger.log("Stopping plugin host", DefaultLogLevels.INFO)
        self.started = False
        for plugin in self.loaded_plugins:
            plugin.stop()

    def add_plugin(self, plugin: Plugin):
        plugin.access_share = self.access_share
        self.loaded_plugins.append(plugin)
        for setting in plugin.own_settings.keys():
            self.access_share.settings.set_setting(setting, plugin.own_settings[setting])
        if self.started:
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
        logger.log("Reloading Cogs", DefaultLogLevels.INFO)
        bot = self.access_share.bot
        #for cog_name in self.access_share.bot.cogs.keys():
            #future = asyncio.run_coroutine_threadsafe(bot.remove_cog(cog_name), bot.loop)
            #future.result(timeout=3)
        for plugin in self.loaded_plugins:
            logger.log(f"Reloading Cogs for Plugin: {plugin.name}", DefaultLogLevels.INFO)
            for Cog in plugin.cogs:
                try:
                    logger.log(f"Reloading Cogs for Plugin: {plugin.name} Cog: {Cog.__cog_name__}", DefaultLogLevels.INFO)

                    cog_instance = Cog(bot, self.access_share)
                    future = asyncio.run_coroutine_threadsafe(bot.add_cog(cog_instance), bot.loop)
                    future.result(timeout=3)
                except Exception as e:
                    logger.log(f"Error while reloading Cog: {e}", DefaultLogLevels.INFO)
                except TimeoutError as e:
                    logger.log(f"Error while reloading Cog: {e}", DefaultLogLevels.INFO)
            logger.log(f"Reloaded Cogs for Plugin: {plugin.name}", DefaultLogLevels.INFO)

class PluginHostCog(commands.Cog):
    def __init__(self, bot, plugin_host:PluginHost):
        self.plugin_host = plugin_host
        self.bot = bot
        super().__init__()

    @commands.Cog.listener()
    async def on_ready(self):
        self.plugin_host.reload_cogs()
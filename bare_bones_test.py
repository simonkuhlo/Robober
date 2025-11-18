import asyncio
from dotenv import get_key
from SimonsPluginResources.asyncio_task_wrapper import AsyncTask
from SimonsPluginResources.reelbot import ReelBot
from SimonsPluginResources.settings import SettingsManager, SimpleSettingsManager
from WebInterface.plugin import WebInterfacePlugin
from Plugins.ChannelCloner.plugin import ChannelClonerPlugin
from SimonsPluginResources.plugin_host import PluginHost
from SimonsPluginResources.task_manager import AsyncTaskManager
from SimonsPluginResources.environment import Environment
from SimonsPluginResources.custom_logging.logger import Logger


async def main():
    logger: Logger = Logger()
    task_manager: AsyncTaskManager = AsyncTaskManager(logger)
    settings: SettingsManager = SimpleSettingsManager()
    bot: ReelBot = ReelBot(logger, settings)
    env: Environment = Environment(settings, logger, task_manager, bot)
    plugin_host: PluginHost = PluginHost(env)
    task_manager.add_task(AsyncTask(bot.start, args=(get_key(".env", "BOT_TOKEN"),), name="Bot main loop"))
    await plugin_host.add_plugin(WebInterfacePlugin)
    await plugin_host.add_plugin(ChannelClonerPlugin)
    await task_manager.start()

asyncio.run(main())

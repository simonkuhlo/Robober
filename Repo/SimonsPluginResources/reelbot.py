import discord
import core_settings
from SimonsPluginResources.Logger import Logger, DefaultLogLevels, color_templates as colors
from discord.ext import commands
from .plugin_signal import Signal


class ReelBot(commands.Bot):
    def __init__(self, logger: Logger):
        intents = discord.Intents.all()
        intents.message_content = True
        self.logger = logger
        self.signal_setup:Signal = Signal()
        self.signal_ready:Signal = Signal()
        super().__init__(command_prefix=commands.when_mentioned_or(core_settings.command_trigger), intents=intents)

    async def setup_hook(self) -> None:
        self.signal_setup.emit()
        self.tree.copy_global_to(guild=discord.Object(id=core_settings.debug_server_id))
        await self.tree.sync(guild=discord.Object(id=core_settings.debug_server_id))

    async def on_ready(self):
        self.signal_ready.emit()
        message = colors.success('LOGGED IN')+' as '+colors.highlight(f"{self.user}")+f' (ID: {self.user.id})'
        self.logger.log(message, DefaultLogLevels.INFO)
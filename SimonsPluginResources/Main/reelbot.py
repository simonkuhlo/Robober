import discord
import settings
from logger import logger, color_templates as colors
from logger.res import DefaultLogLevels
from discord.ext import commands

class ReelBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        intents.message_content = True
        super().__init__(command_prefix=commands.when_mentioned_or(settings.command_trigger), intents=intents)

    async def setup_hook(self) -> None:
        self.tree.copy_global_to(guild=discord.Object(id=settings.debug_server_id))
        await self.tree.sync(guild=discord.Object(id=settings.debug_server_id))

    async def on_ready(self):
        message = colors.success('LOGGED IN')+' as '+colors.highlight(f"{self.user}")+f' (ID: {self.user.id})'
        logger.log(message, DefaultLogLevels.INFO)
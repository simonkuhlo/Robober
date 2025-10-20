from typing import Optional, Sequence

import discord
from discord.abc import Snowflake
from discord.ext.commands import Cog
from discord.utils import MISSING

import core_settings
from Logger import logger, color_templates as colors
from Logger.res import DefaultLogLevels
from discord.ext import commands
from .plugin_signal import Signal


class ReelBot(commands.Bot):
    def __init__(self, system_cogs:list[commands.Cog] = []):
        intents = discord.Intents.all()
        intents.message_content = True
        self.signal_setup:Signal = Signal()
        self.signal_ready:Signal = Signal()
        self.system_cogs:list[commands.Cog] = system_cogs
        super().__init__(command_prefix=commands.when_mentioned_or(core_settings.command_trigger), intents=intents)

    async def setup_hook(self) -> None:
        for cog in self.system_cogs:
            await self.add_cog(cog)
        self.signal_setup.emit()
        self.tree.copy_global_to(guild=discord.Object(id=core_settings.debug_server_id))
        await self.tree.sync(guild=discord.Object(id=core_settings.debug_server_id))

    async def on_ready(self):
        self.signal_ready.emit()
        message = colors.success('LOGGED IN')+' as '+colors.highlight(f"{self.user}")+f' (ID: {self.user.id})'
        logger.log(message, DefaultLogLevels.INFO)
import asyncio
import enum
from typing import final

from discord.ext import commands
from discord.ext.commands import Cog

from Logger import logger, DefaultLogLevels
from .access_share import AccessShare
from .plugin_cog import PluginCog
from .plugin_signal import Signal


class Status(enum.Enum):
    NOT_STARTED = 0
    STARTED = 1
    STOPPED = 2
    ERROR = 3

class Plugin:
    def __init__(self, _plugin_id:str, _access_share:AccessShare):
        #---META---
        self.plugin_id: str = _plugin_id
        self.name: str = ""
        self.desc: str = ""
        self.version: int = 0
        self.needs_backend_version: int = 0
        #---META---
        self.cogs: list[PluginCog] = []
        self.own_settings: dict[str, str] = {}
        self.access_share: AccessShare = _access_share
        self.status: Status = Status.NOT_STARTED
        self.started:Signal = Signal()
        self.stopped:Signal = Signal()

    @final
    def start(self):
        self._on_start()
        if self.check_bot_ready():
            self.reload_cogs()
        self.status = Status.STARTED
        self.started.emit()

    def _on_start(self):
        pass

    @final
    def stop(self):
        self._on_stop()
        self.status = Status.STOPPED
        self.stopped.emit()

    def _on_stop(self):
        self.unload_cogs()

    def check_bot_ready(self) -> bool:
        if not self.access_share.bot:
            return False
        if not self.access_share.bot.is_ready():
            return False
        return True

    def reload_cogs(self) -> None:
        logger.log(f"Reloading Cogs for Plugin: {self.name}", DefaultLogLevels.INFO)
        self.unload_cogs()
        self.load_cogs()

    def unload_cogs(self) -> None:
        bot = self.access_share.bot
        try:
            for cog_name in bot.cogs.keys():
                future = asyncio.run_coroutine_threadsafe(bot.remove_cog(cog_name), bot.loop)
                future.result(timeout=3)
        except TimeoutError:
            logger.log(f"Error while reloading Cog: Asyncio Timeout", DefaultLogLevels.INFO)
        except Exception as e:
            logger.log(f"Error while reloading Cog: {e}", DefaultLogLevels.INFO)


    def load_cogs(self) -> None:
        try:
            if not self.access_share.bot:
                raise Exception("No bot instance given.")
            if not self.access_share.bot.is_ready():
                raise Exception("Bot is not ready.")
        except Exception as e:
            logger.log(f"Loading Cogs could not be started: {self.name}: {e}", DefaultLogLevels.INFO)
            return
        bot = self.access_share.bot
        for CogObject in self.cogs:
            try:
                cog_instance = CogObject(bot, self.access_share)
                future = asyncio.run_coroutine_threadsafe(bot.add_cog(cog_instance), bot.loop)
                future.result(timeout=3)
            except TimeoutError:
                logger.log(f"Error while reloading Cog: Asyncio Timeout", DefaultLogLevels.INFO)
            except Exception as e:
                logger.log(f"Error while reloading Cog: {e}", DefaultLogLevels.INFO)
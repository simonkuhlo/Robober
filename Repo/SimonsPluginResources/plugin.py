import asyncio
import enum
from typing import final, Type
from .Logger import DefaultLogLevels, Logger
from .environment import Environment
from .plugin_cog import PluginCog
from .plugin_signal import Signal


class Status(enum.Enum):
    NOT_STARTED = 0
    STARTED = 1
    STOPPED = 2
    ERROR = 3

class Plugin:
    def __init__(self,
                _plugin_id:str,
                _environment:Environment,
                _name:str = "Not set",
                _description:str = "Not set",
                _version:int = 0,
                _used_host_version:int = 0,
                _cogs: list[Type[PluginCog]] = [],
                _own_settings: dict[str, str] = {},
            ):
        self.plugin_id: str = _plugin_id
        self.name: str = _name
        self.description: str = _description
        self.version: int = _version
        self.needs_backend_version: int = _used_host_version
        self.cogs: list[Type[PluginCog]] = _cogs
        self.own_settings: dict[str, str] = _own_settings

        self.environment: Environment = _environment

        self.status: Status = Status.NOT_STARTED
        self.started:Signal = Signal()
        self.stopped:Signal = Signal()

    @final
    def start(self):
        self._start()
        if self.check_bot_ready():
            self.reload_cogs()
        self.status = Status.STARTED
        self.started.emit()

    def _start(self):
        pass

    @final
    def stop(self):
        self._stop()
        self.status = Status.STOPPED
        self.stopped.emit()

    def _stop(self):
        self.unload_cogs()

    def check_bot_ready(self) -> bool:
        if not self.environment.bot:
            return False
        if not self.environment.bot.is_ready():
            return False
        return True

    def reload_cogs(self) -> None:
        self.environment.logger.log(f"Reloading Cogs for Plugin: {self.name}", DefaultLogLevels.INFO)
        self.unload_cogs()
        self.load_cogs()

    def unload_cogs(self) -> None:
        bot = self.environment.bot
        try:
            for cog_name in bot.cogs.keys():
                future = asyncio.run_coroutine_threadsafe(bot.remove_cog(cog_name), bot.loop)
                future.result(timeout=3)
        except TimeoutError:
            self.environment.logger.log(f"Error while reloading Cog: Asyncio Timeout", DefaultLogLevels.INFO)
        except Exception as e:
            self.environment.logger.log(f"Error while reloading Cog: {e}", DefaultLogLevels.INFO)


    def load_cogs(self) -> None:
        try:
            if not self.environment.bot:
                raise Exception("No bot instance given.")
            if not self.environment.bot.is_ready():
                raise Exception("Bot is not ready.")
        except Exception as e:
            self.environment.logger.log(f"Loading Cogs could not be started: {self.name}: {e}", DefaultLogLevels.INFO)
            return
        bot = self.environment.bot
        for CogObject in self.cogs:
            try:
                cog_instance = CogObject(self.environment)
                future = asyncio.run_coroutine_threadsafe(bot.add_cog(cog_instance), bot.loop)
                future.result(timeout=3)
            except TimeoutError:
                self.environment.logger.log(f"Error while reloading Cog: Asyncio Timeout", DefaultLogLevels.INFO)
            except Exception as e:
                self.environment.logger.log(f"Error while reloading Cog: {e}", DefaultLogLevels.INFO)
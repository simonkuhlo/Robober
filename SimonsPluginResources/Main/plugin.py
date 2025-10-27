import enum
from typing import final
from discord.ext.commands import Cog
from .access_share import AccessShare
from .plugin_cog import PluginCog
from .plugin_signal import Signal


class Status(enum.Enum):
    NOT_STARTED = 0
    STARTED = 1
    STOPPED = 2
    ERROR = 3

class Plugin:
    def __init__(self, _plugin_id:str):
        self.plugin_id: str = _plugin_id
        self.name: str = ""
        self.desc: str = ""
        self.version: int = 0
        self.needs_backend_version: int = 0
        self.cogs: list[PluginCog] = []
        self.own_settings: dict[str, str] = {}
        self.access_share: AccessShare
        self.status: Status = Status.NOT_STARTED
        self.started:Signal = Signal()
        self.stopped:Signal = Signal()

    @final
    def start(self):
        self._on_start()
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
        pass


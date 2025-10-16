import enum
from .access_share import AccessShare
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
        self.desc: str
        self.version: int = 0
        self.needs_backend_version: int = 0

        self.status: Status

        self.access_share: AccessShare

        self.starting:Signal = Signal()
        self.stopping:Signal = Signal()

    def start(self):
        self.starting.emit()

    def stop(self):
        self.stopping.emit()


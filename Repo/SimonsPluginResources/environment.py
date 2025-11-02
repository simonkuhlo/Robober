from .reelbot import ReelBot
from .settings.settings_manager import SettingsManager
from .Logger import Logger
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .plugin_host import PluginHost


class Environment:
    def __init__(self, bot: ReelBot, settings: SettingsManager, logger: Logger):
        self.bot = bot
        self.settings = settings
        self.logger = logger
        self.host: "PluginHost"
from .reelbot import ReelBot
from .settings import SettingsManager
from Logger import Logger, logger

class AccessShare:
    def __init__(self, settings: SettingsManager, bot: ReelBot):
        self.logger: Logger = logger
        self.settings: SettingsManager = settings
        self.bot: ReelBot = bot
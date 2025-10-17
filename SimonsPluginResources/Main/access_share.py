from .reelbot import ReelBot
from .settings_connector import SettingsConnector
from logger import Logger, logger

class AccessShare:
    def __init__(self, settings: SettingsConnector, bot: ReelBot):
        self.logger: Logger = logger
        self.settings: SettingsConnector = settings
        self.bot: ReelBot = bot
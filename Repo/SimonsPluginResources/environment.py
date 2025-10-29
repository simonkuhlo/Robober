from .reelbot import ReelBot
from .settings import SettingsManager
from .Logger import Logger


class Environment:
    def __init__(self, bot: ReelBot, settings: SettingsManager, logger: Logger):
        self.bot = bot
        self.settings = settings
        self.logger = logger
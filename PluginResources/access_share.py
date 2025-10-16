from discord.ext import commands
from .settings_connector import SettingsConnector
from logger import Logger, logger

class AccessShare:
    def __init__(self, settings: SettingsConnector, bot: commands.Bot):
        self.logger: Logger = logger
        self.settings: SettingsConnector = settings
        self.bot: commands.Bot = bot
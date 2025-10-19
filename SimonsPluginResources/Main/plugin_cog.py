from discord.ext import commands
from .access_share import AccessShare

class PluginCog(commands.Cog):
    def __init__(self, bot, access_share:AccessShare):
        self.bot = bot
        self.access_share = access_share
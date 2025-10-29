from discord.ext import commands
from .environment import Environment


class PluginCog(commands.Cog):
    def __init__(self, environment: Environment):
        self.environment = environment
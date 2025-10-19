from discord.ext import commands
from SimonsPluginResources.Main.settings import SettingsManager
from SimonsPluginResources.Main.access_share import AccessShare
from SimonsPluginResources.Main.plugin_cog import PluginCog

class ChannelCloner(PluginCog):
    def __init__(self, bot, access_share:AccessShare):
        super().__init__(bot, access_share)

    @commands.hybrid_command()
    async def hello(self, ctx):
        await ctx.send("Hello from the cog!")

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        origin_channel_id:int = int(self.access_share.settings.get_setting("channelcloner.origin_channel.id"))
        if before.channel != None:
            if before.channel != after.channel:
                if before.channel.category.name == v.TRIOSCATEGORY_NAME:
                    print(member.name, "aka", member.nick, "left Trios. Current users:", len(before.channel.members))
                    if len(before.channel.members) == 0:
                        await before.channel.delete()
                        print("Channel deleted.")
        if after.channel != None:
            if after.channel != before.channel:
                if after.channel.id == origin_channel_id:
                    print(member.name, "aka", member.nick, "connected to Trios. Current users:",
                    len(after.channel.members))
                    await after.channel.clone()
                    print("Channel cloned.")

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
        temp_channel_category_id:int = int(self.access_share.settings.get_setting("channelcloner.temp_channel_category.id"))
        if before.channel is not None:
            if before.channel != after.channel:
                if before.channel.category.id == temp_channel_category_id:
                    if before.channel.id != origin_channel_id:
                        print(member.name, "aka", member.nick, "left temp channel. Current users:", len(before.channel.members))
                        if len(before.channel.members) == 0:
                            await before.channel.delete()
                            print("Channel deleted.")
        if after.channel is not None:
            if after.channel != before.channel:
                if after.channel.id == origin_channel_id:
                    print(member.name, "aka", member.nick, "connected to origin channel. Current users:", len(after.channel.members))
                    category_channel = self.access_share.bot.get_channel(temp_channel_category_id)
                    new_channel = await category_channel.create_voice_channel(member.name)
                    await member.move_to(new_channel)
                    print("Channel cloned.")

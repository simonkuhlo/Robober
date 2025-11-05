from discord import VoiceChannel
from discord.ext import commands
from SimonsPluginResources.environment import Environment
from SimonsPluginResources.plugin_cog import PluginCog
from .Res.channel_authority import ChannelAuthority
from .Res.Views.access_editor import ChannelEditorView
from . import channel_authority_manager as cam

class ChannelCloner(PluginCog):
    def __init__(self, environment: Environment):
        super().__init__(environment)

    @commands.hybrid_command()
    async def hello(self, ctx):
        await ctx.send("Hello from the cog!")

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        try:
            origin_channel_id:int = self.environment.settings.get_value_from_path("PLUGIN:CHANNELCLONER:origin_channel.id")
            if not origin_channel_id:
                raise Exception("origin_channel_id is not set")
            temp_channel_category_id:int = self.environment.settings.get_value_from_path("PLUGIN:CHANNELCLONER:temp_channel_category.id")
            if not temp_channel_category_id:
                raise Exception("temp_channel_category_id is not set")
            if before.channel is not None:
                if before.channel != after.channel:
                    if before.channel.category.id == temp_channel_category_id:
                        if before.channel.id != origin_channel_id:
                            print(member.name, "aka", member.nick, "left temp channel. Current users:", len(before.channel.members))
                            if len(before.channel.members) == 0:
                                try:
                                    cam.delete_channel(before.channel)
                                except:
                                    pass
                                await before.channel.delete()
                                print("Channel deleted.")
                            else:
                                if cam.is_user_owner(before.channel.id, member.id):
                                    cam.set_owner(before.channel.id, None)
                                    await before.channel.send("The owner of this channel left. Click to claim ownership")
            if after.channel is not None:
                if after.channel != before.channel:
                    if after.channel.id == origin_channel_id:
                        print(member.name, "aka", member.nick, "connected to origin channel. Current users:", len(after.channel.members))
                        category_channel = self.environment.bot.get_channel(temp_channel_category_id)
                        new_channel:VoiceChannel = await category_channel.create_voice_channel(member.name)
                        overwrite = new_channel.overwrites_for(new_channel.guild.default_role)
                        overwrite.connect = True
                        await new_channel.set_permissions(new_channel.guild.default_role, overwrite=overwrite)
                        await member.move_to(new_channel)
                        authority = ChannelAuthority(member.id)
                        cam.add_channel(new_channel.id, authority)
                        await new_channel.send("", view=ChannelEditorView(new_channel))
                        print("Channel cloned.")
        except Exception as e:
            self.environment.logger.log(f"Failed to create / delete temporary channel: {e}")
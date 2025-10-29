import discord
from discord import VoiceChannel
from .channel_access_view import ChannelAccessView
from .user_limit_modal import UserLimitModal
from ... import channel_authority_manager as cam


class ChannelEditorView(discord.ui.View):
    def __init__(self, target_channel:VoiceChannel):
        super().__init__(timeout=None)
        self.target_channel = target_channel
        self.add_item(AccessSettingsSelect(self.target_channel, self))

class AccessSettingsSelect(discord.ui.Select):
    def __init__(self, target_channel:VoiceChannel, parent_view:discord.ui.View):
        self.target_channel: VoiceChannel = target_channel
        self.parent_view: discord.ui.View = parent_view
        self.current_lock_label_text: str = ""
        options = [
            discord.SelectOption(label=self.get_channel_lock_label_text() , emoji=self.get_channel_lock_label_emoji(), description="Lock / Unlock Channel"),
            discord.SelectOption(label="Set User Limit", emoji="👥", description="Set a limit for how many users can join this channel"),
            discord.SelectOption(label="Accept / Reject User", emoji="✅", description="Grant or reject access to the channel for specific users"),
            discord.SelectOption(label="Friends override Lock", emoji="❤️", description="Friends can join this channel even if it is locked")
        ]
        super().__init__(placeholder="Access Settings", options=options)

    async def callback(self, interaction: discord.Interaction):
        value = self.values[0]
        target_channel = self.target_channel
        if not cam.get_channel_authority(target_channel.id):
            await interaction.response.send_message(
                "This channel currently has no owner. Do you want to claim ownership?", ephemeral=True
            )
            await interaction.message.edit(view=self.parent_view)
            return

        if not cam.is_user_elevated(target_channel.id, interaction.user.id):
            await interaction.response.send_message(
                "Error! You do not have elevated privileges in this channel. Please contact the current owner: owner_name",
                ephemeral=True,
            )
            await interaction.message.edit(view=self.parent_view)
            return

        match value:
            case self.current_lock_label_text:
                await self.switch_channel_lock_state()
                if self.is_channel_locked():
                    await interaction.response.send_message(f"Channel Locked.", ephemeral=True)
                else:
                    await interaction.response.send_message(f"Channel Unlocked.", ephemeral=True)
            case "Set User Limit":
                await interaction.response.send_modal(UserLimitModal(target_channel))
            case "Accept / Reject User":
                await interaction.response.send_message("Puts user on temporary Whitelist", view=ChannelAccessView(interaction.channel), ephemeral=True)
            case "Friends override Lock":
                await interaction.response.send_message("Friend System module not enabled in Bot base.", ephemeral=True)
            case _:
                await interaction.response.send_message("Unknown command", ephemeral=True)

        await interaction.message.edit(view=ChannelEditorView(self.target_channel))

    def get_channel_lock_label_text(self) -> str:
        if self.is_channel_locked():
            self.current_lock_label_text = "Unlock Channel"
        else:
            self.current_lock_label_text = "Lock Channel"
        return self.current_lock_label_text

    def get_channel_lock_label_emoji(self) -> str:
        if self.is_channel_locked():
            return "🔓"
        else:
            return "🔒"

    async def switch_channel_lock_state(self) -> None:
        overwrite = self.target_channel.overwrites_for(self.target_channel.guild.default_role)
        overwrite.connect = not overwrite.connect
        await self.target_channel.set_permissions(self.target_channel.guild.default_role, overwrite=overwrite)

    def is_channel_locked(self) -> bool:
        overwrite = self.target_channel.overwrites_for(self.target_channel.guild.default_role)
        return not overwrite.connect

class CustomizeSettingSelect(discord.ui.Select):
    def __init__(self, target_channel:VoiceChannel, parent_view:discord.ui.View):
        self.target_channel: VoiceChannel = target_channel
        self.parent_view: discord.ui.View = parent_view
        self.current_lock_label_text: str = ""
        options = [
            discord.SelectOption(label="Set channel name", emoji="👥", description="Set a limit for how many users can join this channel"),
            discord.SelectOption(label="Set channel status", emoji="✅", description="Grant or reject access to the channel for specific users"),
        ]
        super().__init__(placeholder="Access Settings", options=options)

    async def callback(self, interaction: discord.Interaction):
        value = self.values[0]
        target_channel = self.target_channel
        if not cam.get_channel_authority(target_channel.id):
            await interaction.response.send_message(
                "This channel currently has no owner. Do you want to claim ownership?", ephemeral=True
            )
            await interaction.message.edit(view=self.parent_view)
            return

        if not cam.is_user_elevated(target_channel.id, interaction.user.id):
            await interaction.response.send_message(
                "Error! You do not have elevated privileges in this channel. Please contact the current owner: owner_name",
                ephemeral=True,
            )
            await interaction.message.edit(view=self.parent_view)
            return

        match value:
            case self.current_lock_label_text:
                await self.switch_channel_lock_state()
                if self.is_channel_locked():
                    await interaction.response.send_message(f"Channel Locked.", ephemeral=True)
                else:
                    await interaction.response.send_message(f"Channel Unlocked.", ephemeral=True)
            case "Set User Limit":
                await interaction.response.send_modal(UserLimitModal(target_channel))
            case "Accept / Reject User":
                await interaction.response.send_message("Puts user on temporary Whitelist", view=ChannelAccessView(interaction.channel), ephemeral=True)

        await interaction.message.edit(view=ChannelEditorView(self.target_channel))
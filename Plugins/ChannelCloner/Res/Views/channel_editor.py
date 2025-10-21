import discord
from discord import VoiceChannel
from discord.ext import commands

from .lock_status_modal import LockStatusView
from .user_limit_modal import UserLimitModal
from ... import channel_authority_manager as cam
from ..channel_authority import ChannelAuthority


class ChannelEditorView(discord.ui.View):
    def __init__(self, target_channel:VoiceChannel):
        super().__init__(timeout=None)
        self.target_channel = target_channel

    @discord.ui.select(
        placeholder="Access Settings",
        options=[
            discord.SelectOption(label="Lock / Unlock Channel", emoji="🔐", description="Lock / Unlock Channel"),
            discord.SelectOption(label="Set User Limit", emoji="👥", description="Set a limit for how many users can join this channel"),
            # NOTE only show when channel is locked / not open
            discord.SelectOption(label="Accept User (Temporary)", emoji="✅", description="Channel needs to be locked first"),
            discord.SelectOption(label="Reject User (Temporary)", emoji="❌", description="Members on this list cannot access your channel")
        ]
    )
    async def select_callback(self, interaction: discord.Interaction, select):
        value = select.values[0]
        channel_authority:ChannelAuthority = cam.get_channel_authority(value)
        if not cam.get_channel_authority(self.target_channel.id):
            await interaction.response.send_message("This channel currently has no owner. Do you want to claim ownership?", ephemeral=True)
            await interaction.message.edit(view=self)
            return
        else:
            if not cam.is_user_elevated(self.target_channel.id, interaction.user.id):
                await interaction.response.send_message(
                    "Error! You do not have elevated privileges in this channel. Please contact the current owner: owner_name", ephemeral=True)
                await interaction.message.edit(view=self)
                return
        match value:
            case "Edit Channel Access":
                await interaction.response.send_message("", view=LockStatusView(self.target_channel), ephemeral=True)
            case "Set User Limit":
                await interaction.response.send_modal(UserLimitModal(self.target_channel))
            case "Accept User (Temporary)":
                await interaction.response.send_message("Puts user on temporary Whitelist", ephemeral=True)
            case "Reject User (Temporary)":
                await interaction.response.send_message("Puts user on temporary Blacklist", ephemeral=True)
            case _:
                await interaction.response.send_message("Unknown command", ephemeral=True)

        await interaction.message.edit(view=self)

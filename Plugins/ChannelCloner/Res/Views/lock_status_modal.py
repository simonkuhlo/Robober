import discord
from discord import VoiceChannel
from discord.ui import Modal, TextInput, View, Button, Select


class LockStatusView(View):
    def __init__(self, voice_channel: VoiceChannel):
        super().__init__()
        self.voice_channel = voice_channel

    @discord.ui.select(
        placeholder="Select Lock Status",
        options=[
            discord.SelectOption(label="Open", emoji="🔓",
                                 description="Everyone can join"),
            discord.SelectOption(label="Friends only", emoji="🔐",
                                 description="Only friends and users on the temporary whitelist can join"),
            discord.SelectOption(label="Locked", emoji="🔒",
                                 description="Only users on the temporary whitelist can join"),
        ]
    )
    async def select_callback(self, interaction: discord.Interaction, select):
        value = select.values[0]
        match value:
            case "Open":
                await interaction.response.send_message("Channel unlocked.", ephemeral=True)
            case "Friends only":
                await interaction.response.send_message("Bot: Friend plugin not enabled.", ephemeral=True)
            case "Locked":
                await interaction.response.send_message("Channel locked.", ephemeral=True)
            case _:
                await interaction.response.send_message("Unknown command", ephemeral=True)

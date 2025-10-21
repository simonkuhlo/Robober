import discord
from discord import VoiceChannel
from discord.ui import Modal, TextInput, View, Button

class UserLimitModal(Modal):
    def __init__(self, voice_channel: VoiceChannel):
        super().__init__(title="Enter Amount")
        self.amount_input = TextInput(
            label="Amount",
            placeholder="Enter a number",
            required=True
        )
        self.voice_channel = voice_channel
        self.add_item(self.amount_input)

    async def on_submit(self, interaction: discord.Interaction):
        try:
            amount = int(self.amount_input.value)
            await self.voice_channel.edit(user_limit=amount)
            await interaction.response.send_message(f"User limit set: {amount}", ephemeral=True)
        except ValueError:
            await interaction.response.send_message("Please enter a valid number.", ephemeral=True)
            return
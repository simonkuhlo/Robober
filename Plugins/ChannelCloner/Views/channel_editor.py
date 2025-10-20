import discord
from discord.ext import commands

class ChannelEditorView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.select(
        placeholder="Choose an action...",
        options=[
            discord.SelectOption(label="Info", emoji="ℹ️", description="Get info"),
            discord.SelectOption(label="Ping", emoji="🏓", description="Check bot latency"),
            discord.SelectOption(label="Exit", emoji="❌", description="Close this menu")
        ]
    )
    async def select_callback(self, interaction: discord.Interaction, select):
        value = select.values[0]

        if value == "Info":
            await interaction.response.send_message("Here’s some info!", ephemeral=True)
        elif value == "Ping":
            await interaction.response.send_message(f"Pong! Latency xxxx ms", ephemeral=True)
        elif value == "Exit":
            await interaction.response.send_message("Closing menu...", ephemeral=True)

        # Disable all components in this view
        #self.disable_all_items()
        await interaction.message.edit(view=self)

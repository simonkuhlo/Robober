import discord
from discord.ext import commands

class ChannelEditorView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.select(
        placeholder="Access Settings",
        options=[
            discord.SelectOption(label="Edit Channel Access", emoji="🔐", description="Set who has access to this channel"),
            discord.SelectOption(label="Set User Limit", emoji="👥", description="Set a limit for how many users can join this channel"),
            # NOTE only show when channel is locked / not open
            discord.SelectOption(label="Accept User (Temporary)", emoji="✅", description="Channel needs to be locked first"),
            discord.SelectOption(label="Reject User (Temporary)", emoji="❌", description="Members on this list cannot access your channel")
        ]
    )
    async def select_callback(self, interaction: discord.Interaction, select):
        value = select.values[0]

        match value:
            case "Channel Access":
                await interaction.response.send_message("Channel Access: Public, Friends only, Noone", ephemeral=True)
            case "User Limit":
                await interaction.response.send_message("User Limit: 1-25", ephemeral=True)
            case "Accept User (Temporary)":
                await interaction.response.send_message("Puts user on temporary Whitelist", ephemeral=True)
            case "Reject User (Temporary)":
                await interaction.response.send_message("Puts user on temporary Blacklist", ephemeral=True)
            case _:
                await interaction.response.send_message("Unknown command", ephemeral=True)

        # Disable all components in this view
        #self.disable_all_items()
        await interaction.message.edit(view=self)

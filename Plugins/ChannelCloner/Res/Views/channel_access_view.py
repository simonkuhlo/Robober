from enum import Enum
import discord
from discord import VoiceChannel

class AcceptMode(Enum):
    ACCEPT = 1
    REJECT = 2
    RESET = 3

class ChannelAccessView(discord.ui.View):
    def __init__(self, target_channel:VoiceChannel):
        super().__init__(timeout=None)
        self.target_channel = target_channel
        self.accept_mode:AcceptMode = AcceptMode.ACCEPT
        self.add_item(AcceptRejectSelect(self))
        self.add_item(UserSelect(self))

class AcceptRejectSelect(discord.ui.Select):
    def __init__(self, parent_view:ChannelAccessView):
        self.parent_view = parent_view
        options = [
            discord.SelectOption(label="Accept User", emoji="✅",
                                 description=""),
            discord.SelectOption(label="Reject User", emoji="❌",
                                 description=""),
            discord.SelectOption(label="Reject User (Temporary)", emoji="❌",
                                 description="Members on this list cannot access your channel"),
        ]
        super().__init__(placeholder="Access Settings", options=options)

    async def callback(self, interaction: discord.Interaction):
        pass

class UserSelect(discord.ui.UserSelect):
    def __init__(self, parent_view:ChannelAccessView):
        self.parent_view = parent_view
        super().__init__(
            placeholder="Select a user",
            min_values=1,
            max_values=1
        )

    async def callback(self, interaction: discord.Interaction):
        selected_user = self.values[0]
        await interaction.response.send_message(
            f"You selected {selected_user.mention}",
            ephemeral=True
        )
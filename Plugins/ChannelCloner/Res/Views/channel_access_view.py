from enum import Enum
import discord
from discord import VoiceChannel

class AcceptMode(Enum):
    ACCEPT = "✅ Accept"
    REJECT = "❌ Reject"
    RESET = "⚪ Clear Permissions"

class ChannelAccessView(discord.ui.View):
    def __init__(self, target_channel:VoiceChannel):
        super().__init__(timeout=None)
        self.target_channel = target_channel
        self.accept_mode:AcceptMode = AcceptMode.ACCEPT
        self.add_item(AcceptRejectSelect())
        #self.add_item(UserSelect(self))

class AcceptRejectSelect(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Accept User", emoji="✅",
                                 description=""),
            discord.SelectOption(label="Reject User", emoji="❌",
                                 description=""),
            discord.SelectOption(label="Clear User", emoji="⚪",
                                 description="")
        ]
        super().__init__(placeholder="Access Settings", options=options)

    async def callback(self, interaction: discord.Interaction):
        selected_option = self.values[0]
        mode: AcceptMode = AcceptMode.RESET
        match selected_option:
            case "Accept User":
                mode = AcceptMode.ACCEPT
            case "Reject User":
                mode = AcceptMode.REJECT
        await interaction.response.send_message(f"You selected {mode.value}.")

class UserSelect(discord.ui.UserSelect):
    def __init__(self, mode: AcceptMode):
        super().__init__(
            placeholder="Select a user",
            min_values=1,
            max_values=10
        )

    async def callback(self, interaction: discord.Interaction):
        selected_users = self.values
        mention_string:str = ""
        for selected_user in selected_users:
            mention_string += ", " + selected_user.mention
        await interaction.response.send_message(
            f"You selected {mention_string}",
            ephemeral=True
        )
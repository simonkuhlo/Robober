import discord
from discord import VoiceChannel


class ChannelEditorView(discord.ui.View):
    def __init__(self, target_channel:VoiceChannel):
        super().__init__(timeout=None)
        self.target_channel = target_channel
        self.add_item()

class AcceptRejectSelect(discord.ui.Select):
    def __init__(self, target_channel:VoiceChannel):

class WhitelistUserSelectView(discord.ui.View):
    def __init__(self, parent_view:ChannelEditorView):
        self.parent_view = parent_view
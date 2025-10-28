import discord

from SimonsPluginResources.Main.reelbot import ReelBot

async def change_user_channel_access(member:discord.Member, channel:discord.VoiceChannel, allowed:bool = None) -> None:
    if not member:
        return


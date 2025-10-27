from SimonsPluginResources.Main.reelbot import ReelBot

async def change_user_channel_access(user_id:int, channel_id:int, bot:ReelBot, allowed:bool = None) -> None:
    target_channel = bot.get_channel(channel_id)
    member = target_channel.guild.get_member(user_id)
    if not member:
        return
    overwrite = target_channel.overwrites_for(member)
    overwrite.connect = allowed
    await target_channel.set_permissions(member, overwrite=overwrite)

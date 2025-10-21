from .Res.channel_authority import ChannelAuthority

saved_authorities:dict[int, ChannelAuthority] = {}

def add_channel(channel_id:int, authority:ChannelAuthority) -> None:
    saved_authorities[channel_id] = authority

def delete_channel(channel_id:int) -> None:
    saved_authorities.pop(channel_id)

def get_channel_authority(channel_id:int) -> ChannelAuthority:
    return saved_authorities.get(channel_id, None)

def set_owner(channel_id:int, user_id:int) -> None:
    authority = get_channel_authority(channel_id)
    if not authority:
        authority = ChannelAuthority(user_id)
        add_channel(channel_id, authority)
    else:
        authority.owner = user_id

def is_user_elevated(channel_id:int, user_id:int) -> bool:
    authority = get_channel_authority(channel_id)
    if not authority:
        return False
    return authority.is_elevated(user_id)

def is_user_owner(channel_id:int, user_id:int) -> bool:
    authority = get_channel_authority(channel_id)
    if not authority:
        return False
    return authority.is_owner(user_id)
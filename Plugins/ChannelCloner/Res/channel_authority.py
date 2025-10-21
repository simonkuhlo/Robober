class ChannelAuthority:
    def __init__(self, owner:int, elevated:list[int] = []):
        self.owner:int = owner
        self.elevated:list[int] = elevated

    def is_owner(self, user_id:int) -> bool:
        return user_id == self.owner

    def is_elevated(self, user_id:int) -> bool:
        if self.is_owner(user_id):
            return True
        return user_id in self.elevated
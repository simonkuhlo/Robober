class SettingsManager:

    def __init__(self):
        self.settings:dict[str, str] = {}

    def get_setting(self, key: str) -> str:
        setting = self.settings.get(key)
        if setting is None:
            return None
        return setting

    def set_setting(self, key: str, value:str):
        self.settings[key] = value

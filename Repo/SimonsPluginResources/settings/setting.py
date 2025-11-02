from .scope import SettingScope
from .setting_sources import SettingSource
from .setting_type_hints import SettingTypeHint, SettingTypeHintString


class Setting:
    def __init__(self,
                 topic: str,
                 setting_id: str,
                 category: str = None,
                 description: str = "",
                 scope: SettingScope = SettingScope.GLOBAL,
                 type_hint: SettingTypeHint = SettingTypeHintString,
                 important: bool = True,
                 default_value: str = "",
                 current_value: str = None,
                 source: SettingSource = SettingSource("UNKNOWN"),
                 ):
        self.category: str = category
        self.scope: SettingScope = scope
        self.source: SettingSource = source
        self.topic: str = topic
        self.setting_id: str = setting_id
        self.description: str = description
        self.type_hint: SettingTypeHint = type_hint
        self.important: bool = important
        self.default_value: str = default_value
        self.current_value: str = self.default_value
        if current_value:
            self.current_value: str = current_value

    def get_path(self) -> str:
        return f"{str(self.source)}.{self.topic}.{self.setting_id}"

    def get_value(self):
        return self.type_hint.convert(self.current_value)

    def get_value_str(self) -> str:
        return self.current_value

    def set_value(self, value: str):
        if self.type_hint.type_check(value):
            self.current_value = value
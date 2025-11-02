from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..plugin import Plugin

class SettingSource:
    def __init__(self, name:str) -> None:
        self.name:str = ""

    def __str__(self) -> str:
        return self.name

class SettingSourcePlugin(SettingSource):
    def __init__(self, plugin: "Plugin") -> None:
        super().__init__(plugin.plugin_id)
        self.name:str = ""

    def __str__(self) -> str:
        return self.name

CORESETTING = SettingSource("CORE")
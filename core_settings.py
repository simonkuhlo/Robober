from SimonsPluginResources.settings.setting import Setting
from SimonsPluginResources.settings.setting_sources import CORESETTING
from SimonsPluginResources.settings.setting_type_hints import SettingTypeHintInt, SettingTypeHintString

initial_settings:list[Setting] = [
    Setting(topic="logging",
            setting_id="level",
            category="Logging",
            description="",
            type_hint=SettingTypeHintInt(),
            important=True,
            default_value="0",
            source=CORESETTING
            ),
    Setting(topic="debug_server",
            setting_id="id",
            category="Debugging",
            description="",
            type_hint=SettingTypeHintInt(),
            important=True,
            default_value="954128852051968070",
            source=CORESETTING
            ),
    Setting(topic="commands",
            setting_id="trigger",
            category="Bot",
            description="",
            type_hint=SettingTypeHintString(),
            important=True,
            default_value="!r",
            source=CORESETTING
            )
]
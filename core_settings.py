from SimonsPluginResources.settings.setting import Setting
from SimonsPluginResources.settings.type_filters import filters

initial_settings:list[Setting] = [
    Setting(topic="logging",
            setting_id="level",
            category="Logging",
            description="",
            type_filter=filters.INT,
            important=True,
            default_value="0",
            source="CORE"
            ),
    Setting(topic="debug_server",
            setting_id="id",
            category="Debugging",
            description="",
            type_filter=filters.INT,
            important=True,
            default_value="954128852051968070",
            source="CORE"
            ),
    Setting(topic="commands",
            setting_id="trigger",
            category="Bot",
            description="",
            important=True,
            default_value="!r",
            source="CORE"
            )
]
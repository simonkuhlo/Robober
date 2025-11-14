from SimonsPluginResources.settings import Setting

initial_settings:list[Setting] = [
    Setting(rel_path="logging.level", default_value="0"),
    Setting(rel_path="debug_guild.id", default_value="954128852051968070", comment="Bot must be restarted after changing value!"),
    Setting(rel_path="commands.trigger", default_value="!r", comment="Bot must be restarted after changing value!"),
]
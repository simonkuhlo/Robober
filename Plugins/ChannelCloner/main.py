from . import cog
from SimonsPluginResources.Main.plugin import Plugin

plugin_ref:Plugin

def start() -> None:
    if not plugin_ref:
        return
    if not plugin_ref.acces_share:
        return
    if not plugin_ref.access_share.bot:
        return
    plugin_ref.access_share.bot.load_extension("SimonsPluginResources")
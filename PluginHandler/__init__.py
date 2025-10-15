from . import loader

def on_bot_startup() -> None:
    loader.load_static("Plugins/WebInterface/plugin")
    for plugin in loader.loaded_plugins:
        plugin.on_startup()
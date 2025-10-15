from .res.plugin_wrapper import Plugin
import importlib
import os
from . import settings

loaded_plugins:list[Plugin] = []

def load_static(file_path:str) -> None:
    module_path = file_path.replace("/", ".")
    module = importlib.import_module(module_path)
    new_plugin = Plugin()
    new_plugin.id = module.plugin_id
    new_plugin.name = module.plugin_name
    new_plugin.desc = module.plugin_description
    new_plugin.version = module.plugin_version
    new_plugin.needs_backend_version = module.used_backend_version
    new_plugin.on_startup = module.startup_hook
    loaded_plugins.append(new_plugin)
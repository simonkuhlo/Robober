from typing import Type
from SimonsPluginResources.plugin import Plugin
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os

from .webinterface_extension import WebinterfaceExtension

class Webinterface:
    def __init__(self, plugin: Plugin, initial_extensions: list[Type[WebinterfaceExtension]] = None):
        self.parent_plugin: Plugin = plugin
        self.app = FastAPI()
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        static_dir_path = os.path.join(BASE_DIR, "visual/static")
        self.app.mount("/visual/static", StaticFiles(directory=static_dir_path), name="static")

        self.loaded_extensions: list[WebinterfaceExtension] = []
        if initial_extensions:
            for Extension in initial_extensions:
                self.load_extension(Extension(self))

    def load_extension(self, source_plugin: Plugin, Extension: Type[WebinterfaceExtension]):
        instance = Extension(source_plugin, self)
        if instance.router:
            self.app.include_router(instance.router)
        self.loaded_extensions.append(instance)
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from threading import Thread
from fastapi.staticfiles import StaticFiles
from SimonsPluginResources.environment import Environment
from SimonsPluginResources.plugin_extension import PluginExtension
from .visual import main as visual
import uvicorn
import os
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .plugin import WebInterfacePlugin

class WebInterfacePluginExtension(PluginExtension):
    def __init__(self, parent_plugin: "WebInterfacePlugin" = None):
        super().__init__(parent_plugin)
        visual.extension = self
        # Get the directory where the current file (e.g., main.py) is located
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        # Construct the path to the static directory relative to BASE_DIR
        static_dir_path = os.path.join(BASE_DIR, "visual/static")

        # --- FastAPI Web Server Setup ---
        self.app = FastAPI()
        self.app.mount("/visual/static", StaticFiles(directory=static_dir_path), name="static")
        self.app.include_router(visual.router)

        @self.app.get("/")
        async def read_root():
            return RedirectResponse(url="/visual", status_code=308)

    # Function to run the FastAPI server in a separate thread
    def run_webinterface(self):
        uvicorn.run(self.app, host="localhost", port=8000)

    def _start(self) -> None:
        api_thread = Thread(target=self.run_webinterface, daemon=True)
        api_thread.start()


from distutils.extension import Extension

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from threading import Thread
from fastapi.staticfiles import StaticFiles
from SimonsPluginResources.environment import Environment
from SimonsPluginResources.plugin_extension import PluginExtension
from .visual import main as visual
from .bot_api.main import router as bot_api_router
from .bot_api import main as bot_api
import uvicorn
import os
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .plugin import WebInterfacePlugin

class WebInterfacePluginExtension(PluginExtension):
    def __init__(self, parent_plugin: "WebInterfacePlugin" = None):
        super().__init__(parent_plugin)
        bot_api.extension = self
        visual.extension = self
        global extension
        extension = self
    def _start(self) -> None:
        on_startup()

extension: WebInterfacePluginExtension
# Get the directory where the current file (e.g., main.py) is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Construct the path to the static directory relative to BASE_DIR
static_dir_path = os.path.join(BASE_DIR, "visual/static")

# --- FastAPI Web Server Setup ---
app = FastAPI()
app.mount("/visual/static", StaticFiles(directory=static_dir_path), name="static")
app.include_router(visual.router)
app.include_router(bot_api_router)

@app.get("/")
async def read_root():
    return RedirectResponse(url="/visual", status_code=308)

# Function to run the FastAPI server in a separate thread
def run_webinterface():
    uvicorn.run(app, host="localhost", port=8000)

def on_startup() -> None:
    api_thread = Thread(target=run_webinterface, daemon=True)
    api_thread.start()
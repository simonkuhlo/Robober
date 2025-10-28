from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from threading import Thread
from fastapi.staticfiles import StaticFiles
from SimonsPluginResources.Main.plugin_host import PluginHost
from SimonsPluginResources.Main.access_share import AccessShare
from . import bot_api
from .visual.main import router as visual_router
from .bot_api.main import router as bot_api_router
from .bot_api import main as bot_api
import uvicorn
import core_settings
import os

# Get the directory where the current file (e.g., main.py) is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Construct the path to the static directory relative to BASE_DIR
static_dir_path = os.path.join(BASE_DIR, "visual/static")

# --- FastAPI Web Server Setup ---
plugin_host:PluginHost
app = FastAPI()
app.mount("/visual/static", StaticFiles(directory=static_dir_path), name="static")
app.include_router(visual_router)
app.include_router(bot_api_router)

@app.get("/")
async def read_root():
    return RedirectResponse(url="/visual", status_code=308)

@app.get("/bot-status")
async def bot_status():
    bot = plugin_host.access_share.bot
    # Example: return the current bot latency
    return {"latency_ms": round(bot.latency * 1000)}

@app.get("/loglevel")
async def get_status():
    return core_settings.log_level

@app.post("/loglevel")
async def set_loglevel(update: int):
    # Update the shared variable
    core_settings.log_level = update
    return {"message": "Status updated", "new_status": core_settings.log_level}


# Function to run the FastAPI server in a separate thread
def run_api(current_plugin_host: PluginHost):
    global plugin_host
    plugin_host = current_plugin_host
    bot_api.plugin_host = plugin_host
    uvicorn.run(app, host="localhost", port=8000)


def on_startup() -> None:
    api_thread = Thread(target=run_api, daemon=True)
    api_thread.start()
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from threading import Thread
from fastapi.staticfiles import StaticFiles
from SimonsPluginResources.environment import Environment
from .visual import main as visual
from .bot_api.main import router as bot_api_router
from .bot_api import main as bot_api
import uvicorn
import os

# Get the directory where the current file (e.g., main.py) is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Construct the path to the static directory relative to BASE_DIR
static_dir_path = os.path.join(BASE_DIR, "visual/static")

# --- FastAPI Web Server Setup ---
environment: Environment
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

def on_startup(current_environment: Environment) -> None:
    global environment
    environment = current_environment
    bot_api.environment = environment
    visual.environment = environment
    api_thread = Thread(target=run_webinterface, daemon=True)
    api_thread.start()
from fastapi import FastAPI
from threading import Thread
from PluginResources.plugin import Plugin
import uvicorn
import settings

# --- FastAPI Web Server Setup ---
app = FastAPI()
plugin_ref:Plugin

@app.get("/")
async def read_root():
    return {"message": "Discord bot web interface is running."}

@app.get("/bot-status")
async def bot_status():
    bot = plugin_ref.access_share.bot
    # Example: return the current bot latency
    return {"latency_ms": round(bot.latency * 1000)}

@app.get("/loglevel")
async def get_status():
    return settings.log_level

@app.post("/loglevel")
async def set_loglevel(update: int):
    # Update the shared variable
    settings.log_level = update
    return {"message": "Status updated", "new_status": settings.log_level}


# Function to run the FastAPI server in a separate thread
def run_api():
    uvicorn.run(app, host="0.0.0.0", port=8000)


def on_startup() -> None:
    # Start FastAPI in a background thread
    print("Starting up...")
    api_thread = Thread(target=run_api, daemon=True)
    api_thread.start()
import asyncio

from fastapi import APIRouter, Request

from SimonsPluginResources.Main.plugin_host import PluginHost
from SimonsPluginResources.Main.plugin import Plugin
router = APIRouter(prefix="/bot", tags=["api", "bot"])
plugin_host:PluginHost

@router.get("/start")
async def start_bot(request: Request):
    bot = plugin_host.access_share.bot
    future = asyncio.run_coroutine_threadsafe(bot.start(), bot.loop)
    future.result()
    return {"message": "Bot started!"}

@router.get("/stop")
async def stop_bot(request: Request):
    bot = plugin_host.access_share.bot
    future = asyncio.run_coroutine_threadsafe(bot.close(), bot.loop)
    future.result()
    return {"message": "Bot stopped!"}

@router.get("/clear")
async def clear_bot(request: Request):
    bot = plugin_host.access_share.bot
    bot.clear()
    return {"message": "Bot restarted!"}
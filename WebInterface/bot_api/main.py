import asyncio

from fastapi import APIRouter, Request
from SimonsPluginResources.Main.plugin import Plugin
router = APIRouter()

plugin_ref:Plugin

@router.get("/start")
async def start_bot(request: Request):
    bot = plugin_ref.access_share.bot
    asyncio.run_coroutine_threadsafe(bot.start(), bot.loop)
    return {"message": "Bot started!"}

@router.get("/stop")
async def stop_bot(request: Request):
    bot = plugin_ref.access_share.bot
    asyncio.run_coroutine_threadsafe(bot.close(), bot.loop)
    return {"message": "Bot stopped!"}

@router.get("/clear")
async def clear_bot(request: Request):
    bot = plugin_ref.access_share.bot
    bot.clear()
    return {"message": "Bot restarted!"}
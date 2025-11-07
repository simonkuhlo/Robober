import asyncio
from fastapi import APIRouter, Request
from dotenv import get_key
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Plugins.WebInterface.main import WebInterfacePluginExtension
extension: "WebInterfacePluginExtension"
router = APIRouter(prefix="/bot", tags=["api", "bot"])

@router.get("/start")
async def start_bot(request: Request):
    bot = extension.parent_plugin.environment.bot
    bot_token = get_key(".env", 'BOT_TOKEN')
    asyncio.run_coroutine_threadsafe(bot.start(bot_token), bot.loop)
    return {"message": "Bot started!"}

@router.get("/stop")
async def stop_bot(request: Request):
    bot = extension.parent_plugin.environment.bot
    asyncio.run_coroutine_threadsafe(bot.close(), bot.loop)
    return {"message": "Bot stopped!"}

@router.get("/clear")
async def clear_bot(request: Request):
    bot = extension.parent_plugin.environment.bot
    bot.clear()
    return {"message": "Bot restarted!"}
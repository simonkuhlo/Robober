import asyncio
from fastapi import APIRouter, Request
from dotenv import get_key

router = APIRouter(prefix="/bot", tags=["api", "bot"])
plugin_ref = None

@router.get("/start")
async def start_bot(request: Request):
    bot = plugin_ref.environment.bot
    bot_token = get_key(".env", 'BOT_TOKEN')
    asyncio.run_coroutine_threadsafe(bot.start(bot_token), bot.loop)
    return {"message": "Bot started!"}

@router.get("/stop")
async def stop_bot(request: Request):
    bot = plugin_ref.environment.bot
    asyncio.run_coroutine_threadsafe(bot.close(), bot.loop)
    return {"message": "Bot stopped!"}

@router.get("/clear")
async def clear_bot(request: Request):
    bot = plugin_ref.environment.bot
    bot.clear()
    return {"message": "Bot restarted!"}
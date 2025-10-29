import asyncio
from fastapi import APIRouter, Request
from SimonsPluginResources.environment import Environment

router = APIRouter(prefix="/bot", tags=["api", "bot"])
environment:Environment

@router.get("/start")
async def start_bot(request: Request):
    bot = environment.bot
    future = asyncio.run_coroutine_threadsafe(bot.start(), bot.loop)
    future.result()
    return {"message": "Bot started!"}

@router.get("/stop")
async def stop_bot(request: Request):
    bot = environment.bot
    future = asyncio.run_coroutine_threadsafe(bot.close(), bot.loop)
    future.result()
    return {"message": "Bot stopped!"}

@router.get("/clear")
async def clear_bot(request: Request):
    bot = environment.bot
    bot.clear()
    return {"message": "Bot restarted!"}
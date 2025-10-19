from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import os

templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "static"))

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def get_select(request: Request):
    return templates.TemplateResponse("base.j2", {"request": request})

@router.get("/home", response_class=HTMLResponse)
async def settings_interface(request: Request):
    return templates.TemplateResponse("home_page.j2", {"request": request})

@router.get("/status", response_class=HTMLResponse)
async def settings_interface(request: Request):
    return templates.TemplateResponse("status_page.j2", {"request": request})

@router.get("/settings", response_class=HTMLResponse)
async def settings_interface(request: Request):
    return templates.TemplateResponse("settings_page.j2", {"request": request})

@router.get("/plugins", response_class=HTMLResponse)
async def plugin_interface(request: Request):
    return templates.TemplateResponse("plugin_page.j2", {"request": request})



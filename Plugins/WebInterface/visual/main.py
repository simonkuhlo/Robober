from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
import os

templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "static"))

router = APIRouter(prefix="/visual")

@router.get("/", response_class=RedirectResponse)
async def main():
    return RedirectResponse(url=f"{router.prefix}/home", status_code=307)

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
    return templates.TemplateResponse("/plugins/plugin_page.j2", {"request": request})



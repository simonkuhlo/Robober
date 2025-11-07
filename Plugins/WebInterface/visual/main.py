from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
import os
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Plugins.WebInterface.main import WebInterfacePluginExtension
from SimonsPluginResources.environment import Environment
from SimonsPluginResources.plugin import Status as Status

from SimonsPluginResources.plugin_request import PluginRequest

extension: "WebInterfacePluginExtension"

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
    global extension
    latency = extension.parent_plugin.environment.bot.latency
    return templates.TemplateResponse("status_page.j2", {"request": request, "latency": latency})

@router.get("/settings", response_class=HTMLResponse)
async def settings_interface(request: Request):
    global extension
    settings = extension.parent_plugin.environment.settings.get_settings()
    return templates.TemplateResponse("settings_page.j2", {"request": request, "settings": settings})

@router.get("/plugins", response_class=HTMLResponse)
async def plugin_interface(request: Request):
    global extension
    plugins = extension.parent_plugin.host_plugin.get_loaded_plugins()
    return templates.TemplateResponse("/plugins/plugin_page.j2", {"request": request, "plugins":plugins, "Status" : Status})

@router.get("/plugins/{plugin_id}", response_class=HTMLResponse)
async def plugin_details(request: Request, plugin_id: str):
    global extension
    plugin = extension.parent_plugin.host_plugin.get_loaded_plugin(PluginRequest(plugin_id))
    return templates.TemplateResponse("/plugins/plugin_details.j2", {"request": request, "plugin":plugin, "Status" : Status})


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
    return templates.TemplateResponse("/plugins/plugin_list.j2", {"request": request, "plugins":plugins, "Status" : Status})

@router.get("/plugins/{plugin_id}", response_class=HTMLResponse)
async def plugin_details(request: Request, plugin_id: str):
    global extension
    plugin = extension.parent_plugin.host_plugin.get_loaded_plugin(PluginRequest(plugin_id))
    return templates.TemplateResponse("plugins/plugin_inspector.j2", {"request": request, "plugin":plugin, "Status" : Status})

@router.get("/plugins/{plugin_id}/plugin_view", response_class=HTMLResponse)
async def plugin_view(request: Request, plugin_id: str):
    global extension
    plugin = extension.parent_plugin.host_plugin.get_loaded_plugin(PluginRequest(plugin_id))
    module_path = plugin.get_module_path()
    rel_path = os.path.abspath(module_path)
    target_file_path = f"{rel_path}/External/WebInterface"
    temp_templates = Jinja2Templates(target_file_path)
    return temp_templates.TemplateResponse("view.j2", {"request": request, "plugin" : plugin})

@router.get("/plugins/{plugin_id}/plugin_settings", response_class=HTMLResponse)
async def plugin_settings(request: Request, plugin_id: str):
    global extension
    plugin = extension.parent_plugin.host_plugin.get_loaded_plugin(PluginRequest(plugin_id))
    return templates.TemplateResponse("plugins/plugin_settings.j2", {"request": request, "plugin" : plugin})

@router.get("/plugins/{plugin_id}/plugin_integrations", response_class=HTMLResponse)
async def plugin_integrations(request: Request, plugin_id: str):
    global extension
    plugin = extension.parent_plugin.host_plugin.get_loaded_plugin(PluginRequest(plugin_id))
    return templates.TemplateResponse("plugins/plugin_integrations.j2", {"request": request, "plugin" : plugin})

@router.get("/plugins/{plugin_id}/plugin_logs", response_class=HTMLResponse)
async def plugin_logs(request: Request, plugin_id: str):
    global extension
    plugin = extension.parent_plugin.host_plugin.get_loaded_plugin(PluginRequest(plugin_id))
    return templates.TemplateResponse("plugins/plugin_logs.j2", {"request": request, "plugin" : plugin})
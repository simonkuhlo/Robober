# Plugin file template for Backend version 0

from . import main

#INFO
plugin_id:str = "WEBINTERFACE"
plugin_name:str = "Webinterface"
plugin_description:str = "Webinterface"
plugin_version:int = 0
used_backend_version:int = 0

#Gets called on Application Startup
def startup_hook() -> None:
    main.on_startup()
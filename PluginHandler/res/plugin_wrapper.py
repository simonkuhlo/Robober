from collections.abc import Callable
from symtable import Function


class Plugin:

    id:str
    name:str
    desc:str
    version:int
    needs_backend_version:int

    bot_ref = None

    on_startup:Callable
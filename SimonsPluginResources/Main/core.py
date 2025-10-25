import asyncio
from threading import Thread

from Plugins.ChannelCloner.plugin import ChannelCloner as ChannelClonerCog
from main import plugin_host
from .access_share import AccessShare
from .plugin_host import PluginHost
from .settings import SettingsManager
from .reelbot import ReelBot
from WebInterface import main as webinterface

class CoreApp:
    def __init__(self):
        self.settings = SettingsManager()
        self.bot = ReelBot()
        self.bot.signal_ready.connect(self.on_bot_ready)
        self.access_share = AccessShare(self.settings, self.bot)
        self.plugin_host:PluginHost = PluginHost(self.access_share)
        self.bot.system_cogs.extend(self.plugin_host.system_cogs)
        self.bot_token: str = None
        self.webinterface_thread:Thread = Thread(target=self.run_webinterface, daemon=True)
        self.bot_thread:Thread = Thread(target=self.run_bot, daemon=True)

    def on_bot_ready(self):
        #self.plugin_host.reload_cogs()
        pass

    def run_bot(self) -> None:
        asyncio.set_event_loop(asyncio.new_event_loop())  # Create a new event loop for the thread
        self.bot.run(self.bot_token)

    def run_webinterface(self) -> None:
        asyncio.set_event_loop(asyncio.new_event_loop())
        webinterface.run_api()

    def start(self) -> None:
        self.plugin_host.start()
        self.webinterface_thread.start()
        self.bot_thread.start()
        while True:
            cmd = input("Type /quit to exit: ")
            match cmd.strip():
                case "/quit":
                    print("Exiting...")
                    break
                case "/status webinterface":
                    print("Webinterface status: ", self.webinterface_thread.is_alive())
                case "/status bot":
                    print("Bot status: ", self.bot_thread.is_alive())
                case "/plugins reload_cogs":
                    self.plugin_host.reload_cogs()
                case _:
                    print("Unknown command.")
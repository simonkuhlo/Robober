from .res import LogLevel, DefaultLogLevels, LogMessage
from datetime import datetime


## Prints a given Message and saves it to the log cache
class Logger:
    @staticmethod
    def log(msg:str, level:LogLevel = DefaultLogLevels.INFO):
        logmessage:LogMessage = LogMessage(datetime.now().timestamp(), level, msg)
        print(logmessage)

logger:Logger = Logger()
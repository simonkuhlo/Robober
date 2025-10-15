from enum import Enum
from dataclasses import dataclass

@dataclass(frozen=True)
class LogLevel:
    num: int
    label: str
    description: str

@dataclass(frozen=True)
class LogMessage:
    timestamp: float
    level: LogLevel
    message: str
    def __str__(self) -> str:
        output:str = self.level.label + ": " + self.message
        return output

class DefaultLogLevels:
    DEBUG = LogLevel(1, "[DEBUG]", "Debugging")
    INFO = LogLevel(2, "[INFO]", "Information")
    WARNING = LogLevel(3, "[WARN]", "Warning")
    ERROR = LogLevel(4, "[ERROR]", "Error")
class SettingTypeHint:
    def __init__(self):
        self.type_name:str

    def convert(self, value:str):
        return value

    def type_check(self, value:str) -> bool:
        if value:
            return True
        return True

class SettingTypeHintString(SettingTypeHint):
    def __init__(self):
        super().__init__()
        self.type_name = "String"

    def convert(self, value:str) -> str:
        return value

    def type_check(self, value:str) -> bool:
        return True

class SettingTypeHintBoolean(SettingTypeHint):
    def __init__(self):
        super().__init__()
        self.type_name = "Boolean"

    def convert(self, value:str) -> bool:
        match value:
            case "true":
                return True
            case "false":
                return False
        return None

    def type_check(self, value:str) -> bool:
        if value in ["true", "false"]:
            return True
        return False

class SettingTypeHintInt(SettingTypeHint):
    def __init__(self):
        super().__init__()
        self.type_name = "Integer"

    def convert(self, value:str) -> int:
        return int(value)

    def type_check(self, value:str) -> bool:
        try:
            int(value)
        except Exception:
            return False
        return True
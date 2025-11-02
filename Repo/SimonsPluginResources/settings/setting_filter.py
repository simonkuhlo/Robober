from .setting import Setting


class SettingFilter:
    def filter(self, setting: Setting) -> bool:
        return True

    def filter_ist(self, setting_list:list[Setting]) -> list[Setting]:
        returned_list: list[Setting] = []
        for setting in setting_list:
            if self.filter(setting):
                returned_list.append(setting)
        return returned_list

class SettingPathFilter:
    def __init__(self, path: str):
        self.path:str = path

    def filter(self, setting: Setting) -> bool:
        if setting.get_path() == self.path:
            return True
        return False

class SettingSourceNameFilter:
    def __init__(self, source_name: str):
        self.source_name: str = source_name

    def filter(self, setting: Setting) -> bool:
        if setting.source.name == self.source_name:
            return True
        return False

class SettingCategoryFilter:
    def __init__(self, category: str):
        self.category: str = category

    def filter(self, setting: Setting) -> bool:
        if setting.category == self.category:
            return True
        return False
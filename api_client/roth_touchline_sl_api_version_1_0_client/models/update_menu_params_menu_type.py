from enum import Enum

class UpdateMenuParamsMenuType(str, Enum):
    MI = "MI"
    MP = "MP"
    MS = "MS"
    MU = "MU"

    def __str__(self) -> str:
        return str(self.value)

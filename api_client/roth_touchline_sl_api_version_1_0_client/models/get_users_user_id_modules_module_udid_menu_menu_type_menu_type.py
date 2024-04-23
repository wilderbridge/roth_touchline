from enum import Enum

class GetUsersUserIdModulesModuleUdidMenuMenuTypeMenuType(str, Enum):
    MI = "MI"
    MP = "MP"
    MS = "MS"
    MU = "MU"

    def __str__(self) -> str:
        return str(self.value)

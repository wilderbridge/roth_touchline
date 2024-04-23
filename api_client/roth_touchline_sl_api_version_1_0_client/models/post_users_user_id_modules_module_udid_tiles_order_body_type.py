from enum import Enum

class PostUsersUserIdModulesModuleUdidTilesOrderBodyType(str, Enum):
    CONTAINERS = "containers"
    TILES = "tiles"
    ZONES_SYSTEM_CONTAINERS = "zones_system_containers"

    def __str__(self) -> str:
        return str(self.value)

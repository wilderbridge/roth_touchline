from enum import Enum

class PostUsersUserIdNotificationsTimeBodyNotificationType(str, Enum):
    ERROR = "error"
    INFO = "info"
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)

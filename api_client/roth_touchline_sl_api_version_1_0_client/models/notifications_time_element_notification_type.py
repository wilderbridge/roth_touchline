from enum import Enum

class NotificationsTimeElementNotificationType(str, Enum):
    ERROR = "error"
    INFO = "info"
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)

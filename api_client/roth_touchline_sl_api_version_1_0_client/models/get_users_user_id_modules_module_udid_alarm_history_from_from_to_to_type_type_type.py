from enum import Enum

class GetUsersUserIdModulesModuleUdidAlarmHistoryFromFromToToTypeTypeType(str, Enum):
    ALARM = "alarm"
    ALL = "all"
    NOTIFICATION = "notification"
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)

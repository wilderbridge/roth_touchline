from enum import Enum

class GetModulesModuleUuidStatisticsTypeRangeRangeMonthRange(str, Enum):
    MONTH = "month"

    def __str__(self) -> str:
        return str(self.value)

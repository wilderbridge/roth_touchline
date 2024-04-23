from enum import Enum

class GetModulesModuleUuidStatisticsTypeRangeRangeRange(str, Enum):
    DAY = "day"
    HOUR = "hour"
    MONTH = "month"
    TOTAL = "total"
    WEEK = "week"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum

class GetModulesModuleUuidStatisticsTypeRangeRangeMonthMonthYearYearRange(str, Enum):
    MONTH = "month"

    def __str__(self) -> str:
        return str(self.value)

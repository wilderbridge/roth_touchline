from enum import Enum

class GetModulesModuleUuidStatisticsTypeRangeRangeMonthType(str, Enum):
    LINEAR = "linear"

    def __str__(self) -> str:
        return str(self.value)

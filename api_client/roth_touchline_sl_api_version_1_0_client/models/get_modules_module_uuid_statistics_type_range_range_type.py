from enum import Enum

class GetModulesModuleUuidStatisticsTypeRangeRangeType(str, Enum):
    COLD_DELIVERED = "cold_delivered"
    CONSUMPTIONS = "consumptions"
    ENERGY_ACQUIRED_GWC = "energy_acquired_gwc"
    EXHAUST_FAN_ENERGY_CONSUMPTION = "exhaust_fan_energy_consumption"
    LINEAR = "linear"
    PRELIMINARY_HEATER_ENERGY_CONSUMPTION = "preliminary_heater_energy_consumption"
    SUPPLY_FAN_ENERGY_CONSUMPTION = "supply_fan_energy_consumption"
    TEMPERATURE_EFFICIENCY = "temperature_efficiency"
    WARM_DELIVERED = "warm_delivered"
    YIELDS = "yields"

    def __str__(self) -> str:
        return str(self.value)

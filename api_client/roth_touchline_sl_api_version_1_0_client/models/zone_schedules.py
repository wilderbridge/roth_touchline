from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from ..types import UNSET, Unset
from typing import Dict
from typing import Union

if TYPE_CHECKING:
  from ..models.zone_schedules_schedule import ZoneSchedulesSchedule





T = TypeVar("T", bound="ZoneSchedules")


@_attrs_define
class ZoneSchedules:
    """ 
        Attributes:
            mode_id (Union[Unset, int]): id of the mode object (nakładka) connected to the zone
            schedule (Union[Unset, ZoneSchedulesSchedule]):
     """

    mode_id: Union[Unset, int] = UNSET
    schedule: Union[Unset, 'ZoneSchedulesSchedule'] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.zone_schedules_schedule import ZoneSchedulesSchedule
        mode_id = self.mode_id

        schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if mode_id is not UNSET:
            field_dict["modeId"] = mode_id
        if schedule is not UNSET:
            field_dict["schedule"] = schedule

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.zone_schedules_schedule import ZoneSchedulesSchedule
        d = src_dict.copy()
        mode_id = d.pop("modeId", UNSET)

        _schedule = d.pop("schedule", UNSET)
        schedule: Union[Unset, ZoneSchedulesSchedule]
        if isinstance(_schedule,  Unset):
            schedule = UNSET
        else:
            schedule = ZoneSchedulesSchedule.from_dict(_schedule)




        zone_schedules = cls(
            mode_id=mode_id,
            schedule=schedule,
        )

        zone_schedules.additional_properties = d
        return zone_schedules

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

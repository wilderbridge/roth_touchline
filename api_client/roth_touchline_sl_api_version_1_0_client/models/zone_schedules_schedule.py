from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from typing import cast, List
from typing import cast
from typing import Dict
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.zone_schedules_schedule_p1_intervals_item import ZoneSchedulesScheduleP1IntervalsItem





T = TypeVar("T", bound="ZoneSchedulesSchedule")


@_attrs_define
class ZoneSchedulesSchedule:
    """ 
        Attributes:
            id (Union[Unset, int]): id of the global schedule connected to specified module
            index (Union[Unset, float]): index of the global schedule (0 to 4) Example: -1.
            p_0_days (Union[Unset, List[str]]): array of days turned on/off for program 1(1 - on, 0 - off). Values must be
                opposites of p1Days. Example: ['0', '0', '0', '0', '0', '1', '1'].
            p_0_intervals (Union[Unset, List[str]]): group of intervals for program 1. Maximum 3 intervals (can be empty) -
                each interval requires 3 properties: start, stop and temp
                 - start/stop define the starting/stopping times for the interval
                 - start/stop represent time in minutes. Min 0, Max 1440
                 - temp defines the temperature for the interval (x10). Min 50 max 350. eg. {start: 480, stop: 960, temp 200}
                from 8:00 - 16:00 temperature will be 20 degrees celsius
            p_0_setback_temp (Union[Unset, int]): temperature for anytime not covered by p0Intervals. Min 50 max 350.
            p_1_days (Union[Unset, List[str]]): array of days turned on/off for program 2(1 - on, 0 - off). Values must be
                opposites of Example: ['0', '0', '0', '0', '0', '1', '1'].
            p_1_intervals (Union[Unset, List['ZoneSchedulesScheduleP1IntervalsItem']]): group of intervals for program 2.
                Maximum 3 intervals (can be empty)
                                                  - each interval requires 3 properties: start, stop and temp
                                                  - start/stop define the starting/stopping times for the interval
                                                  - start/stop represent time in minutes. Min 0, Max 1440
                                                  - temp defines the temperature for the interval (x10). Min 50 max 350.
                                                  eg. {start: 480, stop: 960, temp 200} from 8:00 - 16:00 temperature will be 20
                degrees celsius
                 Example: [{start:480, stop: 1320, temp: 260}].
            p_1_setback_temp (Union[Unset, int]): temperature for any time not covered by p1Intervals. Min 50 max 350
     """

    id: Union[Unset, int] = UNSET
    index: Union[Unset, float] = UNSET
    p_0_days: Union[Unset, List[str]] = UNSET
    p_0_intervals: Union[Unset, List[str]] = UNSET
    p_0_setback_temp: Union[Unset, int] = UNSET
    p_1_days: Union[Unset, List[str]] = UNSET
    p_1_intervals: Union[Unset, List['ZoneSchedulesScheduleP1IntervalsItem']] = UNSET
    p_1_setback_temp: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.zone_schedules_schedule_p1_intervals_item import ZoneSchedulesScheduleP1IntervalsItem
        id = self.id

        index = self.index

        p_0_days: Union[Unset, List[str]] = UNSET
        if not isinstance(self.p_0_days, Unset):
            p_0_days = self.p_0_days





        p_0_intervals: Union[Unset, List[str]] = UNSET
        if not isinstance(self.p_0_intervals, Unset):
            p_0_intervals = self.p_0_intervals





        p_0_setback_temp = self.p_0_setback_temp

        p_1_days: Union[Unset, List[str]] = UNSET
        if not isinstance(self.p_1_days, Unset):
            p_1_days = self.p_1_days





        p_1_intervals: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.p_1_intervals, Unset):
            p_1_intervals = []
            for p_1_intervals_item_data in self.p_1_intervals:
                p_1_intervals_item = p_1_intervals_item_data.to_dict()
                p_1_intervals.append(p_1_intervals_item)





        p_1_setback_temp = self.p_1_setback_temp


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if index is not UNSET:
            field_dict["index"] = index
        if p_0_days is not UNSET:
            field_dict["p0Days"] = p_0_days
        if p_0_intervals is not UNSET:
            field_dict["p0Intervals"] = p_0_intervals
        if p_0_setback_temp is not UNSET:
            field_dict["p0SetbackTemp"] = p_0_setback_temp
        if p_1_days is not UNSET:
            field_dict["p1Days"] = p_1_days
        if p_1_intervals is not UNSET:
            field_dict["p1Intervals"] = p_1_intervals
        if p_1_setback_temp is not UNSET:
            field_dict["p1SetbackTemp"] = p_1_setback_temp

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.zone_schedules_schedule_p1_intervals_item import ZoneSchedulesScheduleP1IntervalsItem
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        index = d.pop("index", UNSET)

        p_0_days = cast(List[str], d.pop("p0Days", UNSET))


        p_0_intervals = cast(List[str], d.pop("p0Intervals", UNSET))


        p_0_setback_temp = d.pop("p0SetbackTemp", UNSET)

        p_1_days = cast(List[str], d.pop("p1Days", UNSET))


        p_1_intervals = []
        _p_1_intervals = d.pop("p1Intervals", UNSET)
        for p_1_intervals_item_data in (_p_1_intervals or []):
            p_1_intervals_item = ZoneSchedulesScheduleP1IntervalsItem.from_dict(p_1_intervals_item_data)



            p_1_intervals.append(p_1_intervals_item)


        p_1_setback_temp = d.pop("p1SetbackTemp", UNSET)

        zone_schedules_schedule = cls(
            id=id,
            index=index,
            p_0_days=p_0_days,
            p_0_intervals=p_0_intervals,
            p_0_setback_temp=p_0_setback_temp,
            p_1_days=p_1_days,
            p_1_intervals=p_1_intervals,
            p_1_setback_temp=p_1_setback_temp,
        )

        zone_schedules_schedule.additional_properties = d
        return zone_schedules_schedule

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

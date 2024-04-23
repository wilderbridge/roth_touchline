from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="ZoneMode")


@_attrs_define
class ZoneMode:
    """
        Attributes:
            id (Union[Unset, int]):
            parent_id (Union[Unset, int]):
            mode (Union[Unset, str]):  Example: constantTemp.
            const_temp_time (Union[Unset, int]):
            set_temperature (Union[Unset, int]):
            schedule_index (Union[Unset, int]):
     """

    id: Union[Unset, int] = UNSET
    parent_id: Union[Unset, int] = UNSET
    mode: Union[Unset, str] = UNSET
    const_temp_time: Union[Unset, int] = UNSET
    set_temperature: Union[Unset, int] = UNSET
    schedule_index: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        parent_id = self.parent_id

        mode = self.mode

        const_temp_time = self.const_temp_time

        set_temperature = self.set_temperature

        schedule_index = self.schedule_index


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if mode is not UNSET:
            field_dict["mode"] = mode
        if const_temp_time is not UNSET:
            field_dict["constTempTime"] = const_temp_time
        if set_temperature is not UNSET:
            field_dict["setTemperature"] = set_temperature
        if schedule_index is not UNSET:
            field_dict["scheduleIndex"] = schedule_index

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        parent_id = d.pop("parentId", UNSET)

        mode = d.pop("mode", UNSET)

        const_temp_time = d.pop("constTempTime", UNSET)

        set_temperature = d.pop("setTemperature", UNSET)

        schedule_index = d.pop("scheduleIndex", UNSET)

        zone_mode = cls(
            id=id,
            parent_id=parent_id,
            mode=mode,
            const_temp_time=const_temp_time,
            set_temperature=set_temperature,
            schedule_index=schedule_index,
        )

        zone_mode.additional_properties = d
        return zone_mode

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

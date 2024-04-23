from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="TileType41")


@_attrs_define
class TileType41:
    """ 
        Attributes:
            description (Union[Unset, str]): Date
            year (Union[Unset, int]):  Example: 2020.
            month (Union[Unset, int]):  Example: 12.
            day (Union[Unset, int]):  Example: 28.
            day_id (Union[Unset, int]):  Example: 5.
            hours (Union[Unset, int]):  Example: [0..24].
            minutes (Union[Unset, int]):  Example: 32.
     """

    description: Union[Unset, str] = UNSET
    year: Union[Unset, int] = UNSET
    month: Union[Unset, int] = UNSET
    day: Union[Unset, int] = UNSET
    day_id: Union[Unset, int] = UNSET
    hours: Union[Unset, int] = UNSET
    minutes: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        year = self.year

        month = self.month

        day = self.day

        day_id = self.day_id

        hours = self.hours

        minutes = self.minutes


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if year is not UNSET:
            field_dict["year"] = year
        if month is not UNSET:
            field_dict["month"] = month
        if day is not UNSET:
            field_dict["day"] = day
        if day_id is not UNSET:
            field_dict["dayId"] = day_id
        if hours is not UNSET:
            field_dict["hours"] = hours
        if minutes is not UNSET:
            field_dict["minutes"] = minutes

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        year = d.pop("year", UNSET)

        month = d.pop("month", UNSET)

        day = d.pop("day", UNSET)

        day_id = d.pop("dayId", UNSET)

        hours = d.pop("hours", UNSET)

        minutes = d.pop("minutes", UNSET)

        tile_type_41 = cls(
            description=description,
            year=year,
            month=month,
            day=day,
            day_id=day_id,
            hours=hours,
            minutes=minutes,
        )

        tile_type_41.additional_properties = d
        return tile_type_41

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

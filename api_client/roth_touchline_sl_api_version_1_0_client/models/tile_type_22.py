from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="TileType22")


@_attrs_define
class TileType22:
    """ 
        Attributes:
            description (Union[Unset, str]): Fan
            working_status (Union[Unset, bool]):  Example: 1.
            txt_id (Union[Unset, int]):  Example: 11.
            fan_number (Union[Unset, int]):  Example: 4.
            gear (Union[Unset, int]):  Example: 1.
     """

    description: Union[Unset, str] = UNSET
    working_status: Union[Unset, bool] = UNSET
    txt_id: Union[Unset, int] = UNSET
    fan_number: Union[Unset, int] = UNSET
    gear: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        working_status = self.working_status

        txt_id = self.txt_id

        fan_number = self.fan_number

        gear = self.gear


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if working_status is not UNSET:
            field_dict["workingStatus"] = working_status
        if txt_id is not UNSET:
            field_dict["txtId"] = txt_id
        if fan_number is not UNSET:
            field_dict["fanNumber"] = fan_number
        if gear is not UNSET:
            field_dict["gear"] = gear

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        working_status = d.pop("workingStatus", UNSET)

        txt_id = d.pop("txtId", UNSET)

        fan_number = d.pop("fanNumber", UNSET)

        gear = d.pop("gear", UNSET)

        tile_type_22 = cls(
            description=description,
            working_status=working_status,
            txt_id=txt_id,
            fan_number=fan_number,
            gear=gear,
        )

        tile_type_22.additional_properties = d
        return tile_type_22

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

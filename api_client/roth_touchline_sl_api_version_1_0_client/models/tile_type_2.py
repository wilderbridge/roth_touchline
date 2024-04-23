from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="TileType2")


@_attrs_define
class TileType2:
    """ 
        Attributes:
            description (Union[Unset, str]): Fire sensor Example: Fire sensor.
            working_status (Union[Unset, int]):  Example: 1.
            value (Union[Unset, int]):
     """

    description: Union[Unset, str] = UNSET
    working_status: Union[Unset, int] = UNSET
    value: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        working_status = self.working_status

        value = self.value


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if working_status is not UNSET:
            field_dict["workingStatus"] = working_status
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        working_status = d.pop("workingStatus", UNSET)

        value = d.pop("value", UNSET)

        tile_type_2 = cls(
            description=description,
            working_status=working_status,
            value=value,
        )

        tile_type_2.additional_properties = d
        return tile_type_2

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

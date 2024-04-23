from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="TileType32")


@_attrs_define
class TileType32:
    """ 
        Attributes:
            description (Union[Unset, str]): Disinfection
            txt_id (Union[Unset, int]):  Example: 12.
            percentage (Union[Unset, int]):  Example: 40.
     """

    description: Union[Unset, str] = UNSET
    txt_id: Union[Unset, int] = UNSET
    percentage: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        txt_id = self.txt_id

        percentage = self.percentage


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if txt_id is not UNSET:
            field_dict["txtId"] = txt_id
        if percentage is not UNSET:
            field_dict["percentage"] = percentage

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        txt_id = d.pop("txtId", UNSET)

        percentage = d.pop("percentage", UNSET)

        tile_type_32 = cls(
            description=description,
            txt_id=txt_id,
            percentage=percentage,
        )

        tile_type_32.additional_properties = d
        return tile_type_32

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

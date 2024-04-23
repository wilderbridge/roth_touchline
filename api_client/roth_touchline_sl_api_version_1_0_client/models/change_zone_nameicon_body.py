from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ChangeZoneNameiconBody")


@_attrs_define
class ChangeZoneNameiconBody:
    """ 
        Attributes:
            zones_id (int):
            description_id (int):
            name (str): max length 12 characters
            icons_id (int):
     """

    zones_id: int
    description_id: int
    name: str
    icons_id: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        zones_id = self.zones_id

        description_id = self.description_id

        name = self.name

        icons_id = self.icons_id


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "zones_id": zones_id,
            "description_id": description_id,
            "name": name,
            "icons_id": icons_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        zones_id = d.pop("zones_id")

        description_id = d.pop("description_id")

        name = d.pop("name")

        icons_id = d.pop("icons_id")

        change_zone_nameicon_body = cls(
            zones_id=zones_id,
            description_id=description_id,
            name=name,
            icons_id=icons_id,
        )

        change_zone_nameicon_body.additional_properties = d
        return change_zone_nameicon_body

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

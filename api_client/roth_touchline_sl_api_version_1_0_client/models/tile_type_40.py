from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="TileType40")


@_attrs_define
class TileType40:
    """ 
        Attributes:
            description (Union[Unset, str]): Text information
            txt_id (Union[Unset, int]):  Example: 12.
            icon_id (Union[Unset, int]):  Example: 4.
            status_id (Union[Unset, int]):  Example: 1.
            header_id (Union[Unset, int]):  Example: 5.
            options (Union[Unset, int]):  Example: [3..-1].
     """

    description: Union[Unset, str] = UNSET
    txt_id: Union[Unset, int] = UNSET
    icon_id: Union[Unset, int] = UNSET
    status_id: Union[Unset, int] = UNSET
    header_id: Union[Unset, int] = UNSET
    options: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        txt_id = self.txt_id

        icon_id = self.icon_id

        status_id = self.status_id

        header_id = self.header_id

        options = self.options


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if txt_id is not UNSET:
            field_dict["txtId"] = txt_id
        if icon_id is not UNSET:
            field_dict["iconId"] = icon_id
        if status_id is not UNSET:
            field_dict["statusId"] = status_id
        if header_id is not UNSET:
            field_dict["headerId"] = header_id
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        txt_id = d.pop("txtId", UNSET)

        icon_id = d.pop("iconId", UNSET)

        status_id = d.pop("statusId", UNSET)

        header_id = d.pop("headerId", UNSET)

        options = d.pop("options", UNSET)

        tile_type_40 = cls(
            description=description,
            txt_id=txt_id,
            icon_id=icon_id,
            status_id=status_id,
            header_id=header_id,
            options=options,
        )

        tile_type_40.additional_properties = d
        return tile_type_40

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

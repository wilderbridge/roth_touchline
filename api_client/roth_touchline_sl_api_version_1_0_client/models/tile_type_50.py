from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="TileType50")


@_attrs_define
class TileType50:
    """ 
        Attributes:
            description (Union[Unset, str]): Controller software version
            txt_id (Union[Unset, int]):  Example: 12.
            icon_id (Union[Unset, int]):  Example: 4.
            version (Union[Unset, str]):  Example: 1.0.2.
            company_id (Union[Unset, int]):  Example: 5.
            controller_name (Union[Unset, str]):  Example: L-12.
            main_controller_id (Union[Unset, str]):  Example: a5ff.
     """

    description: Union[Unset, str] = UNSET
    txt_id: Union[Unset, int] = UNSET
    icon_id: Union[Unset, int] = UNSET
    version: Union[Unset, str] = UNSET
    company_id: Union[Unset, int] = UNSET
    controller_name: Union[Unset, str] = UNSET
    main_controller_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        txt_id = self.txt_id

        icon_id = self.icon_id

        version = self.version

        company_id = self.company_id

        controller_name = self.controller_name

        main_controller_id = self.main_controller_id


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
        if version is not UNSET:
            field_dict["version"] = version
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if controller_name is not UNSET:
            field_dict["controllerName"] = controller_name
        if main_controller_id is not UNSET:
            field_dict["mainControllerId"] = main_controller_id

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        txt_id = d.pop("txtId", UNSET)

        icon_id = d.pop("iconId", UNSET)

        version = d.pop("version", UNSET)

        company_id = d.pop("companyId", UNSET)

        controller_name = d.pop("controllerName", UNSET)

        main_controller_id = d.pop("mainControllerId", UNSET)

        tile_type_50 = cls(
            description=description,
            txt_id=txt_id,
            icon_id=icon_id,
            version=version,
            company_id=company_id,
            controller_name=controller_name,
            main_controller_id=main_controller_id,
        )

        tile_type_50.additional_properties = d
        return tile_type_50

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

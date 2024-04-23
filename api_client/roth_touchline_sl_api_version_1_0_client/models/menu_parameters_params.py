from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="MenuParametersParams")


@_attrs_define
class MenuParametersParams:
    """ 
        Attributes:
            format_ (Union[Unset, int]):
            value (Union[Unset, int]):
            min_ (Union[Unset, int]):
            max_ (Union[Unset, int]):
            default (Union[Unset, int]):
            txt_id (Union[Unset, int]):
            description (Union[Unset, str]):
     """

    format_: Union[Unset, int] = UNSET
    value: Union[Unset, int] = UNSET
    min_: Union[Unset, int] = UNSET
    max_: Union[Unset, int] = UNSET
    default: Union[Unset, int] = UNSET
    txt_id: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        format_ = self.format_

        value = self.value

        min_ = self.min_

        max_ = self.max_

        default = self.default

        txt_id = self.txt_id

        description = self.description


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if format_ is not UNSET:
            field_dict["format"] = format_
        if value is not UNSET:
            field_dict["value"] = value
        if min_ is not UNSET:
            field_dict["min"] = min_
        if max_ is not UNSET:
            field_dict["max"] = max_
        if default is not UNSET:
            field_dict["default"] = default
        if txt_id is not UNSET:
            field_dict["txtId"] = txt_id
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        format_ = d.pop("format", UNSET)

        value = d.pop("value", UNSET)

        min_ = d.pop("min", UNSET)

        max_ = d.pop("max", UNSET)

        default = d.pop("default", UNSET)

        txt_id = d.pop("txtId", UNSET)

        description = d.pop("description", UNSET)

        menu_parameters_params = cls(
            format_=format_,
            value=value,
            min_=min_,
            max_=max_,
            default=default,
            txt_id=txt_id,
            description=description,
        )

        menu_parameters_params.additional_properties = d
        return menu_parameters_params

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

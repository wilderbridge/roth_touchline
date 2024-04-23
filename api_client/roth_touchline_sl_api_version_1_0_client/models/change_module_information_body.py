from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="ChangeModuleInformationBody")


@_attrs_define
class ChangeModuleInformationBody:
    """ 
        Attributes:
            module_name (Union[Unset, str]):
            phone_number (Union[Unset, str]):
            additional_information (Union[Unset, str]):
     """

    module_name: Union[Unset, str] = UNSET
    phone_number: Union[Unset, str] = UNSET
    additional_information: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        module_name = self.module_name

        phone_number = self.phone_number

        additional_information = self.additional_information


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if module_name is not UNSET:
            field_dict["module_name"] = module_name
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if additional_information is not UNSET:
            field_dict["additional_information"] = additional_information

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        module_name = d.pop("module_name", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        additional_information = d.pop("additional_information", UNSET)

        change_module_information_body = cls(
            module_name=module_name,
            phone_number=phone_number,
            additional_information=additional_information,
        )

        change_module_information_body.additional_properties = d
        return change_module_information_body

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

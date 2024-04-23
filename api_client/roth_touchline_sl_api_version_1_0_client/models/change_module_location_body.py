from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="ChangeModuleLocationBody")


@_attrs_define
class ChangeModuleLocationBody:
    """ 
        Attributes:
            post_policy_accepted (bool):
            zip_code (Union[Unset, str]):
            country_name (Union[Unset, str]):
     """

    post_policy_accepted: bool
    zip_code: Union[Unset, str] = UNSET
    country_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        post_policy_accepted = self.post_policy_accepted

        zip_code = self.zip_code

        country_name = self.country_name


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "post_policy_accepted": post_policy_accepted,
        })
        if zip_code is not UNSET:
            field_dict["zip_code"] = zip_code
        if country_name is not UNSET:
            field_dict["country_name"] = country_name

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        post_policy_accepted = d.pop("post_policy_accepted")

        zip_code = d.pop("zip_code", UNSET)

        country_name = d.pop("country_name", UNSET)

        change_module_location_body = cls(
            post_policy_accepted=post_policy_accepted,
            zip_code=zip_code,
            country_name=country_name,
        )

        change_module_location_body.additional_properties = d
        return change_module_location_body

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

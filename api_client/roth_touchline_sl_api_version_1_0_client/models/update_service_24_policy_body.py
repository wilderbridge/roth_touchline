from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="UpdateService24PolicyBody")


@_attrs_define
class UpdateService24PolicyBody:
    """ 
        Attributes:
            accept_service_24_policy (Union[Unset, bool]):
     """

    accept_service_24_policy: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        accept_service_24_policy = self.accept_service_24_policy


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if accept_service_24_policy is not UNSET:
            field_dict["acceptService24Policy"] = accept_service_24_policy

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        accept_service_24_policy = d.pop("acceptService24Policy", UNSET)

        update_service_24_policy_body = cls(
            accept_service_24_policy=accept_service_24_policy,
        )

        update_service_24_policy_body.additional_properties = d
        return update_service_24_policy_body

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

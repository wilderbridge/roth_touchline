from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.service_24_policy_response_status import Service24PolicyResponseStatus






T = TypeVar("T", bound="Service24PolicyResponse")


@_attrs_define
class Service24PolicyResponse:
    """ 
        Attributes:
            status (Service24PolicyResponseStatus):
            policy (bool):
     """

    status: Service24PolicyResponseStatus
    policy: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        policy = self.policy


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "status": status,
            "policy": policy,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = Service24PolicyResponseStatus(d.pop("status"))




        policy = d.pop("policy")

        service_24_policy_response = cls(
            status=status,
            policy=policy,
        )

        service_24_policy_response.additional_properties = d
        return service_24_policy_response

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

from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="RegisterPushNotificationDeviceBody")


@_attrs_define
class RegisterPushNotificationDeviceBody:
    """ 
        Attributes:
            device_token (Union[Unset, str]):  Example: 12312312312a.
            device_name (Union[Unset, str]):  Example: ExampleName.
            distribution (Union[Unset, str]):  Example: ExampleDistribution.
            platform (Union[Unset, str]):
     """

    device_token: Union[Unset, str] = UNSET
    device_name: Union[Unset, str] = UNSET
    distribution: Union[Unset, str] = UNSET
    platform: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        device_token = self.device_token

        device_name = self.device_name

        distribution = self.distribution

        platform = self.platform


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if device_token is not UNSET:
            field_dict["device_token"] = device_token
        if device_name is not UNSET:
            field_dict["device_name"] = device_name
        if distribution is not UNSET:
            field_dict["distribution"] = distribution
        if platform is not UNSET:
            field_dict["platform"] = platform

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        device_token = d.pop("device_token", UNSET)

        device_name = d.pop("device_name", UNSET)

        distribution = d.pop("distribution", UNSET)

        platform = d.pop("platform", UNSET)

        register_push_notification_device_body = cls(
            device_token=device_token,
            device_name=device_name,
            distribution=distribution,
            platform=platform,
        )

        register_push_notification_device_body.additional_properties = d
        return register_push_notification_device_body

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

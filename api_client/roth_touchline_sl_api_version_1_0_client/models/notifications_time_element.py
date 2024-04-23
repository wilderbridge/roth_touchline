from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from ..models.notifications_time_element_notification_type import NotificationsTimeElementNotificationType
from typing import Union






T = TypeVar("T", bound="NotificationsTimeElement")


@_attrs_define
class NotificationsTimeElement:
    """ 
        Attributes:
            id (Union[Unset, int]):
            enable (Union[Unset, bool]):  Example: True.
            notification_type (Union[Unset, NotificationsTimeElementNotificationType]):  Example: error.
            start (Union[Unset, str]):  Example: 07:00.
            end (Union[Unset, str]):  Example: 22:00.
     """

    id: Union[Unset, int] = UNSET
    enable: Union[Unset, bool] = UNSET
    notification_type: Union[Unset, NotificationsTimeElementNotificationType] = UNSET
    start: Union[Unset, str] = UNSET
    end: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        enable = self.enable

        notification_type: Union[Unset, str] = UNSET
        if not isinstance(self.notification_type, Unset):
            notification_type = self.notification_type.value


        start = self.start

        end = self.end


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if enable is not UNSET:
            field_dict["enable"] = enable
        if notification_type is not UNSET:
            field_dict["notification_type"] = notification_type
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        enable = d.pop("enable", UNSET)

        _notification_type = d.pop("notification_type", UNSET)
        notification_type: Union[Unset, NotificationsTimeElementNotificationType]
        if isinstance(_notification_type,  Unset):
            notification_type = UNSET
        else:
            notification_type = NotificationsTimeElementNotificationType(_notification_type)




        start = d.pop("start", UNSET)

        end = d.pop("end", UNSET)

        notifications_time_element = cls(
            id=id,
            enable=enable,
            notification_type=notification_type,
            start=start,
            end=end,
        )

        notifications_time_element.additional_properties = d
        return notifications_time_element

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

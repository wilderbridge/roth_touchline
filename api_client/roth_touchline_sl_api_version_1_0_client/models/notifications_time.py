from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="NotificationsTime")


@_attrs_define
class NotificationsTime:
    """ 
        Attributes:
            id (Union[Unset, int]):  Example: 1.
            from_ (Union[Unset, str]):  Example: 07:00.
            to (Union[Unset, str]):  Example: 22:00.
            error (Union[Unset, bool]):  Example: True.
            warning (Union[Unset, bool]):
            info (Union[Unset, bool]):
            enable (Union[Unset, bool]):
     """

    id: Union[Unset, int] = UNSET
    from_: Union[Unset, str] = UNSET
    to: Union[Unset, str] = UNSET
    error: Union[Unset, bool] = UNSET
    warning: Union[Unset, bool] = UNSET
    info: Union[Unset, bool] = UNSET
    enable: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        from_ = self.from_

        to = self.to

        error = self.error

        warning = self.warning

        info = self.info

        enable = self.enable


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if error is not UNSET:
            field_dict["error"] = error
        if warning is not UNSET:
            field_dict["warning"] = warning
        if info is not UNSET:
            field_dict["info"] = info
        if enable is not UNSET:
            field_dict["enable"] = enable

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        error = d.pop("error", UNSET)

        warning = d.pop("warning", UNSET)

        info = d.pop("info", UNSET)

        enable = d.pop("enable", UNSET)

        notifications_time = cls(
            id=id,
            from_=from_,
            to=to,
            error=error,
            warning=warning,
            info=info,
            enable=enable,
        )

        notifications_time.additional_properties = d
        return notifications_time

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

from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="GetUsersUserIdModulesModuleUdidNotificationsTimeResponse200Item")


@_attrs_define
class GetUsersUserIdModulesModuleUdidNotificationsTimeResponse200Item:
    """ 
        Example:
            [{'idx': '100', 'from': '07:00:00', 'to': '22:00:00', 'error': True, 'warning': False, 'info': False, 'enable':
                True}]

        Attributes:
            idx (Union[Unset, str]):
            from_ (Union[Unset, str]):
            to (Union[Unset, str]):
            error (Union[Unset, bool]):
            warning (Union[Unset, bool]):
            info (Union[Unset, bool]):
            enable (Union[Unset, bool]):
     """

    idx: Union[Unset, str] = UNSET
    from_: Union[Unset, str] = UNSET
    to: Union[Unset, str] = UNSET
    error: Union[Unset, bool] = UNSET
    warning: Union[Unset, bool] = UNSET
    info: Union[Unset, bool] = UNSET
    enable: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        idx = self.idx

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
        if idx is not UNSET:
            field_dict["idx"] = idx
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
        idx = d.pop("idx", UNSET)

        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        error = d.pop("error", UNSET)

        warning = d.pop("warning", UNSET)

        info = d.pop("info", UNSET)

        enable = d.pop("enable", UNSET)

        get_users_user_id_modules_module_udid_notifications_time_response_200_item = cls(
            idx=idx,
            from_=from_,
            to=to,
            error=error,
            warning=warning,
            info=info,
            enable=enable,
        )

        get_users_user_id_modules_module_udid_notifications_time_response_200_item.additional_properties = d
        return get_users_user_id_modules_module_udid_notifications_time_response_200_item

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

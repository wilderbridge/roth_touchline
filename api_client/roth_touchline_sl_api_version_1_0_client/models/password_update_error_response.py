from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="PasswordUpdateErrorResponse")


@_attrs_define
class PasswordUpdateErrorResponse:
    """ 
        Attributes:
            code (Union[Unset, int]): Error code for password update operation Example: -1.
            status (Union[Unset, str]): Status of the password update operation Example: failed.
            message (Union[Unset, str]): Error message for password update operation Example: Incorrect current password..
     """

    code: Union[Unset, int] = UNSET
    status: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        code = self.code

        status = self.status

        message = self.message


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if code is not UNSET:
            field_dict["code"] = code
        if status is not UNSET:
            field_dict["status"] = status
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("code", UNSET)

        status = d.pop("status", UNSET)

        message = d.pop("message", UNSET)

        password_update_error_response = cls(
            code=code,
            status=status,
            message=message,
        )

        password_update_error_response.additional_properties = d
        return password_update_error_response

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

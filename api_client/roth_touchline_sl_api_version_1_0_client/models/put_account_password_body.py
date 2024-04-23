from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="PutAccountPasswordBody")


@_attrs_define
class PutAccountPasswordBody:
    """ 
        Attributes:
            new_password (Union[Unset, str]):
            reset_password_id (Union[Unset, str]):
     """

    new_password: Union[Unset, str] = UNSET
    reset_password_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        new_password = self.new_password

        reset_password_id = self.reset_password_id


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if new_password is not UNSET:
            field_dict["new_password"] = new_password
        if reset_password_id is not UNSET:
            field_dict["reset_password_id"] = reset_password_id

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        new_password = d.pop("new_password", UNSET)

        reset_password_id = d.pop("reset_password_id", UNSET)

        put_account_password_body = cls(
            new_password=new_password,
            reset_password_id=reset_password_id,
        )

        put_account_password_body.additional_properties = d
        return put_account_password_body

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

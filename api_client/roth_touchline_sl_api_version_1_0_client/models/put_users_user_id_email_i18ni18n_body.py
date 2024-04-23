from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="PutUsersUserIdEmailI18NI18NBody")


@_attrs_define
class PutUsersUserIdEmailI18NI18NBody:
    """ 
        Attributes:
            new_email (Union[Unset, str]):
     """

    new_email: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        new_email = self.new_email


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if new_email is not UNSET:
            field_dict["newEmail"] = new_email

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        new_email = d.pop("newEmail", UNSET)

        put_users_user_id_email_i18ni18n_body = cls(
            new_email=new_email,
        )

        put_users_user_id_email_i18ni18n_body.additional_properties = d
        return put_users_user_id_email_i18ni18n_body

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

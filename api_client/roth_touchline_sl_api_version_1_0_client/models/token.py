from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="Token")


@_attrs_define
class Token:
    """ 
        Attributes:
            authenticated (Union[Unset, str]):  Example: True.
            user_id (Union[Unset, int]):  Example: 240471648.
            access_google_home (Union[Unset, str]):
            token (Union[Unset, str]):  Example: eyJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InRlc3QiLCJ1c2VyX2lkIjoyNDA0NzE2NDgsIm
                lhdCI6MTUyNjk5ODQxOX0.opQW1yTczP7vuiIkI1Skuy8yJ8eGhYrlYUKmll9P88M".
     """

    authenticated: Union[Unset, str] = UNSET
    user_id: Union[Unset, int] = UNSET
    access_google_home: Union[Unset, str] = UNSET
    token: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        authenticated = self.authenticated

        user_id = self.user_id

        access_google_home = self.access_google_home

        token = self.token


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if authenticated is not UNSET:
            field_dict["authenticated"] = authenticated
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if access_google_home is not UNSET:
            field_dict["access_google_home"] = access_google_home
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        authenticated = d.pop("authenticated", UNSET)

        user_id = d.pop("user_id", UNSET)

        access_google_home = d.pop("access_google_home", UNSET)

        token = d.pop("token", UNSET)

        token = cls(
            authenticated=authenticated,
            user_id=user_id,
            access_google_home=access_google_home,
            token=token,
        )

        token.additional_properties = d
        return token

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

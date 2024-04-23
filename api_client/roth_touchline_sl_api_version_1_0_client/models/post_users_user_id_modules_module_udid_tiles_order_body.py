from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.post_users_user_id_modules_module_udid_tiles_order_body_type import PostUsersUserIdModulesModuleUdidTilesOrderBodyType
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="PostUsersUserIdModulesModuleUdidTilesOrderBody")


@_attrs_define
class PostUsersUserIdModulesModuleUdidTilesOrderBody:
    """ 
        Attributes:
            index (Union[Unset, int]):
            order (Union[Unset, str]):
            type (Union[Unset, PostUsersUserIdModulesModuleUdidTilesOrderBodyType]):
     """

    index: Union[Unset, int] = UNSET
    order: Union[Unset, str] = UNSET
    type: Union[Unset, PostUsersUserIdModulesModuleUdidTilesOrderBodyType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        index = self.index

        order = self.order

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value



        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if index is not UNSET:
            field_dict["index"] = index
        if order is not UNSET:
            field_dict["order"] = order
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        index = d.pop("index", UNSET)

        order = d.pop("order", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, PostUsersUserIdModulesModuleUdidTilesOrderBodyType]
        if isinstance(_type,  Unset):
            type = UNSET
        else:
            type = PostUsersUserIdModulesModuleUdidTilesOrderBodyType(_type)




        post_users_user_id_modules_module_udid_tiles_order_body = cls(
            index=index,
            order=order,
            type=type,
        )

        post_users_user_id_modules_module_udid_tiles_order_body.additional_properties = d
        return post_users_user_id_modules_module_udid_tiles_order_body

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

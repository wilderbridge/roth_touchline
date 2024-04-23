from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from ..types import UNSET, Unset
from typing import Dict
from typing import Union

if TYPE_CHECKING:
  from ..models.zone_params import ZoneParams





T = TypeVar("T", bound="Zone")


@_attrs_define
class Zone:
    """ 
        Attributes:
            id (Union[Unset, int]):
            parent_id (Union[Unset, int]):
            type (Union[Unset, int]):
            menu_id (Union[Unset, int]):
            order_id (Union[Unset, int]):
            visibility (Union[Unset, bool]):
            params (Union[Unset, ZoneParams]):
     """

    id: Union[Unset, int] = UNSET
    parent_id: Union[Unset, int] = UNSET
    type: Union[Unset, int] = UNSET
    menu_id: Union[Unset, int] = UNSET
    order_id: Union[Unset, int] = UNSET
    visibility: Union[Unset, bool] = UNSET
    params: Union[Unset, 'ZoneParams'] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.zone_params import ZoneParams
        id = self.id

        parent_id = self.parent_id

        type = self.type

        menu_id = self.menu_id

        order_id = self.order_id

        visibility = self.visibility

        params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if type is not UNSET:
            field_dict["type"] = type
        if menu_id is not UNSET:
            field_dict["menuId"] = menu_id
        if order_id is not UNSET:
            field_dict["orderId"] = order_id
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.zone_params import ZoneParams
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        parent_id = d.pop("parentId", UNSET)

        type = d.pop("type", UNSET)

        menu_id = d.pop("menuId", UNSET)

        order_id = d.pop("orderId", UNSET)

        visibility = d.pop("visibility", UNSET)

        _params = d.pop("params", UNSET)
        params: Union[Unset, ZoneParams]
        if isinstance(_params,  Unset):
            params = UNSET
        else:
            params = ZoneParams.from_dict(_params)




        zone = cls(
            id=id,
            parent_id=parent_id,
            type=type,
            menu_id=menu_id,
            order_id=order_id,
            visibility=visibility,
            params=params,
        )

        zone.additional_properties = d
        return zone

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

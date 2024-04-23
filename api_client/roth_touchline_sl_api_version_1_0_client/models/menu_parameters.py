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
  from ..models.menu_parameters_params import MenuParametersParams





T = TypeVar("T", bound="MenuParameters")


@_attrs_define
class MenuParameters:
    """ 
        Attributes:
            menu_type (Union[Unset, str]):  Example: MU.
            type (Union[Unset, int]):
            id (Union[Unset, int]):
            parent_id (Union[Unset, int]):
            access (Union[Unset, bool]):
            txt_id (Union[Unset, int]):
            wiki_tx_id (Union[Unset, int]):
            icon_id (Union[Unset, int]):
            params (Union[Unset, MenuParametersParams]):
     """

    menu_type: Union[Unset, str] = UNSET
    type: Union[Unset, int] = UNSET
    id: Union[Unset, int] = UNSET
    parent_id: Union[Unset, int] = UNSET
    access: Union[Unset, bool] = UNSET
    txt_id: Union[Unset, int] = UNSET
    wiki_tx_id: Union[Unset, int] = UNSET
    icon_id: Union[Unset, int] = UNSET
    params: Union[Unset, 'MenuParametersParams'] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.menu_parameters_params import MenuParametersParams
        menu_type = self.menu_type

        type = self.type

        id = self.id

        parent_id = self.parent_id

        access = self.access

        txt_id = self.txt_id

        wiki_tx_id = self.wiki_tx_id

        icon_id = self.icon_id

        params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if menu_type is not UNSET:
            field_dict["menuType"] = menu_type
        if type is not UNSET:
            field_dict["type"] = type
        if id is not UNSET:
            field_dict["id"] = id
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if access is not UNSET:
            field_dict["access"] = access
        if txt_id is not UNSET:
            field_dict["txtId"] = txt_id
        if wiki_tx_id is not UNSET:
            field_dict["wikiTxId"] = wiki_tx_id
        if icon_id is not UNSET:
            field_dict["iconId"] = icon_id
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.menu_parameters_params import MenuParametersParams
        d = src_dict.copy()
        menu_type = d.pop("menuType", UNSET)

        type = d.pop("type", UNSET)

        id = d.pop("id", UNSET)

        parent_id = d.pop("parentId", UNSET)

        access = d.pop("access", UNSET)

        txt_id = d.pop("txtId", UNSET)

        wiki_tx_id = d.pop("wikiTxId", UNSET)

        icon_id = d.pop("iconId", UNSET)

        _params = d.pop("params", UNSET)
        params: Union[Unset, MenuParametersParams]
        if isinstance(_params,  Unset):
            params = UNSET
        else:
            params = MenuParametersParams.from_dict(_params)




        menu_parameters = cls(
            menu_type=menu_type,
            type=type,
            id=id,
            parent_id=parent_id,
            access=access,
            txt_id=txt_id,
            wiki_tx_id=wiki_tx_id,
            icon_id=icon_id,
            params=params,
        )

        menu_parameters.additional_properties = d
        return menu_parameters

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

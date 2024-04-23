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
  from ..models.manufacturer_parent_details_success_response_params import ManufacturerParentDetailsSuccessResponseParams





T = TypeVar("T", bound="ManufacturerParentDetailsSuccessResponse")


@_attrs_define
class ManufacturerParentDetailsSuccessResponse:
    """ 
        Attributes:
            id (Union[Unset, int]):  Example: 123.
            parent_id (Union[Unset, int]):  Example: 456.
            type (Union[Unset, int]):  Example: 789.
            index (Union[Unset, int]):  Example: 1.
            params (Union[Unset, ManufacturerParentDetailsSuccessResponseParams]):
     """

    id: Union[Unset, int] = UNSET
    parent_id: Union[Unset, int] = UNSET
    type: Union[Unset, int] = UNSET
    index: Union[Unset, int] = UNSET
    params: Union[Unset, 'ManufacturerParentDetailsSuccessResponseParams'] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.manufacturer_parent_details_success_response_params import ManufacturerParentDetailsSuccessResponseParams
        id = self.id

        parent_id = self.parent_id

        type = self.type

        index = self.index

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
        if index is not UNSET:
            field_dict["index"] = index
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.manufacturer_parent_details_success_response_params import ManufacturerParentDetailsSuccessResponseParams
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        parent_id = d.pop("parentId", UNSET)

        type = d.pop("type", UNSET)

        index = d.pop("index", UNSET)

        _params = d.pop("params", UNSET)
        params: Union[Unset, ManufacturerParentDetailsSuccessResponseParams]
        if isinstance(_params,  Unset):
            params = UNSET
        else:
            params = ManufacturerParentDetailsSuccessResponseParams.from_dict(_params)




        manufacturer_parent_details_success_response = cls(
            id=id,
            parent_id=parent_id,
            type=type,
            index=index,
            params=params,
        )

        manufacturer_parent_details_success_response.additional_properties = d
        return manufacturer_parent_details_success_response

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

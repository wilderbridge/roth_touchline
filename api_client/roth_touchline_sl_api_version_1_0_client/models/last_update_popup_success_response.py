from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, List
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="LastUpdatePopupSuccessResponse")


@_attrs_define
class LastUpdatePopupSuccessResponse:
    """ 
        Attributes:
            elements (Union[Unset, List[Any]]):
            last_update (Union[Unset, str]):  Example: 2024-03-21 12:08:52 +0100.
     """

    elements: Union[Unset, List[Any]] = UNSET
    last_update: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        elements: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.elements, Unset):
            elements = self.elements





        last_update = self.last_update


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if elements is not UNSET:
            field_dict["elements"] = elements
        if last_update is not UNSET:
            field_dict["lastUpdate"] = last_update

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        elements = cast(List[Any], d.pop("elements", UNSET))


        last_update = d.pop("lastUpdate", UNSET)

        last_update_popup_success_response = cls(
            elements=elements,
            last_update=last_update,
        )

        last_update_popup_success_response.additional_properties = d
        return last_update_popup_success_response

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

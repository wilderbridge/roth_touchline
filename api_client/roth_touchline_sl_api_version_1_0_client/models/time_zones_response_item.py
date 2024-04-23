from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="TimeZonesResponseItem")


@_attrs_define
class TimeZonesResponseItem:
    """ 
        Attributes:
            id (Union[Unset, int]):
            gmt (Union[Unset, str]):  Example: -660.
            en (Union[Unset, str]):  Example: Midway Island, Samoa.
            pl (Union[Unset, str]):  Example: Midway Island, Samoa.
            ru (Union[Unset, str]):  Example: Остров Мидуэй, Самоа.
     """

    id: Union[Unset, int] = UNSET
    gmt: Union[Unset, str] = UNSET
    en: Union[Unset, str] = UNSET
    pl: Union[Unset, str] = UNSET
    ru: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        gmt = self.gmt

        en = self.en

        pl = self.pl

        ru = self.ru


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if gmt is not UNSET:
            field_dict["gmt"] = gmt
        if en is not UNSET:
            field_dict["en"] = en
        if pl is not UNSET:
            field_dict["pl"] = pl
        if ru is not UNSET:
            field_dict["ru"] = ru

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        gmt = d.pop("gmt", UNSET)

        en = d.pop("en", UNSET)

        pl = d.pop("pl", UNSET)

        ru = d.pop("ru", UNSET)

        time_zones_response_item = cls(
            id=id,
            gmt=gmt,
            en=en,
            pl=pl,
            ru=ru,
        )

        time_zones_response_item.additional_properties = d
        return time_zones_response_item

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

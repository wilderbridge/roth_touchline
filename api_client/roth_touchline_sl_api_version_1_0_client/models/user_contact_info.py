from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="UserContactInfo")


@_attrs_define
class UserContactInfo:
    """ 
        Attributes:
            city (Union[Unset, str]):  Example: Katowice.
            street (Union[Unset, str]):  Example: Szkolna.
            house_number (Union[Unset, str]):  Example: 20.
            installer_information (Union[Unset, str]):  Example: Information for the installer.
     """

    city: Union[Unset, str] = UNSET
    street: Union[Unset, str] = UNSET
    house_number: Union[Unset, str] = UNSET
    installer_information: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        city = self.city

        street = self.street

        house_number = self.house_number

        installer_information = self.installer_information


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if city is not UNSET:
            field_dict["city"] = city
        if street is not UNSET:
            field_dict["street"] = street
        if house_number is not UNSET:
            field_dict["houseNumber"] = house_number
        if installer_information is not UNSET:
            field_dict["installerInformation"] = installer_information

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        city = d.pop("city", UNSET)

        street = d.pop("street", UNSET)

        house_number = d.pop("houseNumber", UNSET)

        installer_information = d.pop("installerInformation", UNSET)

        user_contact_info = cls(
            city=city,
            street=street,
            house_number=house_number,
            installer_information=installer_information,
        )

        user_contact_info.additional_properties = d
        return user_contact_info

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

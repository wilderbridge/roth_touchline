from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="TileType252")


@_attrs_define
class TileType252:
    """ 
        Attributes:
            description (Union[Unset, str]): OpenTherm
            current_temp (Union[Unset, int]):  Example: 23.
            set_current_temp (Union[Unset, int]):  Example: 22.
            current_temp_dhw (Union[Unset, int]):  Example: 20.
            set_temp_dhw (Union[Unset, int]):  Example: 20.
            modulation_percentage (Union[Unset, int]):  Example: 20.
            flags (Union[Unset, str]):  Example:  00000001 - No connection | 00000010 - Heating curve | 00000100 - Active |
                CO00001000 - Active CWU.
     """

    description: Union[Unset, str] = UNSET
    current_temp: Union[Unset, int] = UNSET
    set_current_temp: Union[Unset, int] = UNSET
    current_temp_dhw: Union[Unset, int] = UNSET
    set_temp_dhw: Union[Unset, int] = UNSET
    modulation_percentage: Union[Unset, int] = UNSET
    flags: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        current_temp = self.current_temp

        set_current_temp = self.set_current_temp

        current_temp_dhw = self.current_temp_dhw

        set_temp_dhw = self.set_temp_dhw

        modulation_percentage = self.modulation_percentage

        flags = self.flags


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if current_temp is not UNSET:
            field_dict["currentTemp"] = current_temp
        if set_current_temp is not UNSET:
            field_dict["setCurrentTemp"] = set_current_temp
        if current_temp_dhw is not UNSET:
            field_dict["currentTempDHW"] = current_temp_dhw
        if set_temp_dhw is not UNSET:
            field_dict["setTempDHW"] = set_temp_dhw
        if modulation_percentage is not UNSET:
            field_dict["modulationPercentage"] = modulation_percentage
        if flags is not UNSET:
            field_dict["flags"] = flags

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        current_temp = d.pop("currentTemp", UNSET)

        set_current_temp = d.pop("setCurrentTemp", UNSET)

        current_temp_dhw = d.pop("currentTempDHW", UNSET)

        set_temp_dhw = d.pop("setTempDHW", UNSET)

        modulation_percentage = d.pop("modulationPercentage", UNSET)

        flags = d.pop("flags", UNSET)

        tile_type_252 = cls(
            description=description,
            current_temp=current_temp,
            set_current_temp=set_current_temp,
            current_temp_dhw=current_temp_dhw,
            set_temp_dhw=set_temp_dhw,
            modulation_percentage=modulation_percentage,
            flags=flags,
        )

        tile_type_252.additional_properties = d
        return tile_type_252

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

from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="TileType23")


@_attrs_define
class TileType23:
    """ 
        Attributes:
            description (Union[Unset, str]): Built-in valve
            working_status (Union[Unset, bool]):  Example: 1.
            txt_id (Union[Unset, int]):  Example: 11.
            valve_number (Union[Unset, int]):  Example: 4.
            current_temp (Union[Unset, int]):  Example: 60.
            return_temp (Union[Unset, int]):  Example: 55.
            set_temp_correction (Union[Unset, int]):  Example: 5.
            opening_percentage (Union[Unset, int]):  Example: 30.
            valve_pump (Union[Unset, int]):  Example: 2.
            boiler_protection (Union[Unset, bool]):  Example: 1.
            return_protection (Union[Unset, int]):  Example: 1.
            set_temp (Union[Unset, int]):  Example: 50.
     """

    description: Union[Unset, str] = UNSET
    working_status: Union[Unset, bool] = UNSET
    txt_id: Union[Unset, int] = UNSET
    valve_number: Union[Unset, int] = UNSET
    current_temp: Union[Unset, int] = UNSET
    return_temp: Union[Unset, int] = UNSET
    set_temp_correction: Union[Unset, int] = UNSET
    opening_percentage: Union[Unset, int] = UNSET
    valve_pump: Union[Unset, int] = UNSET
    boiler_protection: Union[Unset, bool] = UNSET
    return_protection: Union[Unset, int] = UNSET
    set_temp: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        working_status = self.working_status

        txt_id = self.txt_id

        valve_number = self.valve_number

        current_temp = self.current_temp

        return_temp = self.return_temp

        set_temp_correction = self.set_temp_correction

        opening_percentage = self.opening_percentage

        valve_pump = self.valve_pump

        boiler_protection = self.boiler_protection

        return_protection = self.return_protection

        set_temp = self.set_temp


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if working_status is not UNSET:
            field_dict["workingStatus"] = working_status
        if txt_id is not UNSET:
            field_dict["txtId"] = txt_id
        if valve_number is not UNSET:
            field_dict["valveNumber"] = valve_number
        if current_temp is not UNSET:
            field_dict["currentTemp"] = current_temp
        if return_temp is not UNSET:
            field_dict["returnTemp"] = return_temp
        if set_temp_correction is not UNSET:
            field_dict["setTempCorrection"] = set_temp_correction
        if opening_percentage is not UNSET:
            field_dict["openingPercentage"] = opening_percentage
        if valve_pump is not UNSET:
            field_dict["valvePump"] = valve_pump
        if boiler_protection is not UNSET:
            field_dict["boilerProtection"] = boiler_protection
        if return_protection is not UNSET:
            field_dict["returnProtection"] = return_protection
        if set_temp is not UNSET:
            field_dict["setTemp"] = set_temp

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        working_status = d.pop("workingStatus", UNSET)

        txt_id = d.pop("txtId", UNSET)

        valve_number = d.pop("valveNumber", UNSET)

        current_temp = d.pop("currentTemp", UNSET)

        return_temp = d.pop("returnTemp", UNSET)

        set_temp_correction = d.pop("setTempCorrection", UNSET)

        opening_percentage = d.pop("openingPercentage", UNSET)

        valve_pump = d.pop("valvePump", UNSET)

        boiler_protection = d.pop("boilerProtection", UNSET)

        return_protection = d.pop("returnProtection", UNSET)

        set_temp = d.pop("setTemp", UNSET)

        tile_type_23 = cls(
            description=description,
            working_status=working_status,
            txt_id=txt_id,
            valve_number=valve_number,
            current_temp=current_temp,
            return_temp=return_temp,
            set_temp_correction=set_temp_correction,
            opening_percentage=opening_percentage,
            valve_pump=valve_pump,
            boiler_protection=boiler_protection,
            return_protection=return_protection,
            set_temp=set_temp,
        )

        tile_type_23.additional_properties = d
        return tile_type_23

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

from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="TileType251")


@_attrs_define
class TileType251:
    """ 
        Attributes:
            description (Union[Unset, str]): DHW for zones controller
            zone_number (Union[Unset, int]):  Example: 2.
            current_temp_dhw (Union[Unset, int]):  Example: 22.
            is_active (Union[Unset, bool]):  Example: 1.
            mode (Union[Unset, str]):  Example: off parallel.
            current_temp_ch (Union[Unset, int]):  Example: 20.
            set_temp_dhw (Union[Unset, int]):  Example: 20.
            dhw_sensor_events (Union[Unset, int]):  Example: 20.
            heating_sensor_events (Union[Unset, int]):  Example: 20.
     """

    description: Union[Unset, str] = UNSET
    zone_number: Union[Unset, int] = UNSET
    current_temp_dhw: Union[Unset, int] = UNSET
    is_active: Union[Unset, bool] = UNSET
    mode: Union[Unset, str] = UNSET
    current_temp_ch: Union[Unset, int] = UNSET
    set_temp_dhw: Union[Unset, int] = UNSET
    dhw_sensor_events: Union[Unset, int] = UNSET
    heating_sensor_events: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        zone_number = self.zone_number

        current_temp_dhw = self.current_temp_dhw

        is_active = self.is_active

        mode = self.mode

        current_temp_ch = self.current_temp_ch

        set_temp_dhw = self.set_temp_dhw

        dhw_sensor_events = self.dhw_sensor_events

        heating_sensor_events = self.heating_sensor_events


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if zone_number is not UNSET:
            field_dict["zoneNumber"] = zone_number
        if current_temp_dhw is not UNSET:
            field_dict["currentTempDHW"] = current_temp_dhw
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if mode is not UNSET:
            field_dict["mode"] = mode
        if current_temp_ch is not UNSET:
            field_dict["currentTempCH"] = current_temp_ch
        if set_temp_dhw is not UNSET:
            field_dict["setTempDHW"] = set_temp_dhw
        if dhw_sensor_events is not UNSET:
            field_dict["dhwSensorEvents"] = dhw_sensor_events
        if heating_sensor_events is not UNSET:
            field_dict["heatingSensorEvents"] = heating_sensor_events

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        zone_number = d.pop("zoneNumber", UNSET)

        current_temp_dhw = d.pop("currentTempDHW", UNSET)

        is_active = d.pop("isActive", UNSET)

        mode = d.pop("mode", UNSET)

        current_temp_ch = d.pop("currentTempCH", UNSET)

        set_temp_dhw = d.pop("setTempDHW", UNSET)

        dhw_sensor_events = d.pop("dhwSensorEvents", UNSET)

        heating_sensor_events = d.pop("heatingSensorEvents", UNSET)

        tile_type_251 = cls(
            description=description,
            zone_number=zone_number,
            current_temp_dhw=current_temp_dhw,
            is_active=is_active,
            mode=mode,
            current_temp_ch=current_temp_ch,
            set_temp_dhw=set_temp_dhw,
            dhw_sensor_events=dhw_sensor_events,
            heating_sensor_events=heating_sensor_events,
        )

        tile_type_251.additional_properties = d
        return tile_type_251

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

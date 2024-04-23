from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from typing import cast, List
from typing import cast
from typing import Dict
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.tile_type_6_global_schedules_params import TileType6GlobalSchedulesParams
  from ..models.tile_type_6_global_schedules_elements_item import TileType6GlobalSchedulesElementsItem





T = TypeVar("T", bound="TileType6GlobalSchedules")


@_attrs_define
class TileType6GlobalSchedules:
    """ 
        Attributes:
            time (Union[Unset, str]):
            during_change (Union[Unset, str]):
            elements (Union[Unset, List['TileType6GlobalSchedulesElementsItem']]):
            params (Union[Unset, TileType6GlobalSchedulesParams]):
     """

    time: Union[Unset, str] = UNSET
    during_change: Union[Unset, str] = UNSET
    elements: Union[Unset, List['TileType6GlobalSchedulesElementsItem']] = UNSET
    params: Union[Unset, 'TileType6GlobalSchedulesParams'] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.tile_type_6_global_schedules_params import TileType6GlobalSchedulesParams
        from ..models.tile_type_6_global_schedules_elements_item import TileType6GlobalSchedulesElementsItem
        time = self.time

        during_change = self.during_change

        elements: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.elements, Unset):
            elements = []
            for elements_item_data in self.elements:
                elements_item = elements_item_data.to_dict()
                elements.append(elements_item)





        params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if time is not UNSET:
            field_dict["time"] = time
        if during_change is not UNSET:
            field_dict["duringChange"] = during_change
        if elements is not UNSET:
            field_dict["elements"] = elements
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tile_type_6_global_schedules_params import TileType6GlobalSchedulesParams
        from ..models.tile_type_6_global_schedules_elements_item import TileType6GlobalSchedulesElementsItem
        d = src_dict.copy()
        time = d.pop("time", UNSET)

        during_change = d.pop("duringChange", UNSET)

        elements = []
        _elements = d.pop("elements", UNSET)
        for elements_item_data in (_elements or []):
            elements_item = TileType6GlobalSchedulesElementsItem.from_dict(elements_item_data)



            elements.append(elements_item)


        _params = d.pop("params", UNSET)
        params: Union[Unset, TileType6GlobalSchedulesParams]
        if isinstance(_params,  Unset):
            params = UNSET
        else:
            params = TileType6GlobalSchedulesParams.from_dict(_params)




        tile_type_6_global_schedules = cls(
            time=time,
            during_change=during_change,
            elements=elements,
            params=params,
        )

        tile_type_6_global_schedules.additional_properties = d
        return tile_type_6_global_schedules

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

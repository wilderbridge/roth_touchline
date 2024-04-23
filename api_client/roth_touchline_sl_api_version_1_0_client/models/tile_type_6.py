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
  from ..models.tile_type_6_global_schedules import TileType6GlobalSchedules
  from ..models.tile_type_6_elements_item import TileType6ElementsItem





T = TypeVar("T", bound="TileType6")


@_attrs_define
class TileType6:
    """ 
        Attributes:
            transaction_time (Union[Unset, str]):
            elements (Union[Unset, List['TileType6ElementsItem']]):
            global_schedules (Union[Unset, TileType6GlobalSchedules]):
     """

    transaction_time: Union[Unset, str] = UNSET
    elements: Union[Unset, List['TileType6ElementsItem']] = UNSET
    global_schedules: Union[Unset, 'TileType6GlobalSchedules'] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.tile_type_6_global_schedules import TileType6GlobalSchedules
        from ..models.tile_type_6_elements_item import TileType6ElementsItem
        transaction_time = self.transaction_time

        elements: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.elements, Unset):
            elements = []
            for elements_item_data in self.elements:
                elements_item = elements_item_data.to_dict()
                elements.append(elements_item)





        global_schedules: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.global_schedules, Unset):
            global_schedules = self.global_schedules.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if transaction_time is not UNSET:
            field_dict["transaction_time"] = transaction_time
        if elements is not UNSET:
            field_dict["elements"] = elements
        if global_schedules is not UNSET:
            field_dict["globalSchedules"] = global_schedules

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tile_type_6_global_schedules import TileType6GlobalSchedules
        from ..models.tile_type_6_elements_item import TileType6ElementsItem
        d = src_dict.copy()
        transaction_time = d.pop("transaction_time", UNSET)

        elements = []
        _elements = d.pop("elements", UNSET)
        for elements_item_data in (_elements or []):
            elements_item = TileType6ElementsItem.from_dict(elements_item_data)



            elements.append(elements_item)


        _global_schedules = d.pop("globalSchedules", UNSET)
        global_schedules: Union[Unset, TileType6GlobalSchedules]
        if isinstance(_global_schedules,  Unset):
            global_schedules = UNSET
        else:
            global_schedules = TileType6GlobalSchedules.from_dict(_global_schedules)




        tile_type_6 = cls(
            transaction_time=transaction_time,
            elements=elements,
            global_schedules=global_schedules,
        )

        tile_type_6.additional_properties = d
        return tile_type_6

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

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
  from ..models.zone import Zone
  from ..models.tile_type_40 import TileType40





T = TypeVar("T", bound="ModuleData40")


@_attrs_define
class ModuleData40:
    """ 
        Attributes:
            zones (Union[Unset, Zone]):
            tiles (Union[Unset, List['TileType40']]):
     """

    zones: Union[Unset, 'Zone'] = UNSET
    tiles: Union[Unset, List['TileType40']] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.zone import Zone
        from ..models.tile_type_40 import TileType40
        zones: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.zones, Unset):
            zones = self.zones.to_dict()

        tiles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tiles, Unset):
            tiles = []
            for tiles_item_data in self.tiles:
                tiles_item = tiles_item_data.to_dict()
                tiles.append(tiles_item)






        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if zones is not UNSET:
            field_dict["zones"] = zones
        if tiles is not UNSET:
            field_dict["tiles"] = tiles

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.zone import Zone
        from ..models.tile_type_40 import TileType40
        d = src_dict.copy()
        _zones = d.pop("zones", UNSET)
        zones: Union[Unset, Zone]
        if isinstance(_zones,  Unset):
            zones = UNSET
        else:
            zones = Zone.from_dict(_zones)




        tiles = []
        _tiles = d.pop("tiles", UNSET)
        for tiles_item_data in (_tiles or []):
            tiles_item = TileType40.from_dict(tiles_item_data)



            tiles.append(tiles_item)


        module_data_40 = cls(
            zones=zones,
            tiles=tiles,
        )

        module_data_40.additional_properties = d
        return module_data_40

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

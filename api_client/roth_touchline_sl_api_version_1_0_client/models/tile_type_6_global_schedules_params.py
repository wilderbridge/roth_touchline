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
  from ..models.tile_type_6_global_schedules_params_options import TileType6GlobalSchedulesParamsOptions





T = TypeVar("T", bound="TileType6GlobalSchedulesParams")


@_attrs_define
class TileType6GlobalSchedulesParams:
    """ 
        Attributes:
            description (Union[Unset, str]):
            status_id (Union[Unset, int]):
            header_id (Union[Unset, int]):
            icon_id (Union[Unset, int]):
            options (Union[Unset, TileType6GlobalSchedulesParamsOptions]):
     """

    description: Union[Unset, str] = UNSET
    status_id: Union[Unset, int] = UNSET
    header_id: Union[Unset, int] = UNSET
    icon_id: Union[Unset, int] = UNSET
    options: Union[Unset, 'TileType6GlobalSchedulesParamsOptions'] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.tile_type_6_global_schedules_params_options import TileType6GlobalSchedulesParamsOptions
        description = self.description

        status_id = self.status_id

        header_id = self.header_id

        icon_id = self.icon_id

        options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if status_id is not UNSET:
            field_dict["statusId"] = status_id
        if header_id is not UNSET:
            field_dict["headerId"] = header_id
        if icon_id is not UNSET:
            field_dict["iconId"] = icon_id
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tile_type_6_global_schedules_params_options import TileType6GlobalSchedulesParamsOptions
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        status_id = d.pop("statusId", UNSET)

        header_id = d.pop("headerId", UNSET)

        icon_id = d.pop("iconId", UNSET)

        _options = d.pop("options", UNSET)
        options: Union[Unset, TileType6GlobalSchedulesParamsOptions]
        if isinstance(_options,  Unset):
            options = UNSET
        else:
            options = TileType6GlobalSchedulesParamsOptions.from_dict(_options)




        tile_type_6_global_schedules_params = cls(
            description=description,
            status_id=status_id,
            header_id=header_id,
            icon_id=icon_id,
            options=options,
        )

        tile_type_6_global_schedules_params.additional_properties = d
        return tile_type_6_global_schedules_params

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

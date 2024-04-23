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
  from ..models.statistics_data_data_item import StatisticsDataDataItem





T = TypeVar("T", bound="StatisticsData")


@_attrs_define
class StatisticsData:
    """ 
        Attributes:
            status (Union[Unset, bool]):
            data (Union[Unset, List['StatisticsDataDataItem']]):
            description (Union[Unset, str]):
     """

    status: Union[Unset, bool] = UNSET
    data: Union[Unset, List['StatisticsDataDataItem']] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.statistics_data_data_item import StatisticsDataDataItem
        status = self.status

        data: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)





        description = self.description


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if status is not UNSET:
            field_dict["status"] = status
        if data is not UNSET:
            field_dict["data"] = data
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.statistics_data_data_item import StatisticsDataDataItem
        d = src_dict.copy()
        status = d.pop("status", UNSET)

        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in (_data or []):
            data_item = StatisticsDataDataItem.from_dict(data_item_data)



            data.append(data_item)


        description = d.pop("description", UNSET)

        statistics_data = cls(
            status=status,
            data=data,
            description=description,
        )

        statistics_data.additional_properties = d
        return statistics_data

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

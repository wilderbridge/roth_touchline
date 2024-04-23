from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="Module")


@_attrs_define
class Module:
    """ 
        Attributes:
            name (Union[Unset, str]):  Example: I-3 DEMO.
            email (Union[Unset, str]):
            type (Union[Unset, str]):  Example: installation.
            controller_status (Union[Unset, str]):  Example: active.
            module_status (Union[Unset, str]):  Example: active.
            additional_information (Union[Unset, str]):
            phone_number (Union[Unset, str]):  Example: 123456.
            zip_code (Union[Unset, str]):  Example: 00-000.
            country (Union[Unset, str]):  Example: Polska.
            gmt_id (Union[Unset, int]):  Example: 30.
            gmt_time (Union[Unset, str]):  Example: 1.
            postcode_policy_accepted (Union[Unset, bool]):  Example: True.
            version (Union[Unset, str]):
            company (Union[Unset, str]):
            udid (Union[Unset, str]):  Example: dba00bb19dbaa4887196447e363be3e1.
     """

    name: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    controller_status: Union[Unset, str] = UNSET
    module_status: Union[Unset, str] = UNSET
    additional_information: Union[Unset, str] = UNSET
    phone_number: Union[Unset, str] = UNSET
    zip_code: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    gmt_id: Union[Unset, int] = UNSET
    gmt_time: Union[Unset, str] = UNSET
    postcode_policy_accepted: Union[Unset, bool] = UNSET
    version: Union[Unset, str] = UNSET
    company: Union[Unset, str] = UNSET
    udid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        email = self.email

        type = self.type

        controller_status = self.controller_status

        module_status = self.module_status

        additional_information = self.additional_information

        phone_number = self.phone_number

        zip_code = self.zip_code

        country = self.country

        gmt_id = self.gmt_id

        gmt_time = self.gmt_time

        postcode_policy_accepted = self.postcode_policy_accepted

        version = self.version

        company = self.company

        udid = self.udid


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if email is not UNSET:
            field_dict["email"] = email
        if type is not UNSET:
            field_dict["type"] = type
        if controller_status is not UNSET:
            field_dict["controllerStatus"] = controller_status
        if module_status is not UNSET:
            field_dict["moduleStatus"] = module_status
        if additional_information is not UNSET:
            field_dict["additionalInformation"] = additional_information
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if zip_code is not UNSET:
            field_dict["zipCode"] = zip_code
        if country is not UNSET:
            field_dict["country"] = country
        if gmt_id is not UNSET:
            field_dict["gmtId"] = gmt_id
        if gmt_time is not UNSET:
            field_dict["gmtTime"] = gmt_time
        if postcode_policy_accepted is not UNSET:
            field_dict["postcodePolicyAccepted"] = postcode_policy_accepted
        if version is not UNSET:
            field_dict["version"] = version
        if company is not UNSET:
            field_dict["company"] = company
        if udid is not UNSET:
            field_dict["udid"] = udid

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        email = d.pop("email", UNSET)

        type = d.pop("type", UNSET)

        controller_status = d.pop("controllerStatus", UNSET)

        module_status = d.pop("moduleStatus", UNSET)

        additional_information = d.pop("additionalInformation", UNSET)

        phone_number = d.pop("phoneNumber", UNSET)

        zip_code = d.pop("zipCode", UNSET)

        country = d.pop("country", UNSET)

        gmt_id = d.pop("gmtId", UNSET)

        gmt_time = d.pop("gmtTime", UNSET)

        postcode_policy_accepted = d.pop("postcodePolicyAccepted", UNSET)

        version = d.pop("version", UNSET)

        company = d.pop("company", UNSET)

        udid = d.pop("udid", UNSET)

        module = cls(
            name=name,
            email=email,
            type=type,
            controller_status=controller_status,
            module_status=module_status,
            additional_information=additional_information,
            phone_number=phone_number,
            zip_code=zip_code,
            country=country,
            gmt_id=gmt_id,
            gmt_time=gmt_time,
            postcode_policy_accepted=postcode_policy_accepted,
            version=version,
            company=company,
            udid=udid,
        )

        module.additional_properties = d
        return module

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

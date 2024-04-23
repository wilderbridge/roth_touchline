from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="ModuleRegistrationData")


@_attrs_define
class ModuleRegistrationData:
    """ 
        Attributes:
            account_id (Union[Unset, int]):
            module_name (Union[Unset, str]):
            registration_code (Union[Unset, str]): Code that is displayed on the controller screen
            country (Union[Unset, str]):
            zip_code (Union[Unset, str]):
            notification_email (Union[Unset, str]):
            additional_information (Union[Unset, str]):
            accept_post_policy (Union[Unset, str]):
     """

    account_id: Union[Unset, int] = UNSET
    module_name: Union[Unset, str] = UNSET
    registration_code: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    zip_code: Union[Unset, str] = UNSET
    notification_email: Union[Unset, str] = UNSET
    additional_information: Union[Unset, str] = UNSET
    accept_post_policy: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id

        module_name = self.module_name

        registration_code = self.registration_code

        country = self.country

        zip_code = self.zip_code

        notification_email = self.notification_email

        additional_information = self.additional_information

        accept_post_policy = self.accept_post_policy


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if module_name is not UNSET:
            field_dict["module_name"] = module_name
        if registration_code is not UNSET:
            field_dict["registration_code"] = registration_code
        if country is not UNSET:
            field_dict["country"] = country
        if zip_code is not UNSET:
            field_dict["zip_code"] = zip_code
        if notification_email is not UNSET:
            field_dict["notification_email"] = notification_email
        if additional_information is not UNSET:
            field_dict["additional_information"] = additional_information
        if accept_post_policy is not UNSET:
            field_dict["accept_post_policy"] = accept_post_policy

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_id = d.pop("account_id", UNSET)

        module_name = d.pop("module_name", UNSET)

        registration_code = d.pop("registration_code", UNSET)

        country = d.pop("country", UNSET)

        zip_code = d.pop("zip_code", UNSET)

        notification_email = d.pop("notification_email", UNSET)

        additional_information = d.pop("additional_information", UNSET)

        accept_post_policy = d.pop("accept_post_policy", UNSET)

        module_registration_data = cls(
            account_id=account_id,
            module_name=module_name,
            registration_code=registration_code,
            country=country,
            zip_code=zip_code,
            notification_email=notification_email,
            additional_information=additional_information,
            accept_post_policy=accept_post_policy,
        )

        module_registration_data.additional_properties = d
        return module_registration_data

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

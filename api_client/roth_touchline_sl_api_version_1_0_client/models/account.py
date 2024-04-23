from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.account_language import AccountLanguage






T = TypeVar("T", bound="Account")


@_attrs_define
class Account:
    """ 
        Attributes:
            username (str):
            password (str):
            confirm_password (str):
            email (str):
            language (AccountLanguage):
            accept_regulations (bool): /views/regulations_with_extra/regulations/regulations_en
            accept_privacy_policy (bool): /public/docs/policies/privacy_policy_tech.pdf
            accept_mobile_privacy_policy (bool): /public/docs/policies/privacy_policy__mobile_application.pdf
            accept_rules_service24 (bool): I consent to the collection and processing of my personal data by Tech -
                Sterowniki Spółka z ograniczoną odpowiedzialnością Sp.k. with registered office in Wieprz (34-122) (the
                Administrator of Personal Data) in accordance with Regulation (EU) 2016/679 of the European Parliament and of
                the Council of 27 April 2016 on the protection of individuals with regard to the processing of personal data and
                on the free movement such data and the repeal of Directive 95/46/EC for the proper functioning of the Serwis 24
                application and for the Administrator to perform all activities resulting from its operation, and I consent to
                the Administrator sharing my personal data with third parties cooperating with it.
     """

    username: str
    password: str
    confirm_password: str
    email: str
    language: AccountLanguage
    accept_regulations: bool
    accept_privacy_policy: bool
    accept_mobile_privacy_policy: bool
    accept_rules_service24: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        username = self.username

        password = self.password

        confirm_password = self.confirm_password

        email = self.email

        language = self.language.value

        accept_regulations = self.accept_regulations

        accept_privacy_policy = self.accept_privacy_policy

        accept_mobile_privacy_policy = self.accept_mobile_privacy_policy

        accept_rules_service24 = self.accept_rules_service24


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "username": username,
            "password": password,
            "confirm_password": confirm_password,
            "email": email,
            "language": language,
            "accept_regulations": accept_regulations,
            "accept_privacy_policy": accept_privacy_policy,
            "accept_mobile_privacy_policy": accept_mobile_privacy_policy,
            "accept_rules_service24": accept_rules_service24,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        username = d.pop("username")

        password = d.pop("password")

        confirm_password = d.pop("confirm_password")

        email = d.pop("email")

        language = AccountLanguage(d.pop("language"))




        accept_regulations = d.pop("accept_regulations")

        accept_privacy_policy = d.pop("accept_privacy_policy")

        accept_mobile_privacy_policy = d.pop("accept_mobile_privacy_policy")

        accept_rules_service24 = d.pop("accept_rules_service24")

        account = cls(
            username=username,
            password=password,
            confirm_password=confirm_password,
            email=email,
            language=language,
            accept_regulations=accept_regulations,
            accept_privacy_policy=accept_privacy_policy,
            accept_mobile_privacy_policy=accept_mobile_privacy_policy,
            accept_rules_service24=accept_rules_service24,
        )

        account.additional_properties = d
        return account

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

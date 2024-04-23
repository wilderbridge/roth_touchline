from enum import Enum

class DeleteAccountEmailEmailI18NI18NI18N(str, Enum):
    CS = "cs"
    DE = "de"
    EN = "en"
    ES = "es"
    ET = "et"
    FR = "fr"
    HR = "hr"
    HU = "hu"
    IT = "it"
    LT = "lt"
    NL = "nl"
    PL = "pl"
    RO = "ro"
    RU = "ru"
    SI = "si"
    SK = "sk"

    def __str__(self) -> str:
        return str(self.value)

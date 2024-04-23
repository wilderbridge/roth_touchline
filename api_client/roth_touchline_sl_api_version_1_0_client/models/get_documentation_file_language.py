from enum import Enum

class GetDocumentationFileLanguage(str, Enum):
    EN = "en"
    PL = "pl"

    def __str__(self) -> str:
        return str(self.value)

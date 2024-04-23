from enum import Enum

class GetDocumentationFileFileName(str, Enum):
    ALEXA_INSTRUCTIONS_EMODUL_SMART_DOCX = "Alexa Instructions eModul Smart.docx"
    ALEXA_INSTRUCTIONS_EMODUL_SMART_PDF = "alexa_instructions_emodul_smart.pdf"
    ALEXA_INSTRUCTIONS_SMART_PLUS_DOCX = "Alexa Instructions Smart Plus.docx"
    ALEXA_INSTRUCTIONS_SMART_PLUS_PDF = "alexa_instructions_smart_plus.pdf"
    EN_UFH8ZMP_2018_06_08_PDF = "EN_UFH8ZMP_2018.06.08.pdf"
    EN_UFHINTWIFIP_2018_05_15_PDF = "EN_UFHINTWIFIP_2018.05.15.pdf"
    EN_UFHTFTMBP_UFHTFTMWP_M_8_2018_05_30_PDF = "EN_UFHTFTMBP_UFHTFTMWP_M-8_2018.05.30.pdf"
    GOOGLE_ASSISTANT_EMODUL_SMART_INSTRUCTIONS_DOCX = "Google Assistant eModul Smart Instructions.docx"
    GOOGLE_ASSISTANT_EMODUL_SMART_INSTRUCTIONS_PDF = "Google_Assistant_eModul_Smart_Instructions.pdf"
    GOOGLE_ASSISTANT_SMART_PLUS_INSTRUCTIONS_DOCX = "Google Assistant Smart Plus Instructions.docx"
    GOOGLE_ASSISTANT_SMART_PLUS_INSTRUCTIONS_PDF = "google_assistant_smart_plus_instructions.pdf"
    GOOGLE_ASYSTENT_MODUL_TECH_PDF = "google_asystent_modul_tech.pdf"
    GOOGLE_ASYSTENT_MODUŁ_TECH_INSTRUKCJE_DOCX = "Google Asystent Moduł Tech Instrukcje.docx"
    GOOGLE_HOME_FOR_TOUCHLINE_SL_A5_UK_20221222_TIL_APP_PDF = "Google_Home_for_Touchline_SL_A5_UK_20221222_til_app.pdf"
    POLITYKA_PRYWATNOSCI_TECH_PDF = "polityka_prywatnosci_tech.pdf"
    PRIVACY_POLICY_MOBILE_APPLICATION_PDF = "privacy_policy__mobile_application.pdf"
    PRIVACY_POLICY_TECH_PDF = "privacy_policy_tech.pdf"
    ROTH_TOUCHLINE_SL_APP_USER_MANUAL_UK_20221222_TIL_APP_PDF = "Roth_Touchline_SL_app_user_manual_UK_20221222_til_app.pdf"

    def __str__(self) -> str:
        return str(self.value)

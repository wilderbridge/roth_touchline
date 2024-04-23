from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_documentation_file_language import GetDocumentationFileLanguage
from ...models.get_documentation_file_file_name import GetDocumentationFileFileName



def _get_kwargs(
    language: GetDocumentationFileLanguage,
    file_name: GetDocumentationFileFileName,

) -> Dict[str, Any]:
    

    

    

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/public/docs/{language}/{file_name}".format(language=language,file_name=file_name,),
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    language: GetDocumentationFileLanguage,
    file_name: GetDocumentationFileFileName,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Any]:
    """ Get documentation file

     Retrieves the documentation file based on the specified language and file name.

    Examples:
    - /public/docs/en/Alexa Instructions eModul Smart.docx
    - /public/docs/en/Alexa Instructions Smart Plus.docx
    - /public/docs/en/alexa_instructions_emodul_smart.pdf
    - /public/docs/en/alexa_instructions_smart_plus.pdf
    - /public/docs/en/EN_UFH8ZMP_2018.06.08.pdf
    - /public/docs/en/EN_UFHINTWIFIP_2018.05.15.pdf
    - /public/docs/en/EN_UFHTFTMBP_UFHTFTMWP_M-8_2018.05.30.pdf
    - /public/docs/en/Google Assistant eModul Smart Instructions.docx
    - /public/docs/en/Google Assistant Smart Plus Instructions.docx
    - /public/docs/en/Google_Assistant_eModul_Smart_Instructions.pdf
    - /public/docs/en/google_assistant_smart_plus_instructions.pdf
    - /public/docs/en/Google_Home_for_Touchline_SL_A5_UK_20221222_til_app.pdf
    - /public/docs/en/Roth_Touchline_SL_app_user_manual_UK_20221222_til_app.pdf
    - /public/docs/pl/Google Asystent Moduł Tech Instrukcje.docx
    - /public/docs/pl/google_asystent_modul_tech.pdf
    - /public/docs/policies/polityka_prywatnosci_tech.pdf
    - /public/docs/policies/privacy_policy__mobile_application.pdf
    - /public/docs/policies/privacy_policy_tech.pdf

    Args:
        language (GetDocumentationFileLanguage):
        file_name (GetDocumentationFileFileName):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        language=language,
file_name=file_name,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    language: GetDocumentationFileLanguage,
    file_name: GetDocumentationFileFileName,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Any]:
    """ Get documentation file

     Retrieves the documentation file based on the specified language and file name.

    Examples:
    - /public/docs/en/Alexa Instructions eModul Smart.docx
    - /public/docs/en/Alexa Instructions Smart Plus.docx
    - /public/docs/en/alexa_instructions_emodul_smart.pdf
    - /public/docs/en/alexa_instructions_smart_plus.pdf
    - /public/docs/en/EN_UFH8ZMP_2018.06.08.pdf
    - /public/docs/en/EN_UFHINTWIFIP_2018.05.15.pdf
    - /public/docs/en/EN_UFHTFTMBP_UFHTFTMWP_M-8_2018.05.30.pdf
    - /public/docs/en/Google Assistant eModul Smart Instructions.docx
    - /public/docs/en/Google Assistant Smart Plus Instructions.docx
    - /public/docs/en/Google_Assistant_eModul_Smart_Instructions.pdf
    - /public/docs/en/google_assistant_smart_plus_instructions.pdf
    - /public/docs/en/Google_Home_for_Touchline_SL_A5_UK_20221222_til_app.pdf
    - /public/docs/en/Roth_Touchline_SL_app_user_manual_UK_20221222_til_app.pdf
    - /public/docs/pl/Google Asystent Moduł Tech Instrukcje.docx
    - /public/docs/pl/google_asystent_modul_tech.pdf
    - /public/docs/policies/polityka_prywatnosci_tech.pdf
    - /public/docs/policies/privacy_policy__mobile_application.pdf
    - /public/docs/policies/privacy_policy_tech.pdf

    Args:
        language (GetDocumentationFileLanguage):
        file_name (GetDocumentationFileFileName):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        language=language,
file_name=file_name,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)


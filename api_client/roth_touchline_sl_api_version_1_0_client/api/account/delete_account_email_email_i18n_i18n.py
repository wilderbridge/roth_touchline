from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_account_email_email_i18ni18ni18n import DeleteAccountEmailEmailI18NI18NI18N



def _get_kwargs(
    email: str,
    i18n: DeleteAccountEmailEmailI18NI18NI18N,

) -> Dict[str, Any]:
    

    

    

    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": "/account/email/{email}/i18n/{i18n}".format(email=email,i18n=i18n,),
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
    email: str,
    i18n: DeleteAccountEmailEmailI18NI18NI18N,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Any]:
    """ First step of delete account.

     Send email with confirmation code

    Args:
        email (str):
        i18n (DeleteAccountEmailEmailI18NI18NI18N):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        email=email,
i18n=i18n,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    email: str,
    i18n: DeleteAccountEmailEmailI18NI18NI18N,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Any]:
    """ First step of delete account.

     Send email with confirmation code

    Args:
        email (str):
        i18n (DeleteAccountEmailEmailI18NI18NI18N):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        email=email,
i18n=i18n,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)


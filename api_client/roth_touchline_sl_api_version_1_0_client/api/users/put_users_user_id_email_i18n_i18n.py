from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import cast
from typing import Dict
from ...models.put_users_user_id_email_i18ni18n_body import PutUsersUserIdEmailI18NI18NBody
from ...models.put_users_user_id_email_i18ni18ni18n import PutUsersUserIdEmailI18NI18NI18N



def _get_kwargs(
    user_id: int,
    i18n: PutUsersUserIdEmailI18NI18NI18N,
    *,
    body: PutUsersUserIdEmailI18NI18NBody,

) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}


    

    

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/users/{user_id}/email/i18n/{i18n}".format(user_id=user_id,i18n=i18n,),
    }

    _body = body.to_dict()


    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if response.status_code == HTTPStatus.BAD_REQUEST:
        return None
    if response.status_code == HTTPStatus.NOT_FOUND:
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
    user_id: int,
    i18n: PutUsersUserIdEmailI18NI18NI18N,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PutUsersUserIdEmailI18NI18NBody,

) -> Response[Any]:
    """ First step of email update

    Args:
        user_id (int):
        i18n (PutUsersUserIdEmailI18NI18NI18N):
        body (PutUsersUserIdEmailI18NI18NBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        user_id=user_id,
i18n=i18n,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    user_id: int,
    i18n: PutUsersUserIdEmailI18NI18NI18N,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PutUsersUserIdEmailI18NI18NBody,

) -> Response[Any]:
    """ First step of email update

    Args:
        user_id (int):
        i18n (PutUsersUserIdEmailI18NI18NI18N):
        body (PutUsersUserIdEmailI18NI18NBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        user_id=user_id,
i18n=i18n,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)


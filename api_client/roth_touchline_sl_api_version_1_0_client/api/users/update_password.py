from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.update_password_body import UpdatePasswordBody
from typing import cast
from typing import Dict
from ...models.password_update_success_response import PasswordUpdateSuccessResponse
from ...models.password_update_error_response import PasswordUpdateErrorResponse



def _get_kwargs(
    user_id: int,
    *,
    body: UpdatePasswordBody,

) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}


    

    

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/users/{user_id}/password".format(user_id=user_id,),
    }

    _body = body.to_dict()


    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[PasswordUpdateErrorResponse, PasswordUpdateSuccessResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PasswordUpdateSuccessResponse.from_dict(response.json())



        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = PasswordUpdateErrorResponse.from_dict(response.json())



        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[PasswordUpdateErrorResponse, PasswordUpdateSuccessResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdatePasswordBody,

) -> Response[Union[PasswordUpdateErrorResponse, PasswordUpdateSuccessResponse]]:
    """ Update User Password

     Update the password for a user.

    Args:
        user_id (int):
        body (UpdatePasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PasswordUpdateErrorResponse, PasswordUpdateSuccessResponse]]
     """


    kwargs = _get_kwargs(
        user_id=user_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    user_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdatePasswordBody,

) -> Optional[Union[PasswordUpdateErrorResponse, PasswordUpdateSuccessResponse]]:
    """ Update User Password

     Update the password for a user.

    Args:
        user_id (int):
        body (UpdatePasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PasswordUpdateErrorResponse, PasswordUpdateSuccessResponse]
     """


    return sync_detailed(
        user_id=user_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    user_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdatePasswordBody,

) -> Response[Union[PasswordUpdateErrorResponse, PasswordUpdateSuccessResponse]]:
    """ Update User Password

     Update the password for a user.

    Args:
        user_id (int):
        body (UpdatePasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PasswordUpdateErrorResponse, PasswordUpdateSuccessResponse]]
     """


    kwargs = _get_kwargs(
        user_id=user_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    user_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdatePasswordBody,

) -> Optional[Union[PasswordUpdateErrorResponse, PasswordUpdateSuccessResponse]]:
    """ Update User Password

     Update the password for a user.

    Args:
        user_id (int):
        body (UpdatePasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PasswordUpdateErrorResponse, PasswordUpdateSuccessResponse]
     """


    return (await asyncio_detailed(
        user_id=user_id,
client=client,
body=body,

    )).parsed

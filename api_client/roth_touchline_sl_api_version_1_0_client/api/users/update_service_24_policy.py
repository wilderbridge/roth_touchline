from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import cast
from typing import Dict
from ...models.service_24_policy_response import Service24PolicyResponse
from ...models.update_service_24_policy_body import UpdateService24PolicyBody



def _get_kwargs(
    user_id: int,
    *,
    body: UpdateService24PolicyBody,

) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}


    

    

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/users/{user_id}/service24_policy".format(user_id=user_id,),
    }

    _body = body.to_dict()


    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Service24PolicyResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Service24PolicyResponse.from_dict(response.json())



        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Service24PolicyResponse]:
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
    body: UpdateService24PolicyBody,

) -> Response[Service24PolicyResponse]:
    """ Update Service24 Policy Acceptance

     Update the acceptance of Service24 policy for a user.

    Args:
        user_id (int):
        body (UpdateService24PolicyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Service24PolicyResponse]
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
    body: UpdateService24PolicyBody,

) -> Optional[Service24PolicyResponse]:
    """ Update Service24 Policy Acceptance

     Update the acceptance of Service24 policy for a user.

    Args:
        user_id (int):
        body (UpdateService24PolicyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Service24PolicyResponse
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
    body: UpdateService24PolicyBody,

) -> Response[Service24PolicyResponse]:
    """ Update Service24 Policy Acceptance

     Update the acceptance of Service24 policy for a user.

    Args:
        user_id (int):
        body (UpdateService24PolicyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Service24PolicyResponse]
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
    body: UpdateService24PolicyBody,

) -> Optional[Service24PolicyResponse]:
    """ Update Service24 Policy Acceptance

     Update the acceptance of Service24 policy for a user.

    Args:
        user_id (int):
        body (UpdateService24PolicyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Service24PolicyResponse
     """


    return (await asyncio_detailed(
        user_id=user_id,
client=client,
body=body,

    )).parsed

from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.register_push_notification_device_response_400 import RegisterPushNotificationDeviceResponse400
from typing import cast
from typing import Dict
from ...models.register_push_notification_device_body import RegisterPushNotificationDeviceBody
from ...models.register_push_notification_device_response_200 import RegisterPushNotificationDeviceResponse200



def _get_kwargs(
    user_id: int,
    *,
    body: RegisterPushNotificationDeviceBody,

) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}


    

    

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/users/{user_id}/notifications/push/device".format(user_id=user_id,),
    }

    _body = body.to_dict()


    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[RegisterPushNotificationDeviceResponse200, RegisterPushNotificationDeviceResponse400]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RegisterPushNotificationDeviceResponse200.from_dict(response.json())



        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = RegisterPushNotificationDeviceResponse400.from_dict(response.json())



        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[RegisterPushNotificationDeviceResponse200, RegisterPushNotificationDeviceResponse400]]:
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
    body: RegisterPushNotificationDeviceBody,

) -> Response[Union[RegisterPushNotificationDeviceResponse200, RegisterPushNotificationDeviceResponse400]]:
    """ Register push notification device

     Registers a push notification device for the specified user.

    Args:
        user_id (int):
        body (RegisterPushNotificationDeviceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[RegisterPushNotificationDeviceResponse200, RegisterPushNotificationDeviceResponse400]]
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
    body: RegisterPushNotificationDeviceBody,

) -> Optional[Union[RegisterPushNotificationDeviceResponse200, RegisterPushNotificationDeviceResponse400]]:
    """ Register push notification device

     Registers a push notification device for the specified user.

    Args:
        user_id (int):
        body (RegisterPushNotificationDeviceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[RegisterPushNotificationDeviceResponse200, RegisterPushNotificationDeviceResponse400]
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
    body: RegisterPushNotificationDeviceBody,

) -> Response[Union[RegisterPushNotificationDeviceResponse200, RegisterPushNotificationDeviceResponse400]]:
    """ Register push notification device

     Registers a push notification device for the specified user.

    Args:
        user_id (int):
        body (RegisterPushNotificationDeviceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[RegisterPushNotificationDeviceResponse200, RegisterPushNotificationDeviceResponse400]]
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
    body: RegisterPushNotificationDeviceBody,

) -> Optional[Union[RegisterPushNotificationDeviceResponse200, RegisterPushNotificationDeviceResponse400]]:
    """ Register push notification device

     Registers a push notification device for the specified user.

    Args:
        user_id (int):
        body (RegisterPushNotificationDeviceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[RegisterPushNotificationDeviceResponse200, RegisterPushNotificationDeviceResponse400]
     """


    return (await asyncio_detailed(
        user_id=user_id,
client=client,
body=body,

    )).parsed

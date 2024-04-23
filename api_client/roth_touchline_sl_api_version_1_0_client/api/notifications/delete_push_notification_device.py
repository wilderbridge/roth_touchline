from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_push_notification_device_error_response import DeletePushNotificationDeviceErrorResponse
from typing import cast
from typing import Dict
from ...models.delete_push_notification_device_success_response import DeletePushNotificationDeviceSuccessResponse



def _get_kwargs(
    user_id: int,
    device_id: str,

) -> Dict[str, Any]:
    

    

    

    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": "/users/{user_id}/notifications/push/devices/{device_id}".format(user_id=user_id,device_id=device_id,),
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[DeletePushNotificationDeviceErrorResponse, DeletePushNotificationDeviceSuccessResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DeletePushNotificationDeviceSuccessResponse.from_dict(response.json())



        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = DeletePushNotificationDeviceErrorResponse.from_dict(response.json())



        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[DeletePushNotificationDeviceErrorResponse, DeletePushNotificationDeviceSuccessResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: int,
    device_id: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Union[DeletePushNotificationDeviceErrorResponse, DeletePushNotificationDeviceSuccessResponse]]:
    """ Delete push notification device

     Deletes the push notification device associated with the specified user.

    Args:
        user_id (int):
        device_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeletePushNotificationDeviceErrorResponse, DeletePushNotificationDeviceSuccessResponse]]
     """


    kwargs = _get_kwargs(
        user_id=user_id,
device_id=device_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    user_id: int,
    device_id: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Optional[Union[DeletePushNotificationDeviceErrorResponse, DeletePushNotificationDeviceSuccessResponse]]:
    """ Delete push notification device

     Deletes the push notification device associated with the specified user.

    Args:
        user_id (int):
        device_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeletePushNotificationDeviceErrorResponse, DeletePushNotificationDeviceSuccessResponse]
     """


    return sync_detailed(
        user_id=user_id,
device_id=device_id,
client=client,

    ).parsed

async def asyncio_detailed(
    user_id: int,
    device_id: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Union[DeletePushNotificationDeviceErrorResponse, DeletePushNotificationDeviceSuccessResponse]]:
    """ Delete push notification device

     Deletes the push notification device associated with the specified user.

    Args:
        user_id (int):
        device_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeletePushNotificationDeviceErrorResponse, DeletePushNotificationDeviceSuccessResponse]]
     """


    kwargs = _get_kwargs(
        user_id=user_id,
device_id=device_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    user_id: int,
    device_id: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Optional[Union[DeletePushNotificationDeviceErrorResponse, DeletePushNotificationDeviceSuccessResponse]]:
    """ Delete push notification device

     Deletes the push notification device associated with the specified user.

    Args:
        user_id (int):
        device_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeletePushNotificationDeviceErrorResponse, DeletePushNotificationDeviceSuccessResponse]
     """


    return (await asyncio_detailed(
        user_id=user_id,
device_id=device_id,
client=client,

    )).parsed

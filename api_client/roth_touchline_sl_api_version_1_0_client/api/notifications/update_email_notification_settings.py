from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.update_email_notification_settings_response_400 import UpdateEmailNotificationSettingsResponse400
from ...models.update_email_notification_settings_body import UpdateEmailNotificationSettingsBody
from typing import cast
from typing import Dict
from ...models.update_email_notification_settings_response_200 import UpdateEmailNotificationSettingsResponse200



def _get_kwargs(
    user_id: int,
    module_uuid: str,
    *,
    body: UpdateEmailNotificationSettingsBody,

) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}


    

    

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/users/{user_id}/modules/{module_uuid}/notifications/email".format(user_id=user_id,module_uuid=module_uuid,),
    }

    _body = body.to_dict()


    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[UpdateEmailNotificationSettingsResponse200, UpdateEmailNotificationSettingsResponse400]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UpdateEmailNotificationSettingsResponse200.from_dict(response.json())



        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = UpdateEmailNotificationSettingsResponse400.from_dict(response.json())



        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[UpdateEmailNotificationSettingsResponse200, UpdateEmailNotificationSettingsResponse400]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: int,
    module_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateEmailNotificationSettingsBody,

) -> Response[Union[UpdateEmailNotificationSettingsResponse200, UpdateEmailNotificationSettingsResponse400]]:
    """ Update email notification settings

     Updates the email notification settings for the specified user module.

    Args:
        user_id (int):
        module_uuid (str):
        body (UpdateEmailNotificationSettingsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[UpdateEmailNotificationSettingsResponse200, UpdateEmailNotificationSettingsResponse400]]
     """


    kwargs = _get_kwargs(
        user_id=user_id,
module_uuid=module_uuid,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    user_id: int,
    module_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateEmailNotificationSettingsBody,

) -> Optional[Union[UpdateEmailNotificationSettingsResponse200, UpdateEmailNotificationSettingsResponse400]]:
    """ Update email notification settings

     Updates the email notification settings for the specified user module.

    Args:
        user_id (int):
        module_uuid (str):
        body (UpdateEmailNotificationSettingsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[UpdateEmailNotificationSettingsResponse200, UpdateEmailNotificationSettingsResponse400]
     """


    return sync_detailed(
        user_id=user_id,
module_uuid=module_uuid,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    user_id: int,
    module_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateEmailNotificationSettingsBody,

) -> Response[Union[UpdateEmailNotificationSettingsResponse200, UpdateEmailNotificationSettingsResponse400]]:
    """ Update email notification settings

     Updates the email notification settings for the specified user module.

    Args:
        user_id (int):
        module_uuid (str):
        body (UpdateEmailNotificationSettingsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[UpdateEmailNotificationSettingsResponse200, UpdateEmailNotificationSettingsResponse400]]
     """


    kwargs = _get_kwargs(
        user_id=user_id,
module_uuid=module_uuid,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    user_id: int,
    module_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateEmailNotificationSettingsBody,

) -> Optional[Union[UpdateEmailNotificationSettingsResponse200, UpdateEmailNotificationSettingsResponse400]]:
    """ Update email notification settings

     Updates the email notification settings for the specified user module.

    Args:
        user_id (int):
        module_uuid (str):
        body (UpdateEmailNotificationSettingsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[UpdateEmailNotificationSettingsResponse200, UpdateEmailNotificationSettingsResponse400]
     """


    return (await asyncio_detailed(
        user_id=user_id,
module_uuid=module_uuid,
client=client,
body=body,

    )).parsed

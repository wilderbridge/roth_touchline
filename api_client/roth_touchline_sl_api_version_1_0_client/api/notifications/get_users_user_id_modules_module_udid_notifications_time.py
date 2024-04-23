from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import cast, List
from typing import cast
from typing import Dict
from ...models.get_users_user_id_modules_module_udid_notifications_time_response_200_item import GetUsersUserIdModulesModuleUdidNotificationsTimeResponse200Item



def _get_kwargs(
    user_id: int,
    module_udid: int,

) -> Dict[str, Any]:
    

    

    

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/users/{user_id}/modules/{module_udid}/notifications/time".format(user_id=user_id,module_udid=module_udid,),
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, List['GetUsersUserIdModulesModuleUdidNotificationsTimeResponse200Item']]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = GetUsersUserIdModulesModuleUdidNotificationsTimeResponse200Item.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, List['GetUsersUserIdModulesModuleUdidNotificationsTimeResponse200Item']]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: int,
    module_udid: int,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Union[Any, List['GetUsersUserIdModulesModuleUdidNotificationsTimeResponse200Item']]]:
    """ Get notifications time

     Retrieve notifications time based on user ID and module UDID.

    Args:
        user_id (int):
        module_udid (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['GetUsersUserIdModulesModuleUdidNotificationsTimeResponse200Item']]]
     """


    kwargs = _get_kwargs(
        user_id=user_id,
module_udid=module_udid,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    user_id: int,
    module_udid: int,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Optional[Union[Any, List['GetUsersUserIdModulesModuleUdidNotificationsTimeResponse200Item']]]:
    """ Get notifications time

     Retrieve notifications time based on user ID and module UDID.

    Args:
        user_id (int):
        module_udid (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['GetUsersUserIdModulesModuleUdidNotificationsTimeResponse200Item']]
     """


    return sync_detailed(
        user_id=user_id,
module_udid=module_udid,
client=client,

    ).parsed

async def asyncio_detailed(
    user_id: int,
    module_udid: int,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Union[Any, List['GetUsersUserIdModulesModuleUdidNotificationsTimeResponse200Item']]]:
    """ Get notifications time

     Retrieve notifications time based on user ID and module UDID.

    Args:
        user_id (int):
        module_udid (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['GetUsersUserIdModulesModuleUdidNotificationsTimeResponse200Item']]]
     """


    kwargs = _get_kwargs(
        user_id=user_id,
module_udid=module_udid,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    user_id: int,
    module_udid: int,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Optional[Union[Any, List['GetUsersUserIdModulesModuleUdidNotificationsTimeResponse200Item']]]:
    """ Get notifications time

     Retrieve notifications time based on user ID and module UDID.

    Args:
        user_id (int):
        module_udid (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['GetUsersUserIdModulesModuleUdidNotificationsTimeResponse200Item']]
     """


    return (await asyncio_detailed(
        user_id=user_id,
module_udid=module_udid,
client=client,

    )).parsed

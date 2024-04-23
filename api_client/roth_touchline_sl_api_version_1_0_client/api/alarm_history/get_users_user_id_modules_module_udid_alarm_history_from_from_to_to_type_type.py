from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_users_user_id_modules_module_udid_alarm_history_from_from_to_to_type_type_type import GetUsersUserIdModulesModuleUdidAlarmHistoryFromFromToToTypeTypeType



def _get_kwargs(
    user_id: int,
    module_udid: int,
    from_: str,
    to: str,
    type: GetUsersUserIdModulesModuleUdidAlarmHistoryFromFromToToTypeTypeType,

) -> Dict[str, Any]:
    

    

    

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/users/{user_id}/modules/{module_udid}/alarm_history/from/{from_}/to/{to}/type/{type}".format(user_id=user_id,module_udid=module_udid,from_=from_,to=to,type=type,),
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
    user_id: int,
    module_udid: int,
    from_: str,
    to: str,
    type: GetUsersUserIdModulesModuleUdidAlarmHistoryFromFromToToTypeTypeType,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Any]:
    """ Change zone name/icon

     ```Field                       Type        require     Options
    from                           String      yes         start date e.g. 2023-02-01
    to                             String      yes         end date e.g. 2023-02-11
    type                           String      yes         Options: 'all', 'alarm', 'warning',
    'notification'

    Args:
        user_id (int):
        module_udid (int):
        from_ (str):  Example: 2020-10-20.
        to (str):  Example: 2020-10-20.
        type (GetUsersUserIdModulesModuleUdidAlarmHistoryFromFromToToTypeTypeType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        user_id=user_id,
module_udid=module_udid,
from_=from_,
to=to,
type=type,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    user_id: int,
    module_udid: int,
    from_: str,
    to: str,
    type: GetUsersUserIdModulesModuleUdidAlarmHistoryFromFromToToTypeTypeType,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Any]:
    """ Change zone name/icon

     ```Field                       Type        require     Options
    from                           String      yes         start date e.g. 2023-02-01
    to                             String      yes         end date e.g. 2023-02-11
    type                           String      yes         Options: 'all', 'alarm', 'warning',
    'notification'

    Args:
        user_id (int):
        module_udid (int):
        from_ (str):  Example: 2020-10-20.
        to (str):  Example: 2020-10-20.
        type (GetUsersUserIdModulesModuleUdidAlarmHistoryFromFromToToTypeTypeType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        user_id=user_id,
module_udid=module_udid,
from_=from_,
to=to,
type=type,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)


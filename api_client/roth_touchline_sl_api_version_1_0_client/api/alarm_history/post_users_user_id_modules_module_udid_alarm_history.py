from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import cast
from typing import Dict
from ...models.post_users_user_id_modules_module_udid_alarm_history_body import PostUsersUserIdModulesModuleUdidAlarmHistoryBody



def _get_kwargs(
    user_id: int,
    module_udid: int,
    *,
    body: PostUsersUserIdModulesModuleUdidAlarmHistoryBody,

) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}


    

    

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/users/{user_id}/modules/{module_udid}/alarm_history".format(user_id=user_id,module_udid=module_udid,),
    }

    _body = body.to_dict()


    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if response.status_code == HTTPStatus.FORBIDDEN:
        return None
    if response.status_code == HTTPStatus.BAD_REQUEST:
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
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostUsersUserIdModulesModuleUdidAlarmHistoryBody,

) -> Response[Any]:
    """ Confirm alarm

    Args:
        user_id (int):
        module_udid (int):
        body (PostUsersUserIdModulesModuleUdidAlarmHistoryBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        user_id=user_id,
module_udid=module_udid,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    user_id: int,
    module_udid: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostUsersUserIdModulesModuleUdidAlarmHistoryBody,

) -> Response[Any]:
    """ Confirm alarm

    Args:
        user_id (int):
        module_udid (int):
        body (PostUsersUserIdModulesModuleUdidAlarmHistoryBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        user_id=user_id,
module_udid=module_udid,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)


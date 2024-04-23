from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.zone_mode import ZoneMode
from typing import cast
from typing import Dict
from ...models.zone_mode import ZoneMode



def _get_kwargs(
    user_id: int,
    module_udid: int,
    *,
    body: ZoneMode,
    modeOrZone: str,

) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}






    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/users/{user_id}/modules/{module_udid}/zones".format(user_id=user_id,module_udid=module_udid,),
    }

    _body = {modeOrZone: body.to_dict() }
    print(_body)


    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[ZoneMode]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ZoneMode.from_dict(response.json())



        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[ZoneMode]:
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
    body: ZoneMode,

) -> Response[ZoneMode]:
    r""" Change zone parameters

     Change zone parameters (L-7, L-8, WiFi 8S, ST-8S WiFi) \n
    Set constant temperature:

    1. **Set constant temperature**:  \
    POST data example:
       {
        \"mode\": {
            \"id\": 210,
            \"parentId\": 101,
            \"mode\": \"constantTemp\",
            \"constTempTime\": 0,
            \"setTemperature\": 220,
            \"scheduleIndex\": 0
        }
    }

    2. **Set constant temperature with time limitation**: \
    POST data example:{
        \"mode\": {
            \"id\": 210,
            \"parentId\": 101,
            \"mode\": \"timeLimit\",
            \"constTempTime\": 60,
            \"setTemperature\": 220,
            \"scheduleIndex\": 0
        }
    }
    3. **Turn on zone**: \
    POST data example:
    {
        \"zone\": {
            \"id\": 101,
            \"zoneState\": \"zoneOn\"
        }
    }
    4. **Turn off zone**: \
    POST data example:
    {
        \"zone\": {
            \"id\": 101,
            \"zoneState\": \"zoneOff\"
        }
    }

    Args:
        user_id (int):
        module_udid (int):
        body (ZoneMode):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ZoneMode]
     """


    kwargs = _get_kwargs(
        user_id=user_id,
module_udid=module_udid,
body=body,
modeOrZone=modeOrZone

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
    body: ZoneMode,

) -> Optional[ZoneMode]:
    r""" Change zone parameters

     Change zone parameters (L-7, L-8, WiFi 8S, ST-8S WiFi) \n
    Set constant temperature:

    1. **Set constant temperature**:  \
    POST data example:
       {
        \"mode\": {
            \"id\": 210,
            \"parentId\": 101,
            \"mode\": \"constantTemp\",
            \"constTempTime\": 0,
            \"setTemperature\": 220,
            \"scheduleIndex\": 0
        }
    }

    2. **Set constant temperature with time limitation**: \
    POST data example:{
        \"mode\": {
            \"id\": 210,
            \"parentId\": 101,
            \"mode\": \"timeLimit\",
            \"constTempTime\": 60,
            \"setTemperature\": 220,
            \"scheduleIndex\": 0
        }
    }
    3. **Turn on zone**: \
    POST data example:
    {
        \"zone\": {
            \"id\": 101,
            \"zoneState\": \"zoneOn\"
        }
    }
    4. **Turn off zone**: \
    POST data example:
    {
        \"zone\": {
            \"id\": 101,
            \"zoneState\": \"zoneOff\"
        }
    }

    Args:
        user_id (int):
        module_udid (int):
        body (ZoneMode):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ZoneMode
     """


    return sync_detailed(
        user_id=user_id,
module_udid=module_udid,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    user_id: int,
    module_udid: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ZoneMode,
    modeOrZone: str,

) -> Response[ZoneMode]:
    r""" Change zone parameters

     Change zone parameters (L-7, L-8, WiFi 8S, ST-8S WiFi) \n
    Set constant temperature:

    1. **Set constant temperature**:  \
    POST data example:
       {
        \"mode\": {
            \"id\": 210,
            \"parentId\": 101,
            \"mode\": \"constantTemp\",
            \"constTempTime\": 0,
            \"setTemperature\": 220,
            \"scheduleIndex\": 0
        }
    }

    2. **Set constant temperature with time limitation**: \
    POST data example:{
        \"mode\": {
            \"id\": 210,
            \"parentId\": 101,
            \"mode\": \"timeLimit\",
            \"constTempTime\": 60,
            \"setTemperature\": 220,
            \"scheduleIndex\": 0
        }
    }
    3. **Turn on zone**: \
    POST data example:
    {
        \"zone\": {
            \"id\": 101,
            \"zoneState\": \"zoneOn\"
        }
    }
    4. **Turn off zone**: \
    POST data example:
    {
        \"zone\": {
            \"id\": 101,
            \"zoneState\": \"zoneOff\"
        }
    }

    Args:
        user_id (int):
        module_udid (int):
        body (ZoneMode):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ZoneMode]
     """


    kwargs = _get_kwargs(
        user_id=user_id,
module_udid=module_udid,
body=body,
modeOrZone=modeOrZone
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
    body: ZoneMode,
    modeOrZone: str,

) -> Optional[ZoneMode]:
    r""" Change zone parameters

     Change zone parameters (L-7, L-8, WiFi 8S, ST-8S WiFi) \n
    Set constant temperature:

    1. **Set constant temperature**:  \
    POST data example:
       {
        \"mode\": {
            \"id\": 210,
            \"parentId\": 101,
            \"mode\": \"constantTemp\",
            \"constTempTime\": 0,
            \"setTemperature\": 220,
            \"scheduleIndex\": 0
        }
    }

    2. **Set constant temperature with time limitation**: \
    POST data example:{
        \"mode\": {
            \"id\": 210,
            \"parentId\": 101,
            \"mode\": \"timeLimit\",
            \"constTempTime\": 60,
            \"setTemperature\": 220,
            \"scheduleIndex\": 0
        }
    }
    3. **Turn on zone**: \
    POST data example:
    {
        \"zone\": {
            \"id\": 101,
            \"zoneState\": \"zoneOn\"
        }
    }
    4. **Turn off zone**: \
    POST data example:
    {
        \"zone\": {
            \"id\": 101,
            \"zoneState\": \"zoneOff\"
        }
    }

    Args:
        user_id (int):
        module_udid (int):
        body (ZoneMode):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ZoneMode
     """


    return (await asyncio_detailed(
        user_id=user_id,
module_udid=module_udid,
client=client,
body=body,
modeOrZone=modeOrZone

    )).parsed

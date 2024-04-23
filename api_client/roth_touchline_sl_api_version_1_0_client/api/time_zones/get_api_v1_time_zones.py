from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import cast, List
from typing import cast
from ...models.time_zones_response_item import TimeZonesResponseItem
from typing import Dict



def _get_kwargs(
    
) -> Dict[str, Any]:
    

    

    

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/time_zones",
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, List['TimeZonesResponseItem']]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_time_zones_response_item_data in (_response_200):
            componentsschemas_time_zones_response_item = TimeZonesResponseItem.from_dict(componentsschemas_time_zones_response_item_data)



            response_200.append(componentsschemas_time_zones_response_item)

        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = cast(Any, None)
        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, List['TimeZonesResponseItem']]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Union[Any, List['TimeZonesResponseItem']]]:
    r""" getting the time zone

     ### Response data example:
     ``[
    {
      \"id\": 0,
      \"gmt\": \"-11:00\",
      \"en\": \"Midway Island, Samoa\",
      \"pl\": \"Midway Island, Samoa\",
      \"ru\": \"Остров Мидуэй, Самоа\"
    },
    {
      \"id\": 1,
      \"gmt\": \"-10:00\",
      \"en\": \"Hawaii\",
      \"pl\": \"Hawaje\",
      \"ru\": \"Гавайи\"
    },
    ...
     ``

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['TimeZonesResponseItem']]]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],

) -> Optional[Union[Any, List['TimeZonesResponseItem']]]:
    r""" getting the time zone

     ### Response data example:
     ``[
    {
      \"id\": 0,
      \"gmt\": \"-11:00\",
      \"en\": \"Midway Island, Samoa\",
      \"pl\": \"Midway Island, Samoa\",
      \"ru\": \"Остров Мидуэй, Самоа\"
    },
    {
      \"id\": 1,
      \"gmt\": \"-10:00\",
      \"en\": \"Hawaii\",
      \"pl\": \"Hawaje\",
      \"ru\": \"Гавайи\"
    },
    ...
     ``

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['TimeZonesResponseItem']]
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Union[Any, List['TimeZonesResponseItem']]]:
    r""" getting the time zone

     ### Response data example:
     ``[
    {
      \"id\": 0,
      \"gmt\": \"-11:00\",
      \"en\": \"Midway Island, Samoa\",
      \"pl\": \"Midway Island, Samoa\",
      \"ru\": \"Остров Мидуэй, Самоа\"
    },
    {
      \"id\": 1,
      \"gmt\": \"-10:00\",
      \"en\": \"Hawaii\",
      \"pl\": \"Hawaje\",
      \"ru\": \"Гавайи\"
    },
    ...
     ``

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['TimeZonesResponseItem']]]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],

) -> Optional[Union[Any, List['TimeZonesResponseItem']]]:
    r""" getting the time zone

     ### Response data example:
     ``[
    {
      \"id\": 0,
      \"gmt\": \"-11:00\",
      \"en\": \"Midway Island, Samoa\",
      \"pl\": \"Midway Island, Samoa\",
      \"ru\": \"Остров Мидуэй, Самоа\"
    },
    {
      \"id\": 1,
      \"gmt\": \"-10:00\",
      \"en\": \"Hawaii\",
      \"pl\": \"Hawaje\",
      \"ru\": \"Гавайи\"
    },
    ...
     ``

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['TimeZonesResponseItem']]
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed

from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_modules_module_uuid_statistics_type_range_range_month_type import GetModulesModuleUuidStatisticsTypeRangeRangeMonthType
from ...models.get_modules_module_uuid_statistics_type_range_range_month_range import GetModulesModuleUuidStatisticsTypeRangeRangeMonthRange



def _get_kwargs(
    module_uuid: str,
    type: GetModulesModuleUuidStatisticsTypeRangeRangeMonthType,
    range_: GetModulesModuleUuidStatisticsTypeRangeRangeMonthRange,
    month: int,

) -> Dict[str, Any]:
    

    

    

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/modules/{module_uuid}/statistics/{type}/range/{range_}/{month}".format(module_uuid=module_uuid,type=type,range_=range_,month=month,),
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if response.status_code == HTTPStatus.BAD_REQUEST:
        return None
    if response.status_code == HTTPStatus.NOT_FOUND:
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
    module_uuid: str,
    type: GetModulesModuleUuidStatisticsTypeRangeRangeMonthType,
    range_: GetModulesModuleUuidStatisticsTypeRangeRangeMonthRange,
    month: int,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Any]:
    """ Statistics month

    Args:
        module_uuid (str):
        type (GetModulesModuleUuidStatisticsTypeRangeRangeMonthType):
        range_ (GetModulesModuleUuidStatisticsTypeRangeRangeMonthRange):
        month (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        module_uuid=module_uuid,
type=type,
range_=range_,
month=month,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    module_uuid: str,
    type: GetModulesModuleUuidStatisticsTypeRangeRangeMonthType,
    range_: GetModulesModuleUuidStatisticsTypeRangeRangeMonthRange,
    month: int,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Any]:
    """ Statistics month

    Args:
        module_uuid (str):
        type (GetModulesModuleUuidStatisticsTypeRangeRangeMonthType):
        range_ (GetModulesModuleUuidStatisticsTypeRangeRangeMonthRange):
        month (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        module_uuid=module_uuid,
type=type,
range_=range_,
month=month,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)


from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors




def _get_kwargs(
    module_uuid: str,
    range_: str,

) -> Dict[str, Any]:
    

    

    

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/modules/{module_uuid}/statistics/linear/range/{range_}".format(module_uuid=module_uuid,range_=range_,),
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
    range_: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Any]:
    r""" Statistics

     ```
    Field                       Type        require     Options
    module_uuid                 String      true
    range                       String      true        'day' - last day, 'week' - last week, 'month' -
    last month or selected month
    month                       Integer     no          1,2,3,4,5,6,7,8,9,10,11,12
    year                        Integer     no          2020,2021

    Example requests:
    GET '/api/v1/modules/:module_uuid/statistics/linear/range/day'
    GET '/api/v1/modules/:module_uuid/statistics/linear/range/week'
    GET '/api/v1/modules/:module_uuid/statistics/linear/range/month'
    GET '/api/v1/modules/:module_uuid/statistics/linear/range/month/7'
    GET '/api/v1/modules/:module_uuid/statistics/linear/range/month/8/year/2020'

    Example responses:
    1.{ \"status\":\"success\",
      \"data\": {
        \"history\": {
    \"|&^4fdkl|Kitchen\":[{\"x\":\"202110280025\",\"y\":21.0},{\"x\":\"202110280028\",\"y\":21.0}...]},
        \"descriptions\": [\"|&^4fdkl|Kitchen\", \"1234\", \"1686:2\"]
      }
    }
    2.{ \"status\":\"success\",
      \"data\":{
        \"history\":{\"1686:2\":[{\"x\":\"202110280000\",\"y\":20.0,{\"x\":\"202110280100\",\"y\":20.0}.
    ..}]},
        \"descriptions\": [\"|&^4fdkl|Kitchen\", \"1234\", \"1686:2\"]}
      }
    3.{ \"status\":\"success\",
      \"data\":{\"history\":{\"795\":[{\"x\":\"202110280000\",\"y\":20.0,{\"x\":\"202110280100\",\"y\":2
    0.0}...}]},
      \"descriptions\": [\"|&^4fdkl|Kitchen\", \"1234\", \"1686:2\"]
      }
    }

    Possible descriptions:
    1. Description with the string \"|&^4fdkl|\" shows that the description was entered by the user.
    Example: \"|&^4fdkl|Kitchen\" is just \"Kitchen\".
    2. Description with \"1682:\" shows that it is index in translations and next to \":\" is just
    number. Example: \"1686:2\" is \"Zone 2\"
    3. Description with only a number is a index in translations (look at point 9). Example 795 is
    \"External temperature\"

    Args:
        module_uuid (str):
        range_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        module_uuid=module_uuid,
range_=range_,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    module_uuid: str,
    range_: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Any]:
    r""" Statistics

     ```
    Field                       Type        require     Options
    module_uuid                 String      true
    range                       String      true        'day' - last day, 'week' - last week, 'month' -
    last month or selected month
    month                       Integer     no          1,2,3,4,5,6,7,8,9,10,11,12
    year                        Integer     no          2020,2021

    Example requests:
    GET '/api/v1/modules/:module_uuid/statistics/linear/range/day'
    GET '/api/v1/modules/:module_uuid/statistics/linear/range/week'
    GET '/api/v1/modules/:module_uuid/statistics/linear/range/month'
    GET '/api/v1/modules/:module_uuid/statistics/linear/range/month/7'
    GET '/api/v1/modules/:module_uuid/statistics/linear/range/month/8/year/2020'

    Example responses:
    1.{ \"status\":\"success\",
      \"data\": {
        \"history\": {
    \"|&^4fdkl|Kitchen\":[{\"x\":\"202110280025\",\"y\":21.0},{\"x\":\"202110280028\",\"y\":21.0}...]},
        \"descriptions\": [\"|&^4fdkl|Kitchen\", \"1234\", \"1686:2\"]
      }
    }
    2.{ \"status\":\"success\",
      \"data\":{
        \"history\":{\"1686:2\":[{\"x\":\"202110280000\",\"y\":20.0,{\"x\":\"202110280100\",\"y\":20.0}.
    ..}]},
        \"descriptions\": [\"|&^4fdkl|Kitchen\", \"1234\", \"1686:2\"]}
      }
    3.{ \"status\":\"success\",
      \"data\":{\"history\":{\"795\":[{\"x\":\"202110280000\",\"y\":20.0,{\"x\":\"202110280100\",\"y\":2
    0.0}...}]},
      \"descriptions\": [\"|&^4fdkl|Kitchen\", \"1234\", \"1686:2\"]
      }
    }

    Possible descriptions:
    1. Description with the string \"|&^4fdkl|\" shows that the description was entered by the user.
    Example: \"|&^4fdkl|Kitchen\" is just \"Kitchen\".
    2. Description with \"1682:\" shows that it is index in translations and next to \":\" is just
    number. Example: \"1686:2\" is \"Zone 2\"
    3. Description with only a number is a index in translations (look at point 9). Example 795 is
    \"External temperature\"

    Args:
        module_uuid (str):
        range_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        module_uuid=module_uuid,
range_=range_,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)


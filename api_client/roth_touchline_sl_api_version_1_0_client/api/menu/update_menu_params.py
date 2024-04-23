from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.update_menu_params_menu_type import UpdateMenuParamsMenuType



def _get_kwargs(
    user_id: int,
    module_udid: int,
    menu_type: UpdateMenuParamsMenuType,
    ido: int,

) -> Dict[str, Any]:
    

    

    

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/users/{user_id}/modules/{module_udid}/menu/{menu_type}/ido/{ido}".format(user_id=user_id,module_udid=module_udid,menu_type=menu_type,ido=ido,),
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
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
    menu_type: UpdateMenuParamsMenuType,
    ido: int,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Any]:
    r""" Update parameter

     ```
      Parameter Type Required Description
      menu_type String yes Options: 'MU', 'MI', 'MS', 'MP'
      ido Number yes Parameter ido

      when a menu item is locked you need to attach a pin. For example:
      {
        \"pin\": 1234,
        \"value: 25
      }

      type 1 - Valid values

      POST data example:
      {
          \"value\": 25
      }
      \"value\": current value

      Response data example:
      {
          \"status\": \"success\",
          \"data\": \"1\"
      }

      error example:
      { error: 'Value out of range' }

      type 2 - Valid values

      POST data example:
      {
          \"value\": 100
      }
      \"value\": value 1/10

      Response data example:
      {
          \"status\": \"success\",
          \"data\": \"1\"
      }

      error example:
      {
          error: 'Value out of range'
      }

      type 3 - Valid values

      POST data example:
      {
          \"value\": 30
      }
      \"value\": value min: sec

      Response data example:
      {
          \"status\": \"success\",
          \"data\": \"1\"
      }

      error example:
      {
          error: 'Value out of range'
      }
      type 4 - Valid values

      POST data example:
      {
          \"value\": 60
      }
      \"value\": value hour: min

      Response data example:
      {
          \"status\": \"success\",
          \"data\": \"1\"
      }

      error example:
      {
          error: 'Value out of range'
      }

      type 5 - Valid values

      POST data example:
      {
          \"value\": 15
      }
      \"value\": value h: min during the day

      Response data example:
      {
          \"status\": \"success\",
          \"data\": \"1\"
      }

      error example:
      {
          error: 'Value out of range'
      }

      type 6 -  Entering code (input)

      POST data example:
      {
          \"code\": 1234
      }
      \"code\":access code

      Response data example:
      {
          \"status\": \"success\",
          \"data\": \"1\"
      }

      error example:
      {
          error: 'the code is not a number'
      }

      type 7 - Time mode (temperature + time)

      POST data example:
      {
          \"temp\":50,
          \"time\":100
      }
      \"temp\": temperature transfer value
      \"time\": time transfer value

      Response data example:
      {
          \"status\": \"success\",
          \"data\": \"1\"
      }

      error example:
      {
          error: 'Value out of range'
      }

      type 10 - ON / OFF

      POST data example:
      {
          \"value\": 1
      }
      \"value\": enable(1) or disable(0) the value

      Response data example:
      {
          \"status\": \"success\",
          \"data\": \"1\"
      }

      error example:
      {
          error: 'Invalid value for turn on-off'
      }

      type 11 - Choice 1 out of many

      POST data example:
      {
          \"value\": 1
      }
      \"value\": Choice 1 of many

      Response data example:
      {
          \"status\": \"success\",
          \"data\": \"1\"
      }

      error example:
      {
          error: 'Value out of range'
      }

      type 111 -  Selection of strip mode (or other zone controller)

      POST data example:
      {
          \"value\": 1
      }
      \"value\":Choice 1 of many

      Response data example:
      {
          \"status\": \"success\",
          \"data\": \"1\"
      }

      error example:
      {
          error: 'wrong number of parameters'
      }

      type 112 - Selection 1 of many + wiki, message

      POST data example:
      {
          \"value\": 1
      }
      \"value\":Choice 1 of many

      Response data example:
      {
          \"status\": \"success\",
          \"data\": \"1\"
      }

      error example:
      {
          error: 'Value out of range'
      }

      type 12 - Weekly + -

      POST data example:
      {
          \"weekly_plus_minus\":{
          \"values\":[0,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,0,15,15,15,15,15,15]
      }
      }
      \"values\": [new adjustment values...]

      Response data example:
      {
          \"status\": \"success\",
          \"data\": \"1\"
      }

      error example:
      {
          error: 'wrong number of hours'
      }

      type 13 - Weekly on / off

      POST data example:
      {
          \"weekly_on_off\":{
              \"values\":[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
          }
      }
      \"values\": [values on off...]
      1 - on
      0 - off

      Response data example:
      {
          \"status\": \"success\",
          \"data\": \"1\"
      }

      error example:
      {
          error: 'wrong number of parameters'
      }

      type 15 - Many-of-many selection (ON / OFF set of lamps)
      POST data example:
      {
          \"many_of_many\":[
          {
              \"id\":0,
              \"value\":1
          },
          {
              \"id\":1,
              \"value\":1
          }
          ]
      }
      \"id\" - item id
      \"value\" - selected value
      1 - checked
      0 - unchecked

      Response data example:
      {
          \"status\": \"success\",
          \"data\": \"1\"
      }

      error example:
      {
          error: 'too many elements'
      }

      type 29 - Heating curve offset / slope - Viessmann

      POST data example:
      {
          \"slope\":4,
          \"shift\":4
      }
      \"slope\": value slope
      \"shift\": value shift

      Response data example:
      {
          \"status\": \"success\",
          \"data\": \"1\"
      }

      error example:
      {
          error: 'Value out of range'
      }

      type 30 - Heat curve

      POST data example:
      {
          \"heating_curve\":[
          {
              \"id\":0,
              \"value\":33
          },
          {
              \"id\":1,
              \"value\":33
          },{
              \"id\":2,
              \"value\":33
          },
          {
              \"id\":3,
              \"value\":33
          }
          ]
      }
      \"id\":element id
      \"value\":values after editing

      Response data example:
      {
          \"status\": \"success\",
          \"data\": \"1\"
      }

      error example:
      { error: 'number of items out of range' }
      { error: 'Value out of range' }

      type 31 - Heating curve slope / offset

      POST data example:
      {
          \"slope\":4,
          \"shift\":4
      }
      \"slope\": value slope
      \"shift\": value shift

      error example:
      {
          error: 'Value out of range'
      }

      type 100 - Universal schedule

      POST data example:
      {
          \"universal_schedule\":[
          {
              \"start\":0,
              \"end\":15,
              \"interval\":1,
              \"temp\": 20
          },
          {
              \"start\":15,
              \"end\":30,
              \"interval\":1,
              \"temp\": 20
          },
          {
              \"start\":30,
              \"end\":45,
              \"interval\":1,
              \"temp\": 20
          },
          {
              \"start\":45,
              \"end\":60,
              \"interval\":1,
              \"temp\": 20
          },
          {
              \"start\":60,
              \"end\":1439,
              \"interval\":1,
              \"temp\": 20
          }
          ]
      }
      \"start\":start time expressed in seconds ,
      \"end\":end time in seconds
      \"interval\":fan power,
      \"temp\": set temperature

      Response data example:
      {
          \"status\": \"success\",
          \"data\": \"1\"
      }

      error example:
      { error: 'the time of the first object is not equal to 0' }
      { error: 'the time of the last object is not equal to 1439' }
      { error: 'the times are intertwined' }
      { error: 'time is not quarterly' }
      { error: 'the number of items is incorrect' }

      type 106 - Universal value editing

      POST data example:
      {\"value\": 10}
      \"value\": current value

      Response data example:
      {
          \"status\": \"success\",
          \"data\": \"1\"
      }

      error example:
      {
           error: 'Value out of range'
      }

      type 107 - Date edit

      POST data example:
      {
          \"year\":2020,
          \"month\":3,
          \"day\": 21
      }
      \"year\":year,
      \"month\":month,
      \"day\": day

      Response data example:
      {
          \"status\": \"success\",
          \"data\": \"1\"
      }

      error example:
      { error: 'wrong day data' }
      { error: 'wrong month data' }

      type 108 - Edition of the range (date from - date to)

      POST data example:
      {
          \"date_start\":{
              \"year\":2019,
              \"month\":12,
              \"day\":1
          },
          \"date_end\":{
          \"year\":2019,
          \"month\":12,
          \"day\":2
          }
      }
      \"year\":year,
      \"month\":month,
      \"day\": day

      Response data example:
      {
          \"status\": \"success\",
          \"data\": \"1\"
      }

      error example:
      { error: 'the dates overlap' }
      { error: 'wrong day data' }
      { error: 'wrong month data' }

      type 109 - Date (various formats and edits supported)

      POST data example:
      {
          \"years\":2000,
          \"month\":4,
          \"day\":3
      }
      \"year\":year,
      \"month\":month,
      \"day\": day

      Response data example:
      {
          \"status\": \"success\",
          \"data\": \"1\"
      }

      error example:
      { error: 'month is out of range' }
      { error: 'too many elements' }

      type 120 - Viessmann schedule

      POST data example:
      {
          \"schedule\":[
          {
          \"day\": 0,
          \"time\":[{\"start\":300,\"end\":400},{\"start\":400,\"end\":500},{\"start\":600,\"end\":700}]
          },
          {
          \"day\": 1,
          \"time\":[{\"start\":300,\"end\":400},{\"start\":400,\"end\":500},{\"start\":600,\"end\":700}]
          }
          ]
      }
      day: days of the week
      0 - Monday
      1 - Tuesday
      2 - Wednesday
      3 - Thursday
      4 - Friday
      5 - Saturday
      6 - Sunday
      time: schedule work time
      \"start\":the stated start time
      \"end\": end time

      Response data example:
      {
          \"status\": \"success\",
          \"data\": \"1\"
      }

      error example:
      { error: 'wrong number of time' }
      { error: 'the times are coming' }
      { error: 'wrong number of days' }

    Args:
        user_id (int):
        module_udid (int):
        menu_type (UpdateMenuParamsMenuType):
        ido (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        user_id=user_id,
module_udid=module_udid,
menu_type=menu_type,
ido=ido,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    user_id: int,
    module_udid: int,
    menu_type: UpdateMenuParamsMenuType,
    ido: int,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Any]:
    r""" Update parameter

     ```
      Parameter Type Required Description
      menu_type String yes Options: 'MU', 'MI', 'MS', 'MP'
      ido Number yes Parameter ido

      when a menu item is locked you need to attach a pin. For example:
      {
        \"pin\": 1234,
        \"value: 25
      }

      type 1 - Valid values

      POST data example:
      {
          \"value\": 25
      }
      \"value\": current value

      Response data example:
      {
          \"status\": \"success\",
          \"data\": \"1\"
      }

      error example:
      { error: 'Value out of range' }

      type 2 - Valid values

      POST data example:
      {
          \"value\": 100
      }
      \"value\": value 1/10

      Response data example:
      {
          \"status\": \"success\",
          \"data\": \"1\"
      }

      error example:
      {
          error: 'Value out of range'
      }

      type 3 - Valid values

      POST data example:
      {
          \"value\": 30
      }
      \"value\": value min: sec

      Response data example:
      {
          \"status\": \"success\",
          \"data\": \"1\"
      }

      error example:
      {
          error: 'Value out of range'
      }
      type 4 - Valid values

      POST data example:
      {
          \"value\": 60
      }
      \"value\": value hour: min

      Response data example:
      {
          \"status\": \"success\",
          \"data\": \"1\"
      }

      error example:
      {
          error: 'Value out of range'
      }

      type 5 - Valid values

      POST data example:
      {
          \"value\": 15
      }
      \"value\": value h: min during the day

      Response data example:
      {
          \"status\": \"success\",
          \"data\": \"1\"
      }

      error example:
      {
          error: 'Value out of range'
      }

      type 6 -  Entering code (input)

      POST data example:
      {
          \"code\": 1234
      }
      \"code\":access code

      Response data example:
      {
          \"status\": \"success\",
          \"data\": \"1\"
      }

      error example:
      {
          error: 'the code is not a number'
      }

      type 7 - Time mode (temperature + time)

      POST data example:
      {
          \"temp\":50,
          \"time\":100
      }
      \"temp\": temperature transfer value
      \"time\": time transfer value

      Response data example:
      {
          \"status\": \"success\",
          \"data\": \"1\"
      }

      error example:
      {
          error: 'Value out of range'
      }

      type 10 - ON / OFF

      POST data example:
      {
          \"value\": 1
      }
      \"value\": enable(1) or disable(0) the value

      Response data example:
      {
          \"status\": \"success\",
          \"data\": \"1\"
      }

      error example:
      {
          error: 'Invalid value for turn on-off'
      }

      type 11 - Choice 1 out of many

      POST data example:
      {
          \"value\": 1
      }
      \"value\": Choice 1 of many

      Response data example:
      {
          \"status\": \"success\",
          \"data\": \"1\"
      }

      error example:
      {
          error: 'Value out of range'
      }

      type 111 -  Selection of strip mode (or other zone controller)

      POST data example:
      {
          \"value\": 1
      }
      \"value\":Choice 1 of many

      Response data example:
      {
          \"status\": \"success\",
          \"data\": \"1\"
      }

      error example:
      {
          error: 'wrong number of parameters'
      }

      type 112 - Selection 1 of many + wiki, message

      POST data example:
      {
          \"value\": 1
      }
      \"value\":Choice 1 of many

      Response data example:
      {
          \"status\": \"success\",
          \"data\": \"1\"
      }

      error example:
      {
          error: 'Value out of range'
      }

      type 12 - Weekly + -

      POST data example:
      {
          \"weekly_plus_minus\":{
          \"values\":[0,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,0,15,15,15,15,15,15]
      }
      }
      \"values\": [new adjustment values...]

      Response data example:
      {
          \"status\": \"success\",
          \"data\": \"1\"
      }

      error example:
      {
          error: 'wrong number of hours'
      }

      type 13 - Weekly on / off

      POST data example:
      {
          \"weekly_on_off\":{
              \"values\":[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
          }
      }
      \"values\": [values on off...]
      1 - on
      0 - off

      Response data example:
      {
          \"status\": \"success\",
          \"data\": \"1\"
      }

      error example:
      {
          error: 'wrong number of parameters'
      }

      type 15 - Many-of-many selection (ON / OFF set of lamps)
      POST data example:
      {
          \"many_of_many\":[
          {
              \"id\":0,
              \"value\":1
          },
          {
              \"id\":1,
              \"value\":1
          }
          ]
      }
      \"id\" - item id
      \"value\" - selected value
      1 - checked
      0 - unchecked

      Response data example:
      {
          \"status\": \"success\",
          \"data\": \"1\"
      }

      error example:
      {
          error: 'too many elements'
      }

      type 29 - Heating curve offset / slope - Viessmann

      POST data example:
      {
          \"slope\":4,
          \"shift\":4
      }
      \"slope\": value slope
      \"shift\": value shift

      Response data example:
      {
          \"status\": \"success\",
          \"data\": \"1\"
      }

      error example:
      {
          error: 'Value out of range'
      }

      type 30 - Heat curve

      POST data example:
      {
          \"heating_curve\":[
          {
              \"id\":0,
              \"value\":33
          },
          {
              \"id\":1,
              \"value\":33
          },{
              \"id\":2,
              \"value\":33
          },
          {
              \"id\":3,
              \"value\":33
          }
          ]
      }
      \"id\":element id
      \"value\":values after editing

      Response data example:
      {
          \"status\": \"success\",
          \"data\": \"1\"
      }

      error example:
      { error: 'number of items out of range' }
      { error: 'Value out of range' }

      type 31 - Heating curve slope / offset

      POST data example:
      {
          \"slope\":4,
          \"shift\":4
      }
      \"slope\": value slope
      \"shift\": value shift

      error example:
      {
          error: 'Value out of range'
      }

      type 100 - Universal schedule

      POST data example:
      {
          \"universal_schedule\":[
          {
              \"start\":0,
              \"end\":15,
              \"interval\":1,
              \"temp\": 20
          },
          {
              \"start\":15,
              \"end\":30,
              \"interval\":1,
              \"temp\": 20
          },
          {
              \"start\":30,
              \"end\":45,
              \"interval\":1,
              \"temp\": 20
          },
          {
              \"start\":45,
              \"end\":60,
              \"interval\":1,
              \"temp\": 20
          },
          {
              \"start\":60,
              \"end\":1439,
              \"interval\":1,
              \"temp\": 20
          }
          ]
      }
      \"start\":start time expressed in seconds ,
      \"end\":end time in seconds
      \"interval\":fan power,
      \"temp\": set temperature

      Response data example:
      {
          \"status\": \"success\",
          \"data\": \"1\"
      }

      error example:
      { error: 'the time of the first object is not equal to 0' }
      { error: 'the time of the last object is not equal to 1439' }
      { error: 'the times are intertwined' }
      { error: 'time is not quarterly' }
      { error: 'the number of items is incorrect' }

      type 106 - Universal value editing

      POST data example:
      {\"value\": 10}
      \"value\": current value

      Response data example:
      {
          \"status\": \"success\",
          \"data\": \"1\"
      }

      error example:
      {
           error: 'Value out of range'
      }

      type 107 - Date edit

      POST data example:
      {
          \"year\":2020,
          \"month\":3,
          \"day\": 21
      }
      \"year\":year,
      \"month\":month,
      \"day\": day

      Response data example:
      {
          \"status\": \"success\",
          \"data\": \"1\"
      }

      error example:
      { error: 'wrong day data' }
      { error: 'wrong month data' }

      type 108 - Edition of the range (date from - date to)

      POST data example:
      {
          \"date_start\":{
              \"year\":2019,
              \"month\":12,
              \"day\":1
          },
          \"date_end\":{
          \"year\":2019,
          \"month\":12,
          \"day\":2
          }
      }
      \"year\":year,
      \"month\":month,
      \"day\": day

      Response data example:
      {
          \"status\": \"success\",
          \"data\": \"1\"
      }

      error example:
      { error: 'the dates overlap' }
      { error: 'wrong day data' }
      { error: 'wrong month data' }

      type 109 - Date (various formats and edits supported)

      POST data example:
      {
          \"years\":2000,
          \"month\":4,
          \"day\":3
      }
      \"year\":year,
      \"month\":month,
      \"day\": day

      Response data example:
      {
          \"status\": \"success\",
          \"data\": \"1\"
      }

      error example:
      { error: 'month is out of range' }
      { error: 'too many elements' }

      type 120 - Viessmann schedule

      POST data example:
      {
          \"schedule\":[
          {
          \"day\": 0,
          \"time\":[{\"start\":300,\"end\":400},{\"start\":400,\"end\":500},{\"start\":600,\"end\":700}]
          },
          {
          \"day\": 1,
          \"time\":[{\"start\":300,\"end\":400},{\"start\":400,\"end\":500},{\"start\":600,\"end\":700}]
          }
          ]
      }
      day: days of the week
      0 - Monday
      1 - Tuesday
      2 - Wednesday
      3 - Thursday
      4 - Friday
      5 - Saturday
      6 - Sunday
      time: schedule work time
      \"start\":the stated start time
      \"end\": end time

      Response data example:
      {
          \"status\": \"success\",
          \"data\": \"1\"
      }

      error example:
      { error: 'wrong number of time' }
      { error: 'the times are coming' }
      { error: 'wrong number of days' }

    Args:
        user_id (int):
        module_udid (int):
        menu_type (UpdateMenuParamsMenuType):
        ido (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        user_id=user_id,
module_udid=module_udid,
menu_type=menu_type,
ido=ido,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)


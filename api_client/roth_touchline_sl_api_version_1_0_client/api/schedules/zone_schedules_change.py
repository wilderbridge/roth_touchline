from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import cast
from typing import Dict
from ...models.zone_schedules import ZoneSchedules



def _get_kwargs(
    user_id: int,
    module_udid: int,
    zone_id: int,
    *,
    body: ZoneSchedules,

) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}


    

    

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/users/{user_id}/modules/{module_udid}/zones/{zone_id}/local_schedule".format(user_id=user_id,module_udid=module_udid,zone_id=zone_id,),
    }

    _body = body.to_dict()


    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[ZoneSchedules]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ZoneSchedules.from_dict(response.json())



        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[ZoneSchedules]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: int,
    module_udid: int,
    zone_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ZoneSchedules,

) -> Response[ZoneSchedules]:
    r""" Local zone schedules

     ### POST data example:
    ```
    {
      modeId = 100
      schedule = {
              id: 150,
              index: -1,
              p0Days: [\"1\", \"1\", \"1\", \"1\", \"1\", \"0\", \"0\"],
              p0Intervals: [{start:0, stop: 480, temp: 180}, {start: 480, stop: 960, temp: 240}],
              p0SetbackTemp: 200,
              p1Days: [\"0\", \"0\", \"0\", \"0\", \"0\", \"1\", \"1\"],
              p1Intervals: ddd,
              p1SetbackTemp: 210
          }
     }

    modeId(integer):                                   id of the mode object (nakładka)  connected to
    the zone
    schedule(object)    id(integer):                   id of the global schedule connected to specified
    module
                        index(integer):                index of the global schedule (0 to 4)
                        p0Days(array of strings):      array of days turned on/off for program 1(1 - on,
    0 - off). Values must be opposites of p1Days.
                        p0Intervals(array of objects): group of intervals for program 1. Maximum 3
    intervals (can be empty)
                                                        - each interval requires 3 properties: start,
    stop and temp
                                                        - start/stop define the starting/stopping times
    for the interval
                                                        - start/stop represent time in minutes. Min 0,
    Max 1440
                                                        - temp defines the temperature for the interval
    (x10). Min 50 max 350.
                                                        eg. {start: 480, stop: 960, temp 200} from 8:00
    - 16:00 temperature will be 20 degrees celsius
                        p0SetbackTemp(integer):         temperature for anytime not covered by
    p0Intervals. Min 50 max 350.
                        p1Days(array of strings):       array of days turned on/off for program 2(1 -
    on, 0 - off). Values must be opposites of p0Days.
                        p1Intervals(array of objects):  group of intervals for program 2. Maximum 3
    intervals (can be empty)
                                                        - each interval requires 3 properties: start,
    stop and temp
                                                        - start/stop define the starting/stopping times
    for the interval
                                                        - start/stop represent time in minutes. Min 0,
    Max 1440
                                                        - temp defines the temperature for the interval
    (x10). Min 50 max 350.
                                                        eg. {start: 480, stop: 960, temp 200} from 8:00
    - 16:00 temperature will be 20 degrees celsius
                        p1SetbackTemp(integer):         temperature for any time not covered by
    p1Intervals. Min 50 max 350.
    Error response

    Each error response returns data in the following format:
    {\"error\": \"code_for_received_error\", \"error_description\": \"Some text describing the error\"}


         invalid_json
              General error regarding incorrectly sent data.
    Schedule property errors:

          missing_schedule_property
              The request is missing the required 'schedule' property.

          invalid_schedule_property
              The request is missing required properties on the schedule property. 'schedule' must have
    the following
              properties: id, index, p0Days, p0Intervals, p0SetbackTemp, p1Days, p1Intervals,
    p1SetbackTemp.

          Interval errors:

              invalid_number_of_interval_elements
                  Invalid amount of elements in 'p0Intervals' or 'p1Intervals'. The maximum allowed
    amount is 3.

              missing_interval_property
                  Element(s) of 'p0Intervals' or 'p1Intervals' are missing interval properties. Each
    interval must have the
                  following properties: start, stop, temp.

              invalid_interval_start_out_of_range
              invalid_interval_stop_out_of_range
                  Element(s) of 'p0Intervals' or 'p1Intervals' have an invalid 'start' or 'stop'
    property. 'start' and 'stop'
                  must be between 0 and 1440.

              invalid_interval_start_time_not_increment_of_15
              invalid_interval_stop_time_not_increment_of_15
                  Element(s) of 'p0Intervals' or 'p1Intervals' have an invalid 'start' or 'stop'
    property. 'start' and 'stop'
                  must be an increment of 15.

          invalid_interval_stop_greater_than_or_equal_to_start
              Element(s) of 'p0Intervals' or 'p1Intervals' start property must be less than (and not
    equal) to the stop
              property.

          invalid_interval_temp
              Element(s) of 'p0Intervals' or 'p1Intervals' have and invalid temp property. Temp must be
    between 50
              and 350 inclusive.

          invalid_interval_overlap
              Element(s) of 'p0Intervals' or 'p1Intervals' start/stop times overlap each other. An
    element's 'start' must be
              greater than or equal to the previous element's 'stop'.


      Day errors
            invalid_p0days_length
            invalid_p1days_length
                The request has an invalid 'p0Days' or 'p1Days' property. Its length must always be 7
    (the amount of days
                in a week).

            invalid_p0day_element
            invalid_p1day_element
                The request has an invalid 'p0Days' or 'p1Days' property. Each element must be either
    \"0\" or \"1\".

            invalid_pday_equal
                An element at 'n' in 'p0Days' has the same value as 'p1Days' at index 'n'. Elements at
    the same index must
                not have the same value.

        invalid_p0setback_temp
        invalid_p1setback_temp
                The request has an invalid 'p0SetbackTemp' or 'p1SetbackTemp' property. It's value must
    be between 50
                and 350 inclusive.

        invalid_local_schedule_index
            Invalid 'index' property on 'schedule' property. The index must be between -40 and -1
    inclusive.

        invalid_local_schedule_property
            The request is missing the required 'modeId' property.

        invalid_local_schedule_zone_not_in_module
            The 'zoneId' parameter has an id that does not belong to the specified module.

        invalid_local_schedule_doesnt_belong_to_zone
            The request's schedule has an id that does not belong to the zone.

        invalid_local_schedule_index_mismatch
            The request's schedule has an index which doesn't match it's id.

        invalid_local_schedule_mode_not_in_zone
            The request's modeId does not belong to it's zone.

       Type errors

               invalid_schedule_type
                    Wrong type for schedule property. Schedule must be an object.

                invalid_pinterval_type
                    Wrong type for p0Interval or p1Interval property. p0Interval and p1Interval must be
    arrays of objects.

                invalid_interval_type
                    Wrong type for interval property. Interval must be a object.

                invalid_interval_start_type
                    Wrong type for interval start property. Start must be an integer.

                invalid_interval_stop_type
                    Wrong type for interval stop property. Stop must be an integer.

                invalid_interval_temp_type
                    Wrong type for interval temp property. Temp must be an integer.

                invalid_p0days_type
                    Wrong type for p0Days. p0Days must be an array of strings.

                invalid_p1days_type
                    Wrong type for p1Days. p1Days must be an array of strings.

                invalid_p0day_element_type
                    Wrong type for p0Day element. p0Day elements must be strings.

                invalid_p1day_element_type
                    Wrong type for p1Day element. p1Day elements must be strings.

                invalid_p0setback_temp_type
                    Wrong type for p0SetbackType. p0SetbackType must be an integer.

                invalid_p1setback_temp_type
                    Wrong type for p1SetbackType. p1SetbackType must be an integer.

                invalid_local_schedule_index_type
                    Wrong type for index. Index must be an integer.

                invalid_local_schedule_mode_id_type
                    Wrong type for modeId. modeId must be an integer.

    Args:
        user_id (int):
        module_udid (int):
        zone_id (int):
        body (ZoneSchedules):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ZoneSchedules]
     """


    kwargs = _get_kwargs(
        user_id=user_id,
module_udid=module_udid,
zone_id=zone_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    user_id: int,
    module_udid: int,
    zone_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ZoneSchedules,

) -> Optional[ZoneSchedules]:
    r""" Local zone schedules

     ### POST data example:
    ```
    {
      modeId = 100
      schedule = {
              id: 150,
              index: -1,
              p0Days: [\"1\", \"1\", \"1\", \"1\", \"1\", \"0\", \"0\"],
              p0Intervals: [{start:0, stop: 480, temp: 180}, {start: 480, stop: 960, temp: 240}],
              p0SetbackTemp: 200,
              p1Days: [\"0\", \"0\", \"0\", \"0\", \"0\", \"1\", \"1\"],
              p1Intervals: ddd,
              p1SetbackTemp: 210
          }
     }

    modeId(integer):                                   id of the mode object (nakładka)  connected to
    the zone
    schedule(object)    id(integer):                   id of the global schedule connected to specified
    module
                        index(integer):                index of the global schedule (0 to 4)
                        p0Days(array of strings):      array of days turned on/off for program 1(1 - on,
    0 - off). Values must be opposites of p1Days.
                        p0Intervals(array of objects): group of intervals for program 1. Maximum 3
    intervals (can be empty)
                                                        - each interval requires 3 properties: start,
    stop and temp
                                                        - start/stop define the starting/stopping times
    for the interval
                                                        - start/stop represent time in minutes. Min 0,
    Max 1440
                                                        - temp defines the temperature for the interval
    (x10). Min 50 max 350.
                                                        eg. {start: 480, stop: 960, temp 200} from 8:00
    - 16:00 temperature will be 20 degrees celsius
                        p0SetbackTemp(integer):         temperature for anytime not covered by
    p0Intervals. Min 50 max 350.
                        p1Days(array of strings):       array of days turned on/off for program 2(1 -
    on, 0 - off). Values must be opposites of p0Days.
                        p1Intervals(array of objects):  group of intervals for program 2. Maximum 3
    intervals (can be empty)
                                                        - each interval requires 3 properties: start,
    stop and temp
                                                        - start/stop define the starting/stopping times
    for the interval
                                                        - start/stop represent time in minutes. Min 0,
    Max 1440
                                                        - temp defines the temperature for the interval
    (x10). Min 50 max 350.
                                                        eg. {start: 480, stop: 960, temp 200} from 8:00
    - 16:00 temperature will be 20 degrees celsius
                        p1SetbackTemp(integer):         temperature for any time not covered by
    p1Intervals. Min 50 max 350.
    Error response

    Each error response returns data in the following format:
    {\"error\": \"code_for_received_error\", \"error_description\": \"Some text describing the error\"}


         invalid_json
              General error regarding incorrectly sent data.
    Schedule property errors:

          missing_schedule_property
              The request is missing the required 'schedule' property.

          invalid_schedule_property
              The request is missing required properties on the schedule property. 'schedule' must have
    the following
              properties: id, index, p0Days, p0Intervals, p0SetbackTemp, p1Days, p1Intervals,
    p1SetbackTemp.

          Interval errors:

              invalid_number_of_interval_elements
                  Invalid amount of elements in 'p0Intervals' or 'p1Intervals'. The maximum allowed
    amount is 3.

              missing_interval_property
                  Element(s) of 'p0Intervals' or 'p1Intervals' are missing interval properties. Each
    interval must have the
                  following properties: start, stop, temp.

              invalid_interval_start_out_of_range
              invalid_interval_stop_out_of_range
                  Element(s) of 'p0Intervals' or 'p1Intervals' have an invalid 'start' or 'stop'
    property. 'start' and 'stop'
                  must be between 0 and 1440.

              invalid_interval_start_time_not_increment_of_15
              invalid_interval_stop_time_not_increment_of_15
                  Element(s) of 'p0Intervals' or 'p1Intervals' have an invalid 'start' or 'stop'
    property. 'start' and 'stop'
                  must be an increment of 15.

          invalid_interval_stop_greater_than_or_equal_to_start
              Element(s) of 'p0Intervals' or 'p1Intervals' start property must be less than (and not
    equal) to the stop
              property.

          invalid_interval_temp
              Element(s) of 'p0Intervals' or 'p1Intervals' have and invalid temp property. Temp must be
    between 50
              and 350 inclusive.

          invalid_interval_overlap
              Element(s) of 'p0Intervals' or 'p1Intervals' start/stop times overlap each other. An
    element's 'start' must be
              greater than or equal to the previous element's 'stop'.


      Day errors
            invalid_p0days_length
            invalid_p1days_length
                The request has an invalid 'p0Days' or 'p1Days' property. Its length must always be 7
    (the amount of days
                in a week).

            invalid_p0day_element
            invalid_p1day_element
                The request has an invalid 'p0Days' or 'p1Days' property. Each element must be either
    \"0\" or \"1\".

            invalid_pday_equal
                An element at 'n' in 'p0Days' has the same value as 'p1Days' at index 'n'. Elements at
    the same index must
                not have the same value.

        invalid_p0setback_temp
        invalid_p1setback_temp
                The request has an invalid 'p0SetbackTemp' or 'p1SetbackTemp' property. It's value must
    be between 50
                and 350 inclusive.

        invalid_local_schedule_index
            Invalid 'index' property on 'schedule' property. The index must be between -40 and -1
    inclusive.

        invalid_local_schedule_property
            The request is missing the required 'modeId' property.

        invalid_local_schedule_zone_not_in_module
            The 'zoneId' parameter has an id that does not belong to the specified module.

        invalid_local_schedule_doesnt_belong_to_zone
            The request's schedule has an id that does not belong to the zone.

        invalid_local_schedule_index_mismatch
            The request's schedule has an index which doesn't match it's id.

        invalid_local_schedule_mode_not_in_zone
            The request's modeId does not belong to it's zone.

       Type errors

               invalid_schedule_type
                    Wrong type for schedule property. Schedule must be an object.

                invalid_pinterval_type
                    Wrong type for p0Interval or p1Interval property. p0Interval and p1Interval must be
    arrays of objects.

                invalid_interval_type
                    Wrong type for interval property. Interval must be a object.

                invalid_interval_start_type
                    Wrong type for interval start property. Start must be an integer.

                invalid_interval_stop_type
                    Wrong type for interval stop property. Stop must be an integer.

                invalid_interval_temp_type
                    Wrong type for interval temp property. Temp must be an integer.

                invalid_p0days_type
                    Wrong type for p0Days. p0Days must be an array of strings.

                invalid_p1days_type
                    Wrong type for p1Days. p1Days must be an array of strings.

                invalid_p0day_element_type
                    Wrong type for p0Day element. p0Day elements must be strings.

                invalid_p1day_element_type
                    Wrong type for p1Day element. p1Day elements must be strings.

                invalid_p0setback_temp_type
                    Wrong type for p0SetbackType. p0SetbackType must be an integer.

                invalid_p1setback_temp_type
                    Wrong type for p1SetbackType. p1SetbackType must be an integer.

                invalid_local_schedule_index_type
                    Wrong type for index. Index must be an integer.

                invalid_local_schedule_mode_id_type
                    Wrong type for modeId. modeId must be an integer.

    Args:
        user_id (int):
        module_udid (int):
        zone_id (int):
        body (ZoneSchedules):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ZoneSchedules
     """


    return sync_detailed(
        user_id=user_id,
module_udid=module_udid,
zone_id=zone_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    user_id: int,
    module_udid: int,
    zone_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ZoneSchedules,

) -> Response[ZoneSchedules]:
    r""" Local zone schedules

     ### POST data example:
    ```
    {
      modeId = 100
      schedule = {
              id: 150,
              index: -1,
              p0Days: [\"1\", \"1\", \"1\", \"1\", \"1\", \"0\", \"0\"],
              p0Intervals: [{start:0, stop: 480, temp: 180}, {start: 480, stop: 960, temp: 240}],
              p0SetbackTemp: 200,
              p1Days: [\"0\", \"0\", \"0\", \"0\", \"0\", \"1\", \"1\"],
              p1Intervals: ddd,
              p1SetbackTemp: 210
          }
     }

    modeId(integer):                                   id of the mode object (nakładka)  connected to
    the zone
    schedule(object)    id(integer):                   id of the global schedule connected to specified
    module
                        index(integer):                index of the global schedule (0 to 4)
                        p0Days(array of strings):      array of days turned on/off for program 1(1 - on,
    0 - off). Values must be opposites of p1Days.
                        p0Intervals(array of objects): group of intervals for program 1. Maximum 3
    intervals (can be empty)
                                                        - each interval requires 3 properties: start,
    stop and temp
                                                        - start/stop define the starting/stopping times
    for the interval
                                                        - start/stop represent time in minutes. Min 0,
    Max 1440
                                                        - temp defines the temperature for the interval
    (x10). Min 50 max 350.
                                                        eg. {start: 480, stop: 960, temp 200} from 8:00
    - 16:00 temperature will be 20 degrees celsius
                        p0SetbackTemp(integer):         temperature for anytime not covered by
    p0Intervals. Min 50 max 350.
                        p1Days(array of strings):       array of days turned on/off for program 2(1 -
    on, 0 - off). Values must be opposites of p0Days.
                        p1Intervals(array of objects):  group of intervals for program 2. Maximum 3
    intervals (can be empty)
                                                        - each interval requires 3 properties: start,
    stop and temp
                                                        - start/stop define the starting/stopping times
    for the interval
                                                        - start/stop represent time in minutes. Min 0,
    Max 1440
                                                        - temp defines the temperature for the interval
    (x10). Min 50 max 350.
                                                        eg. {start: 480, stop: 960, temp 200} from 8:00
    - 16:00 temperature will be 20 degrees celsius
                        p1SetbackTemp(integer):         temperature for any time not covered by
    p1Intervals. Min 50 max 350.
    Error response

    Each error response returns data in the following format:
    {\"error\": \"code_for_received_error\", \"error_description\": \"Some text describing the error\"}


         invalid_json
              General error regarding incorrectly sent data.
    Schedule property errors:

          missing_schedule_property
              The request is missing the required 'schedule' property.

          invalid_schedule_property
              The request is missing required properties on the schedule property. 'schedule' must have
    the following
              properties: id, index, p0Days, p0Intervals, p0SetbackTemp, p1Days, p1Intervals,
    p1SetbackTemp.

          Interval errors:

              invalid_number_of_interval_elements
                  Invalid amount of elements in 'p0Intervals' or 'p1Intervals'. The maximum allowed
    amount is 3.

              missing_interval_property
                  Element(s) of 'p0Intervals' or 'p1Intervals' are missing interval properties. Each
    interval must have the
                  following properties: start, stop, temp.

              invalid_interval_start_out_of_range
              invalid_interval_stop_out_of_range
                  Element(s) of 'p0Intervals' or 'p1Intervals' have an invalid 'start' or 'stop'
    property. 'start' and 'stop'
                  must be between 0 and 1440.

              invalid_interval_start_time_not_increment_of_15
              invalid_interval_stop_time_not_increment_of_15
                  Element(s) of 'p0Intervals' or 'p1Intervals' have an invalid 'start' or 'stop'
    property. 'start' and 'stop'
                  must be an increment of 15.

          invalid_interval_stop_greater_than_or_equal_to_start
              Element(s) of 'p0Intervals' or 'p1Intervals' start property must be less than (and not
    equal) to the stop
              property.

          invalid_interval_temp
              Element(s) of 'p0Intervals' or 'p1Intervals' have and invalid temp property. Temp must be
    between 50
              and 350 inclusive.

          invalid_interval_overlap
              Element(s) of 'p0Intervals' or 'p1Intervals' start/stop times overlap each other. An
    element's 'start' must be
              greater than or equal to the previous element's 'stop'.


      Day errors
            invalid_p0days_length
            invalid_p1days_length
                The request has an invalid 'p0Days' or 'p1Days' property. Its length must always be 7
    (the amount of days
                in a week).

            invalid_p0day_element
            invalid_p1day_element
                The request has an invalid 'p0Days' or 'p1Days' property. Each element must be either
    \"0\" or \"1\".

            invalid_pday_equal
                An element at 'n' in 'p0Days' has the same value as 'p1Days' at index 'n'. Elements at
    the same index must
                not have the same value.

        invalid_p0setback_temp
        invalid_p1setback_temp
                The request has an invalid 'p0SetbackTemp' or 'p1SetbackTemp' property. It's value must
    be between 50
                and 350 inclusive.

        invalid_local_schedule_index
            Invalid 'index' property on 'schedule' property. The index must be between -40 and -1
    inclusive.

        invalid_local_schedule_property
            The request is missing the required 'modeId' property.

        invalid_local_schedule_zone_not_in_module
            The 'zoneId' parameter has an id that does not belong to the specified module.

        invalid_local_schedule_doesnt_belong_to_zone
            The request's schedule has an id that does not belong to the zone.

        invalid_local_schedule_index_mismatch
            The request's schedule has an index which doesn't match it's id.

        invalid_local_schedule_mode_not_in_zone
            The request's modeId does not belong to it's zone.

       Type errors

               invalid_schedule_type
                    Wrong type for schedule property. Schedule must be an object.

                invalid_pinterval_type
                    Wrong type for p0Interval or p1Interval property. p0Interval and p1Interval must be
    arrays of objects.

                invalid_interval_type
                    Wrong type for interval property. Interval must be a object.

                invalid_interval_start_type
                    Wrong type for interval start property. Start must be an integer.

                invalid_interval_stop_type
                    Wrong type for interval stop property. Stop must be an integer.

                invalid_interval_temp_type
                    Wrong type for interval temp property. Temp must be an integer.

                invalid_p0days_type
                    Wrong type for p0Days. p0Days must be an array of strings.

                invalid_p1days_type
                    Wrong type for p1Days. p1Days must be an array of strings.

                invalid_p0day_element_type
                    Wrong type for p0Day element. p0Day elements must be strings.

                invalid_p1day_element_type
                    Wrong type for p1Day element. p1Day elements must be strings.

                invalid_p0setback_temp_type
                    Wrong type for p0SetbackType. p0SetbackType must be an integer.

                invalid_p1setback_temp_type
                    Wrong type for p1SetbackType. p1SetbackType must be an integer.

                invalid_local_schedule_index_type
                    Wrong type for index. Index must be an integer.

                invalid_local_schedule_mode_id_type
                    Wrong type for modeId. modeId must be an integer.

    Args:
        user_id (int):
        module_udid (int):
        zone_id (int):
        body (ZoneSchedules):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ZoneSchedules]
     """


    kwargs = _get_kwargs(
        user_id=user_id,
module_udid=module_udid,
zone_id=zone_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    user_id: int,
    module_udid: int,
    zone_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ZoneSchedules,

) -> Optional[ZoneSchedules]:
    r""" Local zone schedules

     ### POST data example:
    ```
    {
      modeId = 100
      schedule = {
              id: 150,
              index: -1,
              p0Days: [\"1\", \"1\", \"1\", \"1\", \"1\", \"0\", \"0\"],
              p0Intervals: [{start:0, stop: 480, temp: 180}, {start: 480, stop: 960, temp: 240}],
              p0SetbackTemp: 200,
              p1Days: [\"0\", \"0\", \"0\", \"0\", \"0\", \"1\", \"1\"],
              p1Intervals: ddd,
              p1SetbackTemp: 210
          }
     }

    modeId(integer):                                   id of the mode object (nakładka)  connected to
    the zone
    schedule(object)    id(integer):                   id of the global schedule connected to specified
    module
                        index(integer):                index of the global schedule (0 to 4)
                        p0Days(array of strings):      array of days turned on/off for program 1(1 - on,
    0 - off). Values must be opposites of p1Days.
                        p0Intervals(array of objects): group of intervals for program 1. Maximum 3
    intervals (can be empty)
                                                        - each interval requires 3 properties: start,
    stop and temp
                                                        - start/stop define the starting/stopping times
    for the interval
                                                        - start/stop represent time in minutes. Min 0,
    Max 1440
                                                        - temp defines the temperature for the interval
    (x10). Min 50 max 350.
                                                        eg. {start: 480, stop: 960, temp 200} from 8:00
    - 16:00 temperature will be 20 degrees celsius
                        p0SetbackTemp(integer):         temperature for anytime not covered by
    p0Intervals. Min 50 max 350.
                        p1Days(array of strings):       array of days turned on/off for program 2(1 -
    on, 0 - off). Values must be opposites of p0Days.
                        p1Intervals(array of objects):  group of intervals for program 2. Maximum 3
    intervals (can be empty)
                                                        - each interval requires 3 properties: start,
    stop and temp
                                                        - start/stop define the starting/stopping times
    for the interval
                                                        - start/stop represent time in minutes. Min 0,
    Max 1440
                                                        - temp defines the temperature for the interval
    (x10). Min 50 max 350.
                                                        eg. {start: 480, stop: 960, temp 200} from 8:00
    - 16:00 temperature will be 20 degrees celsius
                        p1SetbackTemp(integer):         temperature for any time not covered by
    p1Intervals. Min 50 max 350.
    Error response

    Each error response returns data in the following format:
    {\"error\": \"code_for_received_error\", \"error_description\": \"Some text describing the error\"}


         invalid_json
              General error regarding incorrectly sent data.
    Schedule property errors:

          missing_schedule_property
              The request is missing the required 'schedule' property.

          invalid_schedule_property
              The request is missing required properties on the schedule property. 'schedule' must have
    the following
              properties: id, index, p0Days, p0Intervals, p0SetbackTemp, p1Days, p1Intervals,
    p1SetbackTemp.

          Interval errors:

              invalid_number_of_interval_elements
                  Invalid amount of elements in 'p0Intervals' or 'p1Intervals'. The maximum allowed
    amount is 3.

              missing_interval_property
                  Element(s) of 'p0Intervals' or 'p1Intervals' are missing interval properties. Each
    interval must have the
                  following properties: start, stop, temp.

              invalid_interval_start_out_of_range
              invalid_interval_stop_out_of_range
                  Element(s) of 'p0Intervals' or 'p1Intervals' have an invalid 'start' or 'stop'
    property. 'start' and 'stop'
                  must be between 0 and 1440.

              invalid_interval_start_time_not_increment_of_15
              invalid_interval_stop_time_not_increment_of_15
                  Element(s) of 'p0Intervals' or 'p1Intervals' have an invalid 'start' or 'stop'
    property. 'start' and 'stop'
                  must be an increment of 15.

          invalid_interval_stop_greater_than_or_equal_to_start
              Element(s) of 'p0Intervals' or 'p1Intervals' start property must be less than (and not
    equal) to the stop
              property.

          invalid_interval_temp
              Element(s) of 'p0Intervals' or 'p1Intervals' have and invalid temp property. Temp must be
    between 50
              and 350 inclusive.

          invalid_interval_overlap
              Element(s) of 'p0Intervals' or 'p1Intervals' start/stop times overlap each other. An
    element's 'start' must be
              greater than or equal to the previous element's 'stop'.


      Day errors
            invalid_p0days_length
            invalid_p1days_length
                The request has an invalid 'p0Days' or 'p1Days' property. Its length must always be 7
    (the amount of days
                in a week).

            invalid_p0day_element
            invalid_p1day_element
                The request has an invalid 'p0Days' or 'p1Days' property. Each element must be either
    \"0\" or \"1\".

            invalid_pday_equal
                An element at 'n' in 'p0Days' has the same value as 'p1Days' at index 'n'. Elements at
    the same index must
                not have the same value.

        invalid_p0setback_temp
        invalid_p1setback_temp
                The request has an invalid 'p0SetbackTemp' or 'p1SetbackTemp' property. It's value must
    be between 50
                and 350 inclusive.

        invalid_local_schedule_index
            Invalid 'index' property on 'schedule' property. The index must be between -40 and -1
    inclusive.

        invalid_local_schedule_property
            The request is missing the required 'modeId' property.

        invalid_local_schedule_zone_not_in_module
            The 'zoneId' parameter has an id that does not belong to the specified module.

        invalid_local_schedule_doesnt_belong_to_zone
            The request's schedule has an id that does not belong to the zone.

        invalid_local_schedule_index_mismatch
            The request's schedule has an index which doesn't match it's id.

        invalid_local_schedule_mode_not_in_zone
            The request's modeId does not belong to it's zone.

       Type errors

               invalid_schedule_type
                    Wrong type for schedule property. Schedule must be an object.

                invalid_pinterval_type
                    Wrong type for p0Interval or p1Interval property. p0Interval and p1Interval must be
    arrays of objects.

                invalid_interval_type
                    Wrong type for interval property. Interval must be a object.

                invalid_interval_start_type
                    Wrong type for interval start property. Start must be an integer.

                invalid_interval_stop_type
                    Wrong type for interval stop property. Stop must be an integer.

                invalid_interval_temp_type
                    Wrong type for interval temp property. Temp must be an integer.

                invalid_p0days_type
                    Wrong type for p0Days. p0Days must be an array of strings.

                invalid_p1days_type
                    Wrong type for p1Days. p1Days must be an array of strings.

                invalid_p0day_element_type
                    Wrong type for p0Day element. p0Day elements must be strings.

                invalid_p1day_element_type
                    Wrong type for p1Day element. p1Day elements must be strings.

                invalid_p0setback_temp_type
                    Wrong type for p0SetbackType. p0SetbackType must be an integer.

                invalid_p1setback_temp_type
                    Wrong type for p1SetbackType. p1SetbackType must be an integer.

                invalid_local_schedule_index_type
                    Wrong type for index. Index must be an integer.

                invalid_local_schedule_mode_id_type
                    Wrong type for modeId. modeId must be an integer.

    Args:
        user_id (int):
        module_udid (int):
        zone_id (int):
        body (ZoneSchedules):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ZoneSchedules
     """


    return (await asyncio_detailed(
        user_id=user_id,
module_udid=module_udid,
zone_id=zone_id,
client=client,
body=body,

    )).parsed

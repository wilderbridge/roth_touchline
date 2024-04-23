from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_users_user_id_modules_module_udid_menu_menu_type_menu_type import GetUsersUserIdModulesModuleUdidMenuMenuTypeMenuType



def _get_kwargs(
    user_id: int,
    module_udid: int,
    menu_type: GetUsersUserIdModulesModuleUdidMenuMenuTypeMenuType,

) -> Dict[str, Any]:
    

    

    

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/users/{user_id}/modules/{module_udid}/menu/{menu_type}".format(user_id=user_id,module_udid=module_udid,menu_type=menu_type,),
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
    user_id: int,
    module_udid: int,
    menu_type: GetUsersUserIdModulesModuleUdidMenuMenuTypeMenuType,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Any]:
    r""" Get menu parameters

     ### Valid values:
         (type 1)
                 {
                 \"menuType\": \"MU\",
                 \"type\": 1,
                 \"id\": 2063,
                 \"parentId\": 30002,
                 \"access\": true,
                 \"txtId\": 296,
                 \"wikiTxtId\": 0,
                 \"iconId\": 87,
                 \"params\": {
                     \"format\": 1,
                     \"value\": 10,
                     \"min\": 1,
                     \"max\": 25,
                     \"default\": 0,
                     \"txtId\": 1035,
                     \"description\": \"Number value control\"
                 },
                 \"duringChange\": null
                 {
                   (type 1..5) Value edits Control variants:
                   \"format\" = parameter_type = 1: Normal value
                           parameter_type = 2: value 1/10
                           parameter_type = 3: min: sec
                           parameter_type = 4: hour: min
                           parameter_type = 5: h: min during the day
                   \"value\": current_value
                   \"min\": minimum_value
                   \"max\": max_value
                   \"default\":  default_value
                   \"description\": unit_script_id: from the subtitle database
                   Feedback in the format:
                   [parameter_id, changed_value]

                   (type 6)

                               {
                                   \"menuType\": \"MS\",
                                   \"type\": 6,
                                   \"id\": 30111,
                                   \"parentId\": 0,
                                   \"access\": true,
                                   \"txtId\": 4109,
                                   \"wikiTxtId\": 0,
                                   \"iconId\": 0,
                                   \"params\": {
                                      state: params,
                                      code: params,
                                      stateTxtId: params
                                   },
                                   \"duringChange\": \"f\"
                               },

                   (type 6) Entering code (input)
                   state: light state (0, 1, 2)
                   code: key on the basis of which the code sent to the controller is generated (-1 key
    will not be displayed)
                   stateTxtId: string id for the current state
                   state 0 - default
                   state 1 after entering a valid value
                   state 2 after entering an incorrect value
                   Feedback in the format:
                   [parameter_id, given_code]

                   (type 7)
                    {
                                   \"menuType\": \"MS\",
                                   \"type\": 7,
                                   \"id\": 30111,
                                   \"parentId\": 0,
                                   \"access\": true,
                                   \"txtId\": 4109,
                                   \"wikiTxtId\": 0,
                                   \"iconId\": 0,
                                   \"params\": {
                                       format: type,
                                       remoteReset: params,
                                       value: params
                                       min: params
                                       max: params,
                                       default: params,
                                       type: params,
                                       timeValue: params,
                                       timeMin: params,
                                       timeMax: params,
                                       timeMax: params,
                                       },
                                   \"duringChange\": \"f\"
                               },


                   (type 7) Time mode (temperature + time)
                   format: possibility to delete from the Internet (0 - no, 1 - yes) - a button will be
    displayed, which will be used to send feedback to the controller filled in -1
                   remoteReset:temperature_current_value
                   min:minimum_temperature_value
                   max: temperature_maximum_value
                   default: temperature_default_value
                   type: type-format values table data format
                   timeValue: current_value
                   timeMin: time_minimum_value
                   timeMax: time_maximum_value
                   timeMax: time_default_value
                   Feedback in the format:
                   [parameter_id, temperature_changed_value, time_changed_value]

                   (type 10)
                                {
                                   \"menuType\": \"MI\",
                                   \"type\": 10,
                                   \"id\": 3682,
                                   \"parentId\": 30105,
                                   \"access\": true,
                                   \"txtId\": 953,
                                   \"wikiTxtId\": 0,
                                   \"iconId\": 95,
                                   \"params\": {
                                       \"value\": 0,
                                       \"default\": 0,
                                       \"description\": \"On/Off control\"
                                   },
                                   \"duringChange\": null
                               },


                   (type 10) ON / OFF
                   \"value\": actual_value: 0 or 1
                   \"default\": default_value: 0 or 1
                   Feedback in the format:
                   [parameter_id, changed_value]

                   (type 11)

                               {
                                   \"menuType\": \"MU\",
                                   \"type\": 11,
                                   \"id\": 3350,
                                   \"parentId\": 30040,
                                   \"access\": true,
                                   \"txtId\": 806,
                                   \"wikiTxtId\": 18,
                                   \"iconId\": 13,
                                   \"params\": {
                                       \"value\": 0,
                                       \"default\": 0,
                                       \"options\": [
                                           {
                                               \"txtId\": 922,
                                               \"value\": 0,
                                           },
                                           {
                                               \"txtId\": 818,
                                               \"value\": 1
                                           },
                                           {
                                               \"txtId\": 819,
                                               \"value\": 2
                                           }
                                       ],
                                       \"description\": \"Radio button control\"
                                   },
                                   \"duringChange\": null
                               },


                   (type 11) Choice 1 out of many
                   \"value\": current_value
                   \"default\": default_value
                   \"options\":
                   \"txtId\": text_id
                   \"value\": value
                   Feedback in the format:
                   [parameter_id, changed_value]

                   (type 111)

                                {
                                   \"menuType\": \"MI\",
                                   \"type\": 111,
                                   \"id\": 1000,
                                   \"parentId\": 0,
                                   \"access\": true,
                                   \"txtId\": 814,
                                   \"wikiTxtId\": 0,
                                   \"iconId\": 95,
                                   \"params\": {
                                       \"value\": 0,
                                       \"default\": 0,
                                       \"options\": [
                                           {
                                               \"txtId\": 3109,
                                               \"value\": 0
                                           },
                                           {
                                               \"txtId\": 1401,
                                               \"value\": 1
                                           },
                                           {
                                               \"txtId\": 4324,
                                               \"value\": 2
                                           },
                                           {
                                               \"txtId\": 4325,
                                               \"value\": 3
                                           }
                                       ],
                                       \"description\": \"Zones controller - mode selection\"
                                   },
                                   \"duringChange\": null
                               },

                   (type 111) Selection of strip mode (or other zone controller)
                   \"value\": current_value
                   \"default\":  default_value
                   \"options\": Then the check boxes are sent successively in the following format:
                   \"txtId\": text_id
                   \"value\": value
                   Feedback in the format:
                   [parameter_id, changed_value]

                   (type 112)
                                           {
                                               {
                                               \"menuType\": \"MI\",
                                               \"type\": 112,
                                               \"id\": 1000,
                                               \"parentId\": 0,
                                               \"access\": true,
                                               \"txtId\": 814,
                                               \"wikiTxtId\": 0,
                                               \"iconId\": 95,
                                               \"params\": {
                                                    value: @params[0],
                                                    default: @params,
                                                    options: @params
                                                    {
                                                       txtId: x,
                                                       value: x,
                                                       wikiTxtId: x,
                                                       messageTxtId: x
                                                    }
                                                          },
                                                    description: 'Radio button control expanded'
                                               },
                                               \"duringChange\": null
                                           },



                   (type 112) Selection 1 of many + wiki, message
                   default: current_value
                   options: default_value
                   Then the check boxes are sent successively in the following format:
                   text_id
                   value
                   wiki sub-id (displayed after hovering the cursor over the given option) in the
    absence of -1
                   message_id (displayed after confirming the selection) in the absence of -1
                   Feedback in the format:
                   [parameter_id, changed_value]

                   (type 12)
                                {
                                   \"menuType\": \"MU\",
                                   \"type\": 12,
                                   \"id\": 3002,
                                   \"parentId\": 30056,
                                   \"access\": true,
                                   \"txtId\": 589,
                                   \"wikiTxtId\": 0,
                                   \"iconId\": 13,
                                   \"params\": {
                                       \"dayId\": 1,
                                       \"prevObjId\": 3001,
                                       \"nextObjId\": 3003,
                                       \"valueObjId\": 2060,
                                       \"min\": -10,
                                       \"max\": 10,
                                       \"values\": [],
                                       \"description\": \"Weekly control - temperature correction\"
                                   },
                                   \"duringChange\": null
                               },


                   (type 12) Weekly + -
                   \"dayId\":  day_id: 0-Sunday, 1-Monday, .., 6-Saturday, 7-Mon-Fri, 8-Sat-Sun, 9-Mon-
    Sun
                   \"prevObjId\": previous_day_check_id
                   \"nextObjId\": next_day_check_id
                   \"valueObjId\": corrected_variable_control_ID
                   \"min\": minimum_value
                   \"max\": max_value
                   Then corrections for 24 hours are sent.
                   The values are increased by the minimum (unsigned) value.

                   Feedback in the format:
                   [parameter_id, new_correction_values ...]

                   (type 13)

                               {
                                   \"menuType\": \"MU\",
                                   \"type\": 13,
                                   \"id\": 3377,
                                   \"parentId\": 30070,
                                   \"access\": true,
                                   \"txtId\": 0,
                                   \"wikiTxtId\": 0,
                                   \"iconId\": 13,
                                   \"params\": {
                                       \"dayId\": 1,
                                       \"prevObjId\": 3376,
                                       \"nextObjId\": 3378,
                                       \"value\": 0,
                                       \"default\": 0,
                                       \"noZones\": 48,
                                       \"daySubtitles\": 0,
                                       \"description\": \"Weekly control - on/off\"
                                   },
                                   \"duringChange\": null
                               },


                   (type 13) Weekly on / off
                   \"dayId\": day_id: 0-Sunday, 1-Monday, .., 6-Saturday, 7-Mon-Fri, 8-Sat-Sun, 9-Mon-
    Sun
                   \"prevObjId\": previous_day_check_id
                   \"nextObjId\": next_day_check_id
                   \"value\": number. The youngest bit describes the first zone
                   \"default\": default value (written as above)
                   \"noZones\": number of zones (usually 24 or 48)
                   \"daySubtitles\": \"only own descriptions\" - 0 / none: no, 1: yes = we do not add
    the day strings from the machine (there will be only the one from field [4])
                   Feedback in the format:
                   [parameter_id, changed_value (also in the form of a number)]

                   (type 15)

                               {
                                   \"menuType\": \"MI\",
                                   \"type\": 15,
                                   \"id\": 30856,
                                   \"parentId\": 30751,
                                   \"access\": true,
                                   \"txtId\": 642,
                                   \"wikiTxtId\": 0,
                                   \"iconId\": 98,
                                   \"params\": {
                                       \"value\": 0,
                                       \"default\": 0,
                                       \"options\": [
                                           645,
                                           646,
                                           1333,
                                           1177
                                       ],
                                       \"description\": \"Checkbox control\"
                                   },
                                   \"duringChange\": null
                               }

                   (type 15) Many-of-many selection (ON / OFF set of lamps)
                   \"value\": current_value as a number (the youngest bit specifies the first field,
    etc.)
                   \"default\": default_value (as above)
                   Then the data of individual fields is sent in the form of:
                   \"options\": text_id
                   Feedback in the format:
                   [parameter_id, changed_value (also in the form of a number)]

                   (type 20)

                               {
                                   \"menuType\": \"MU\",
                                   \"type\": 20,
                                   \"id\": 8333,
                                   \"parentId\": 30068,
                                   \"access\": true,
                                   \"txtId\": 839,
                                   \"wikiTxtId\": 0,
                                   \"iconId\": 14,
                                   \"params\": {
                                       \"txtId\": 838,
                                       \"type\": 1,
                                       \"value\": -1,
                                       \"blockHide\": 0,
                                       \"description\": \"Dialogue control - Yes/No\"
                                   },
                                   \"duringChange\": null
                               },


                   (type 20) Dialog (Firing up, disinfecting etc.)
                   \"txtId\": notification string id
                   \"type\": dialogue type:
                   0 dialog with OK button + control closing button,
                   1 YES / NO dialogue + light closing button,
                   2 info with cancel button
                   \"value\":selected value (when the parameter was changed from the controller)
                   \"blockHide\": turning off the hiding of the indicator after sending the parameter 1
    - YES, 0 / none - NO
                   Feedback in the format:

                   parameter_id, return value:
                   for type 0: (2 after confirmation of the dialogue
                   for type 1: (1 means YES, (0 means NO
                   for type 2: (Cancellation 3 after

                   (type 29)

                                           {
                                               {
                                               \"menuType\": \"MI\",
                                               \"type\": 29,
                                               \"id\": 1000,
                                               \"parentId\": 0,
                                               \"access\": true,
                                               \"txtId\": 814,
                                               \"wikiTxtId\": 0,
                                               \"iconId\": 95,
                                               \"params\": {
                                                   slope: param
                                                   slopeMin: param
                                                   slopeMax: param
                                                   shift: param
                                                   shiftMin: param
                                                   shiftMax: param
                                                   setTemp: param
                                                   externalTemp: param
                                                   resultingTemperatureMin: param
                                                   resultingTemperatureMax: param
                                                   constant1:  params
                                                   constant2:  params
                                                   constant3:  params
                                                   constant4:  params
                                                   constant5:  params
                                                   patternId: params
                                                   xMin: params
                                                   xMax: params
                                                   yMin: params
                                                   yMax: params
                                                   },
                                               \"duringChange\": null
                                           },

                   (type 29) Heating curve offset / slope - Viessmann
                   slope: slope * 10
                   slopeMin: min slope * 10
                   slopeMax: maximum slope * 10
                   shift: shift
                   shiftMin: min. Change
                   shiftMax: maximum change
                   setTemp: set room temperature * 10
                   resultingTemperatureMin: outdoor temperature * 10
                   resultingTemperatureMax: min of the set of results
                   constant1: max of the result set
                   constant2: the constant 1 * 100
                   constant3: the constant 2 * 100
                   constant4: the constant 3 * 100
                   constant5: constant 4 * 100
                   patternId: the constant 5 * 100
                   xMin:  pattern id (in the absence of -1, default pattern id 0)
                   xMax: point X min (in the absence of -1)
                   yMin: point X max (in the absence of -1)
                   yMax: point Y min (in the absence of -1)
                   \"duringChange\": point Y max (in the absence of -1)
                   Patterns:
                   (0) result = (Constant_1 * curve_lope) * (set_room_temperature ^ (outdoor_temperature
    / (Constant_2 - (outdoor_temperature * Constant_3)))) * ((Constant_4 - outdoor_temperature) *
    Constant_5) + set_temperature_offset;
                   Feedback in the format:
                   [parameter_id, slope, offset]

                   (type 30)

                                {
                                   \"menuType\": \"MI\",
                                   \"type\": 30,
                                   \"id\": 2217,
                                   \"parentId\": 30144,
                                   \"access\": true,
                                   \"txtId\": 342,
                                   \"wikiTxtId\": 0,
                                   \"iconId\": 0,
                                   \"params\": {
                                       \"min\": 20,
                                       \"max\": 70,
                                       \"points\": [
                                           {
                                               \"value\": 60,
                                               \"default\": 60,
                                               \"position\": -20
                                           },
                                           {
                                               \"value\": 55,
                                               \"default\": 55,
                                               \"position\": -10
                                           },
                                           {
                                               \"value\": 50,
                                               \"default\": 50,
                                               \"position\": 0
                                           },
                                           {
                                               \"value\": 45,
                                               \"default\": 45,
                                               \"position\": 10
                                           }
                                       ],
                                       \"description\": \"Heating Curve with points\"
                                   },
                                   \"duringChange\": null
                               },


                   (type 30) Heat curve
                   \"min\": minimum_value
                   \"max\": max_value
                   \"points\": Then the data of individual points on the curve are sent in the form of:
                   \"value\": edited_value (Y)
                   \"default\": default_value (Y)
                   \"position\": location_in_osi_X
                   Feedback in the format:
                   [parameter_id, edited values ...]

                   (type 31)


                                               {
                                               \"menuType\": \"MI\",
                                               \"type\": 31,
                                               \"id\": 1000,
                                               \"parentId\": 0,
                                               \"access\": true,
                                               \"txtId\": 814,
                                               \"wikiTxtId\": 0,
                                               \"iconId\": 95,
                                               \"params\": {
                                                  slope: @params
                                                  minSlope: params
                                                  maxSlope: params
                                                  defaultSlope: params
                                                  shift: params
                                                  minShift: params
                                                  maxShift: params
                                                  defaultShift: params
                                                  maxValue: params
                                                  description: 'Heating Curve Shift/Slope'
                                           },


                   (type 31) Heating curve slope / offset
                   slope: slope * 10
                   minSlope:min slope * 10
                   maxSlope: maximum slope * 10
                   defaultSlope:  default slope * 10
                   shift: offset * 10
                   minShift:  min. Change * 10
                   maxShift: maximum offset * 10
                   defaultShift: default offset * 10
                   maxValue: set max * 10: the curve is limited to this value (above it will be
    \"broken\" at this level)
                   Feedback in the format:
                   [parameter_id, slope, offset]

                   z = n * (((20 + p) - ts) + (20 + p))

                   where:
                   z - set temperature
                   n - the slope of the curve
                   ts - average outside temperature
                   p - shift (par)

                   (type 32)

                               {
                                   \"menuType\": \"MS\",
                                   \"type\": 32,
                                   \"id\": 30111,
                                   \"parentId\": 0,
                                   \"access\": true,
                                   \"txtId\": 4109,
                                   \"wikiTxtId\": 0,
                                   \"iconId\": 0,
                                   \"params\": {
                                       \"groupCode\": null
                                   },
                                   \"duringChange\": \"f\"
                               },

                   (type 32) Administration / Statistics group
                   \"groupCode\": Control - trigger to enter the identifier / name / code of the group
    for collective statistics of many
                    controllers (eg Preview of energy yields for the entire commune). Basically an
    option only available on the Internet.
                    Needed for unambiguous identification that the controller supports statistics in the
    form of statuses + release
                    of the form for adding modules to the account with redundant options. We assume that
    it should be in the INSTALLER MENU

                   (type 35)

                               {
                                   \"menuType\": \"MI\",
                                   \"type\": 35,
                                   \"id\": 30090,
                                   \"parentId\": 0,
                                   \"access\": true,
                                   \"txtId\": 2459,
                                   \"wikiTxtId\": 0,
                                   \"iconId\": 95,
                                   \"params\": {
                                       \"password\": [
                                           \"1410\"
                                       ],
                                       \"description\": \"Menu password\"
                                   },
                                   \"duringChange\": \"f\"
                               },

                   (type 35) Password
                   \"password\": password to access the submenu

                   (type 36)

                               {
                                   \"menuType\": \"MI\",
                                   \"type\": 36,
                                   \"id\": 30090,
                                   \"parentId\": 0,
                                   \"access\": true,
                                   \"txtId\": 2459,
                                   \"wikiTxtId\": 0,
                                   \"iconId\": 95,
                                   \"params\": {
                                      txt: params,
                                      value: params,
                                      type: params,
                                      unit: params,
                                      activity: params
                                   },
                                   \"duringChange\": \"f\"
                               },

                   (type 36) Display service parameters (not used)
                   txt: Parameter string 1 identifier
                   value: value of 1 parameter
                   type: parameter value type 1
                   unit: Parameter unit 1 ID
                   activity: the activity of the 1st parameter (should it be e.g. bold)
                   \"duringChange\": parameter string identifier 2
                   [13] ...
                   value type = 0: Normal value.
                   value type = 1: value in seconds.
                   value type = 2: minute value.
                   value type = 3: hourly value.
                   value type = 4: decimal value.
                   value type = 5: hundredth value.

                   (type 40)
                               {
                                   \"menuType\": \"MI\",
                                   \"type\": 40,
                                   \"id\": 30090,
                                   \"parentId\": 0,
                                   \"access\": true,
                                   \"txtId\": 2459,
                                   \"wikiTxtId\": 0,
                                   \"iconId\": 95,
                                   \"params\": {
                                      txt: params,
                                      value: params,
                                      type: params,
                                      unit: params,
                                      activity: params
                                   },
                                   \"duringChange\": \"f\"
                               },

                   :description => 'Text information',
                             :statusId => @params[0],
                             :headerId => @params[1],
                             :iconId => @params[2],
                             options: @params[3..-1]
                   (type 40) Duplicate menu item:
                   :description  parameter_id (unique)
                   :statusId Parent_ID
                   :headerIdparameter_type
                   :iconId visibility
                   options: identifier of the copied item

                   (type 45)

                                {
                                   \"menuType\": \"MU\",
                                   \"type\": 45,
                                   \"id\": 20008,
                                   \"parentId\": 30011,
                                   \"access\": true,
                                   \"txtId\": 2447,
                                   \"wikiTxtId\": 0,
                                   \"iconId\": 149,
                                   \"params\": {
                                       \"noCols\": 4,
                                       \"noRows\": 0,
                                       \"colsDef\": [
                                           {
                                               \"idSubtitle\": 1106,
                                               \"type\": 24
                                           },
                                           {
                                               \"idSubtitle\": 1352,
                                               \"type\": 16
                                           },
                                           {
                                               \"idSubtitle\": 2437,
                                               \"type\": 6
                                           },
                                           {
                                               \"idSubtitle\": 2438,
                                               \"type\": 6
                                           }
                                       ],
                                       \"rowsData\": [],
                                       \"description\": \"Data table\"
                                   },
                                   \"duringChange\": \"f\"
                               },

                   (type 45) Data table
                   \"noCols\": number of columns
                   \"noRows\": number of significant lines (more can be sent, but only the first ...
    will be displayed)
                   \"colsDef\": column_identifier_scription
                   \"type\": column_type k

                   (type 46)

                               {
                                   \"menuType\": \"MU\",
                                   \"type\": 46,
                                   \"id\": 20007,
                                   \"parentId\": 30011,
                                   \"access\": true,
                                   \"txtId\": 2446,
                                   \"wikiTxtId\": 0,
                                   \"iconId\": 147,
                                   \"params\": {
                                       \"noCols\": 2,
                                       \"noRows\": 6,
                                       \"colsDef\": [
                                           2718,
                                           2719
                                       ],
                                       \"rowsData\": [
                                           [
                                               {
                                                   \"value\": 2983,
                                                   \"type\": 18
                                               },
                                               {
                                                   \"value\": 102,
                                                   \"type\": 29
                                               }
                                           ],
                                           [
                                               {
                                                   \"value\": 1236,
                                                   \"type\": 18
                                               },
                                               {
                                                   \"value\": 99,
                                                   \"type\": 19
                                               }
                                           ],
                                           [
                                               {
                                                   \"value\": 1237,
                                                   \"type\": 18
                                               },
                                               {
                                                   \"value\": 100,
                                                   \"type\": 11
                                               }
                                           ],
                                           [
                                               {
                                                   \"value\": 1739,
                                                   \"type\": 18
                                               },
                                               {
                                                   \"value\": 100,
                                                   \"type\": 11
                                               }
                                           ],
                                           [
                                               {
                                                   \"value\": 1740,
                                                   \"type\": 18
                                               },
                                               {
                                                   \"value\": 0,
                                                   \"type\": 11
                                               }
                                           ],
                                           [
                                               {
                                                   \"value\": 2982,
                                                   \"type\": 18
                                               },
                                               {
                                                   \"value\": 110,
                                                   \"type\": 11
                                               }
                                           ]
                                       ],
                                       \"description\": \"Data table with different rows\"
                                   },
                                   \"duringChange\": \"f\"
                               },

                   (type 46) Data table - non-uniform rows
                   \"noCols\": number of columns
                   \"noRows\":  number of significant lines (more can be sent, but only the first will
    be shown)
                   \"colsDef\":  column headings (subtitle identifier)
                   \"rowsData\":  pairs: value, id value type

                   (type 50)

                               {
                                   \"menuType\": \"MU\",
                                   \"type\": 50,
                                   \"id\": 501,
                                   \"parentId\": 0,
                                   \"access\": true,
                                   \"txtId\": 265,
                                   \"wikiTxtId\": 0,
                                   \"iconId\": 0,
                                   \"params\": {
                                       \"manufacturerParentId\": 500,
                                       \"description\": \"Manufacturers screen\"
                                   },
                                   \"duringChange\": \"f\"
                               },

                   (type 50) Manufacturer's screen
                   After the \"^\" character, the identifier of the parent element of the manufacturer's
    screen parameters group is connected;

                   \"manufacturerParentId\": id text
                   \"description\": description
                   It collects various data / parameters in one common \"view\". Refresh every 3
    seconds. The menu option is just a display trigger, the data itself comes in a separate package: EP

                   (type 100)

                               {
                                   \"menuType\": \"MU\",
                                   \"type\": 100,
                                   \"id\": 17,
                                   \"parentId\": 30023,
                                   \"access\": true,
                                   \"txtId\": 444,
                                   \"wikiTxtId\": 0,
                                   \"iconId\": 74,
                                   \"params\": {
                                       \"dayId\": 0,
                                       \"prevObjId\": 23,
                                       \"nextObjId\": 18,
                                       \"type\": 0,
                                       \"step\": 1,
                                       \"numRows\": 5,
                                       \"numCols\": 1,
                                       \"cols\": [
                                           {
                                               \"txtId\": 1163,
                                               \"min\": 0,
                                               \"max\": 1,
                                               \"interval\": 1,
                                               \"type\": 29
                                           }
                                       ],
                                       \"rows\": [
                                           {
                                               \"startTime\": 0,
                                               \"defaultStartTime\": 0,
                                               \"endTime\": 0,
                                               \"defaultEndTime\": 0,
                                               \"valueFirstColumn\": 0,
                                               \"defaultFirstColumn\": 0,
                                               \"valueSecondColumn\": 0,
                                               \"defaultSecondColumn\": 0
                                           },
                                           {
                                               \"startTime\": 0,
                                               \"defaultStartTime\": 0,
                                               \"endTime\": 0,
                                               \"defaultEndTime\": 0,
                                               \"valueFirstColumn\": 0,
                                               \"defaultFirstColumn\": 0,
                                               \"valueSecondColumn\": 0,
                                               \"defaultSecondColumn\": 0
                                           },
                                           {
                                               \"startTime\": 0,
                                               \"defaultStartTime\": 0,
                                               \"endTime\": 0,
                                               \"defaultEndTime\": 0,
                                               \"valueFirstColumn\": 0,
                                               \"defaultFirstColumn\": 0,
                                               \"valueSecondColumn\": 0,
                                               \"defaultSecondColumn\": 0
                                           },
                                           {
                                               \"startTime\": 0,
                                               \"defaultStartTime\": 0,
                                               \"endTime\": 0,
                                               \"defaultEndTime\": 0,
                                               \"valueFirstColumn\": 0,
                                               \"defaultFirstColumn\": 0,
                                               \"valueSecondColumn\": 0,
                                               \"defaultSecondColumn\": 0
                                           },
                                           {
                                               \"startTime\": 0,
                                               \"defaultStartTime\": 0,
                                               \"endTime\": 0,
                                               \"defaultEndTime\": 0,
                                               \"valueFirstColumn\": 0,
                                               \"defaultFirstColumn\": 0,
                                               \"valueSecondColumn\": null,
                                               \"defaultSecondColumn\": null
                                           }
                                       ],
                                       \"description\": \"Weekly control -recuperator\"
                                   },
                                   \"duringChange\": \"f\"
                               },

                   (type 100) Universal schedule
                   \"dayId\" day_id: 0-Sunday, 1-Monday, .., 6-Saturday, 7-Mon-Fri, 8-Sat-Sun, 9-Mon-Sun
                   \"prevObjId\": previous_day_check_id
                   \"nextObjId\": next_day_check_id
                   \"type\": schedule type
                   \"step\": scheduling step in minutes
                   \"numRows\": number of lines
                   numCols\": number of additional columns
                   Then general information about the additional columns is sent.
                   Each column is described by 5 values:
                   \"cols\":
                   \"txtId\":  text ID
                   \"min\": minimum value
                   \"max\": maximum value
                   \"interval\": jump value
                   \"type\": value type (Invisible value (-1) hides the column)
                   Then detailed information about the values of each row is sent.
                   Each field is described by (2 + number of additional columns) value:
                   \"rows\":
                   \"startTime\": start time in minutes
                   \"defaultStartTime\": default start time in minutes
                   \"endTime\": end time in minutes
                   \"defaultEndTime\": default end time in minutes
                   \"valueSecondColumn\": value for the first column ...
                   \"defaultSecondColumn\": default value for the first column ...

                   (type 106)

                               {
                                   \"menuType\": \"MI\",
                                   \"type\": 106,
                                   \"id\": 2325,
                                   \"parentId\": 30127,
                                   \"access\": true,
                                   \"txtId\": 6518,
                                   \"wikiTxtId\": 0,
                                   \"iconId\": 209,
                                   \"params\": {
                                       \"value\": 0,
                                       \"min\": -1000,
                                       \"max\": 0,
                                       \"default\": -100,
                                       \"txtId\": 0,
                                       \"format\": 0,
                                       \"jump\": 1,
                                       \"description\": \"Universal value control\"
                                   },
                                   \"duringChange\": \"f\"
                               },

                   (type 106) Universal value editing
                   it will be able to replace 1..5 and handle several (dozen) others

                   \"value\": current_value
                   \"min\": minimum_value
                   max\":max_value
                   \"default\": default_value
                   \"txtId\": unit_script_id: from the subtitle database (in some cases it may not be
    applicable)
                   \"format\": type-format values table data format
                   \"jump\": step in value change (in the absence of = 1)
                   Feedback in the format:
                   [parameter_id, changed_value]

                   (type 107)

                               {
                                   \"menuType\": \"MU\",
                                   \"type\": 107,
                                   \"id\": 1004,
                                   \"parentId\": 0,
                                   \"access\": true,
                                   \"txtId\": 1106,
                                   \"wikiTxtId\": 0,
                                   \"iconId\": 77,
                                   \"params\": {
                                       \"day\": 20,
                                       \"month\": 4,
                                       \"year\": 2021,
                                       \"description\": \"Date control\"
                                   },
                                   \"duringChange\": \"f\"
                               },

                   (type 107) Date edit
                   \"day\": current_value days
                   \"month\"current_value_months
                   \"year\": current_value_year
                   Feedback in the format:
                   [parameter_id, changed_value_days, changed_value_months, changed_value_years]

                   (type 108)

                               {
                                   \"menuType\": \"MU\",
                                   \"type\": 108,
                                   \"id\": 3021,
                                   \"parentId\": 0,
                                   \"access\": true,
                                   \"txtId\": 4363,
                                   \"wikiTxtId\": 0,
                                   \"iconId\": 6,
                                   \"params\": {
                                       \"remoteReset\": true,
                                       \"startDay\": -1,
                                       \"startMonth\": -1,
                                       \"startYear\": -1,
                                       \"endDay\": -1,
                                       \"endMonth\": -1,
                                       \"endYear\": -1,
                                       \"description\": \"Date control\"
                                   },
                                   \"duringChange\": null
                               },

                   (type 108) Edition of the range (date from - date to)
                   \"remoteReset\":  possibility to delete from the Internet (0 - no, 1 - yes) - a
    button will be displayed, which will be used to send feedback to the controller filled in -1
                   \"startDay\": value_days_beginning
                   \"startMonth\": value_month_start
                    \"startYear\": value_year_beginning
                   \"endDay\": value_days_end
                   \"endMonth\": value_month_end
                   \"description\": value_year_end
                   Feedback in the format:
                   ]


                   (type 120) Viessmann schedule¶
                               {
                                   \"menuType\": \"MU\",
                                   \"type\": 120,
                                   \"id\": 3001,
                                   \"parentId\": 0,
                                   \"access\": true,
                                   \"txtId\": 4362,
                                   \"wikiTxtId\": 0,
                                   \"iconId\": 13,
                                   \"params\": {
                                       \"type\": \"0\",
                                       \"days\": [
                                           [
                                               {
                                                   \"start\": 360,
                                                   \"end\": 1320
                                               },
                                               {
                                                   \"start\": -1,
                                                   \"end\": -1
                                               },
                                               {
                                                   \"start\": -1,
                                                   \"end\": -1
                                               },
                                               {
                                                   \"start\": -1,
                                                   \"end\": -1
                                               }
                                           ],
                                           [
                                               {
                                                   \"start\": 360,
                                                   \"end\": 1320
                                               },
                                               {
                                                   \"start\": -1,
                                                   \"end\": -1
                                               },
                                               {
                                                   \"start\": -1,
                                                   \"end\": -1
                                               },
                                               {
                                                   \"start\": -1,
                                                   \"end\": -1
                                               }
                                           ],
                                           [
                                               {
                                                   \"start\": 360,
                                                   \"end\": 1320
                                               },
                                               {
                                                   \"start\": -1,
                                                   \"end\": -1
                                               },
                                               {
                                                   \"start\": -1,
                                                   \"end\": -1
                                               },
                                               {
                                                   \"start\": -1,
                                                   \"end\": -1
                                               }
                                           ],
                                           [
                                               {
                                                   \"start\": 360,
                                                   \"end\": 1320
                                               },
                                               {
                                                   \"start\": -1,
                                                   \"end\": -1
                                               },
                                               {
                                                   \"start\": -1,
                                                   \"end\": -1
                                               },
                                               {
                                                   \"start\": -1,
                                                   \"end\": -1
                                               }
                                           ],
                                           [
                                               {
                                                   \"start\": 360,
                                                   \"end\": 1320
                                               },
                                               {
                                                   \"start\": -1,
                                                   \"end\": -1
                                               },
                                               {
                                                   \"start\": -1,
                                                   \"end\": -1
                                               },
                                               {
                                                   \"start\": -1,
                                                   \"end\": -1
                                               }
                                           ],
                                           [
                                               {
                                                   \"start\": 360,
                                                   \"end\": 1320
                                               },
                                               {
                                                   \"start\": -1,
                                                   \"end\": -1
                                               },
                                               {
                                                   \"start\": -1,
                                                   \"end\": -1
                                               },
                                               {
                                                   \"start\": -1,
                                                   \"end\": -1
                                               }
                                           ],
                                           [
                                               {
                                                   \"start\": 360,
                                                   \"end\": 1320
                                               },
                                               {
                                                   \"start\": -1,
                                                   \"end\": -1
                                               },
                                               {
                                                   \"start\": -1,
                                                   \"end\": -1
                                               },
                                               {
                                                   \"start\": -1,
                                                   \"end\": -1
                                               }
                                           ]
                                       ]
                                   },
                                   \"duringChange\": null
                               },

                   \"type\": \"0\", type of schedule
                   \"start\": regular schedule,
                   \"end\": DHW schedule

                    Then schedule 7 days separated by # on each day 8 parameters (4 pairs start and end
    in minutes) where the higher temperature will be applied.

                    # Mon # Tue # ... #Sun. - individual days separated by \"#\"
                    # [0] .. [7] # - 4 pairs of ranges in the absence of -1 e.g. # 240,600,720,860, -1,
    -1, -1, -1 #

    Args:
        user_id (int):
        module_udid (int):
        menu_type (GetUsersUserIdModulesModuleUdidMenuMenuTypeMenuType):

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

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    user_id: int,
    module_udid: int,
    menu_type: GetUsersUserIdModulesModuleUdidMenuMenuTypeMenuType,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Any]:
    r""" Get menu parameters

     ### Valid values:
         (type 1)
                 {
                 \"menuType\": \"MU\",
                 \"type\": 1,
                 \"id\": 2063,
                 \"parentId\": 30002,
                 \"access\": true,
                 \"txtId\": 296,
                 \"wikiTxtId\": 0,
                 \"iconId\": 87,
                 \"params\": {
                     \"format\": 1,
                     \"value\": 10,
                     \"min\": 1,
                     \"max\": 25,
                     \"default\": 0,
                     \"txtId\": 1035,
                     \"description\": \"Number value control\"
                 },
                 \"duringChange\": null
                 {
                   (type 1..5) Value edits Control variants:
                   \"format\" = parameter_type = 1: Normal value
                           parameter_type = 2: value 1/10
                           parameter_type = 3: min: sec
                           parameter_type = 4: hour: min
                           parameter_type = 5: h: min during the day
                   \"value\": current_value
                   \"min\": minimum_value
                   \"max\": max_value
                   \"default\":  default_value
                   \"description\": unit_script_id: from the subtitle database
                   Feedback in the format:
                   [parameter_id, changed_value]

                   (type 6)

                               {
                                   \"menuType\": \"MS\",
                                   \"type\": 6,
                                   \"id\": 30111,
                                   \"parentId\": 0,
                                   \"access\": true,
                                   \"txtId\": 4109,
                                   \"wikiTxtId\": 0,
                                   \"iconId\": 0,
                                   \"params\": {
                                      state: params,
                                      code: params,
                                      stateTxtId: params
                                   },
                                   \"duringChange\": \"f\"
                               },

                   (type 6) Entering code (input)
                   state: light state (0, 1, 2)
                   code: key on the basis of which the code sent to the controller is generated (-1 key
    will not be displayed)
                   stateTxtId: string id for the current state
                   state 0 - default
                   state 1 after entering a valid value
                   state 2 after entering an incorrect value
                   Feedback in the format:
                   [parameter_id, given_code]

                   (type 7)
                    {
                                   \"menuType\": \"MS\",
                                   \"type\": 7,
                                   \"id\": 30111,
                                   \"parentId\": 0,
                                   \"access\": true,
                                   \"txtId\": 4109,
                                   \"wikiTxtId\": 0,
                                   \"iconId\": 0,
                                   \"params\": {
                                       format: type,
                                       remoteReset: params,
                                       value: params
                                       min: params
                                       max: params,
                                       default: params,
                                       type: params,
                                       timeValue: params,
                                       timeMin: params,
                                       timeMax: params,
                                       timeMax: params,
                                       },
                                   \"duringChange\": \"f\"
                               },


                   (type 7) Time mode (temperature + time)
                   format: possibility to delete from the Internet (0 - no, 1 - yes) - a button will be
    displayed, which will be used to send feedback to the controller filled in -1
                   remoteReset:temperature_current_value
                   min:minimum_temperature_value
                   max: temperature_maximum_value
                   default: temperature_default_value
                   type: type-format values table data format
                   timeValue: current_value
                   timeMin: time_minimum_value
                   timeMax: time_maximum_value
                   timeMax: time_default_value
                   Feedback in the format:
                   [parameter_id, temperature_changed_value, time_changed_value]

                   (type 10)
                                {
                                   \"menuType\": \"MI\",
                                   \"type\": 10,
                                   \"id\": 3682,
                                   \"parentId\": 30105,
                                   \"access\": true,
                                   \"txtId\": 953,
                                   \"wikiTxtId\": 0,
                                   \"iconId\": 95,
                                   \"params\": {
                                       \"value\": 0,
                                       \"default\": 0,
                                       \"description\": \"On/Off control\"
                                   },
                                   \"duringChange\": null
                               },


                   (type 10) ON / OFF
                   \"value\": actual_value: 0 or 1
                   \"default\": default_value: 0 or 1
                   Feedback in the format:
                   [parameter_id, changed_value]

                   (type 11)

                               {
                                   \"menuType\": \"MU\",
                                   \"type\": 11,
                                   \"id\": 3350,
                                   \"parentId\": 30040,
                                   \"access\": true,
                                   \"txtId\": 806,
                                   \"wikiTxtId\": 18,
                                   \"iconId\": 13,
                                   \"params\": {
                                       \"value\": 0,
                                       \"default\": 0,
                                       \"options\": [
                                           {
                                               \"txtId\": 922,
                                               \"value\": 0,
                                           },
                                           {
                                               \"txtId\": 818,
                                               \"value\": 1
                                           },
                                           {
                                               \"txtId\": 819,
                                               \"value\": 2
                                           }
                                       ],
                                       \"description\": \"Radio button control\"
                                   },
                                   \"duringChange\": null
                               },


                   (type 11) Choice 1 out of many
                   \"value\": current_value
                   \"default\": default_value
                   \"options\":
                   \"txtId\": text_id
                   \"value\": value
                   Feedback in the format:
                   [parameter_id, changed_value]

                   (type 111)

                                {
                                   \"menuType\": \"MI\",
                                   \"type\": 111,
                                   \"id\": 1000,
                                   \"parentId\": 0,
                                   \"access\": true,
                                   \"txtId\": 814,
                                   \"wikiTxtId\": 0,
                                   \"iconId\": 95,
                                   \"params\": {
                                       \"value\": 0,
                                       \"default\": 0,
                                       \"options\": [
                                           {
                                               \"txtId\": 3109,
                                               \"value\": 0
                                           },
                                           {
                                               \"txtId\": 1401,
                                               \"value\": 1
                                           },
                                           {
                                               \"txtId\": 4324,
                                               \"value\": 2
                                           },
                                           {
                                               \"txtId\": 4325,
                                               \"value\": 3
                                           }
                                       ],
                                       \"description\": \"Zones controller - mode selection\"
                                   },
                                   \"duringChange\": null
                               },

                   (type 111) Selection of strip mode (or other zone controller)
                   \"value\": current_value
                   \"default\":  default_value
                   \"options\": Then the check boxes are sent successively in the following format:
                   \"txtId\": text_id
                   \"value\": value
                   Feedback in the format:
                   [parameter_id, changed_value]

                   (type 112)
                                           {
                                               {
                                               \"menuType\": \"MI\",
                                               \"type\": 112,
                                               \"id\": 1000,
                                               \"parentId\": 0,
                                               \"access\": true,
                                               \"txtId\": 814,
                                               \"wikiTxtId\": 0,
                                               \"iconId\": 95,
                                               \"params\": {
                                                    value: @params[0],
                                                    default: @params,
                                                    options: @params
                                                    {
                                                       txtId: x,
                                                       value: x,
                                                       wikiTxtId: x,
                                                       messageTxtId: x
                                                    }
                                                          },
                                                    description: 'Radio button control expanded'
                                               },
                                               \"duringChange\": null
                                           },



                   (type 112) Selection 1 of many + wiki, message
                   default: current_value
                   options: default_value
                   Then the check boxes are sent successively in the following format:
                   text_id
                   value
                   wiki sub-id (displayed after hovering the cursor over the given option) in the
    absence of -1
                   message_id (displayed after confirming the selection) in the absence of -1
                   Feedback in the format:
                   [parameter_id, changed_value]

                   (type 12)
                                {
                                   \"menuType\": \"MU\",
                                   \"type\": 12,
                                   \"id\": 3002,
                                   \"parentId\": 30056,
                                   \"access\": true,
                                   \"txtId\": 589,
                                   \"wikiTxtId\": 0,
                                   \"iconId\": 13,
                                   \"params\": {
                                       \"dayId\": 1,
                                       \"prevObjId\": 3001,
                                       \"nextObjId\": 3003,
                                       \"valueObjId\": 2060,
                                       \"min\": -10,
                                       \"max\": 10,
                                       \"values\": [],
                                       \"description\": \"Weekly control - temperature correction\"
                                   },
                                   \"duringChange\": null
                               },


                   (type 12) Weekly + -
                   \"dayId\":  day_id: 0-Sunday, 1-Monday, .., 6-Saturday, 7-Mon-Fri, 8-Sat-Sun, 9-Mon-
    Sun
                   \"prevObjId\": previous_day_check_id
                   \"nextObjId\": next_day_check_id
                   \"valueObjId\": corrected_variable_control_ID
                   \"min\": minimum_value
                   \"max\": max_value
                   Then corrections for 24 hours are sent.
                   The values are increased by the minimum (unsigned) value.

                   Feedback in the format:
                   [parameter_id, new_correction_values ...]

                   (type 13)

                               {
                                   \"menuType\": \"MU\",
                                   \"type\": 13,
                                   \"id\": 3377,
                                   \"parentId\": 30070,
                                   \"access\": true,
                                   \"txtId\": 0,
                                   \"wikiTxtId\": 0,
                                   \"iconId\": 13,
                                   \"params\": {
                                       \"dayId\": 1,
                                       \"prevObjId\": 3376,
                                       \"nextObjId\": 3378,
                                       \"value\": 0,
                                       \"default\": 0,
                                       \"noZones\": 48,
                                       \"daySubtitles\": 0,
                                       \"description\": \"Weekly control - on/off\"
                                   },
                                   \"duringChange\": null
                               },


                   (type 13) Weekly on / off
                   \"dayId\": day_id: 0-Sunday, 1-Monday, .., 6-Saturday, 7-Mon-Fri, 8-Sat-Sun, 9-Mon-
    Sun
                   \"prevObjId\": previous_day_check_id
                   \"nextObjId\": next_day_check_id
                   \"value\": number. The youngest bit describes the first zone
                   \"default\": default value (written as above)
                   \"noZones\": number of zones (usually 24 or 48)
                   \"daySubtitles\": \"only own descriptions\" - 0 / none: no, 1: yes = we do not add
    the day strings from the machine (there will be only the one from field [4])
                   Feedback in the format:
                   [parameter_id, changed_value (also in the form of a number)]

                   (type 15)

                               {
                                   \"menuType\": \"MI\",
                                   \"type\": 15,
                                   \"id\": 30856,
                                   \"parentId\": 30751,
                                   \"access\": true,
                                   \"txtId\": 642,
                                   \"wikiTxtId\": 0,
                                   \"iconId\": 98,
                                   \"params\": {
                                       \"value\": 0,
                                       \"default\": 0,
                                       \"options\": [
                                           645,
                                           646,
                                           1333,
                                           1177
                                       ],
                                       \"description\": \"Checkbox control\"
                                   },
                                   \"duringChange\": null
                               }

                   (type 15) Many-of-many selection (ON / OFF set of lamps)
                   \"value\": current_value as a number (the youngest bit specifies the first field,
    etc.)
                   \"default\": default_value (as above)
                   Then the data of individual fields is sent in the form of:
                   \"options\": text_id
                   Feedback in the format:
                   [parameter_id, changed_value (also in the form of a number)]

                   (type 20)

                               {
                                   \"menuType\": \"MU\",
                                   \"type\": 20,
                                   \"id\": 8333,
                                   \"parentId\": 30068,
                                   \"access\": true,
                                   \"txtId\": 839,
                                   \"wikiTxtId\": 0,
                                   \"iconId\": 14,
                                   \"params\": {
                                       \"txtId\": 838,
                                       \"type\": 1,
                                       \"value\": -1,
                                       \"blockHide\": 0,
                                       \"description\": \"Dialogue control - Yes/No\"
                                   },
                                   \"duringChange\": null
                               },


                   (type 20) Dialog (Firing up, disinfecting etc.)
                   \"txtId\": notification string id
                   \"type\": dialogue type:
                   0 dialog with OK button + control closing button,
                   1 YES / NO dialogue + light closing button,
                   2 info with cancel button
                   \"value\":selected value (when the parameter was changed from the controller)
                   \"blockHide\": turning off the hiding of the indicator after sending the parameter 1
    - YES, 0 / none - NO
                   Feedback in the format:

                   parameter_id, return value:
                   for type 0: (2 after confirmation of the dialogue
                   for type 1: (1 means YES, (0 means NO
                   for type 2: (Cancellation 3 after

                   (type 29)

                                           {
                                               {
                                               \"menuType\": \"MI\",
                                               \"type\": 29,
                                               \"id\": 1000,
                                               \"parentId\": 0,
                                               \"access\": true,
                                               \"txtId\": 814,
                                               \"wikiTxtId\": 0,
                                               \"iconId\": 95,
                                               \"params\": {
                                                   slope: param
                                                   slopeMin: param
                                                   slopeMax: param
                                                   shift: param
                                                   shiftMin: param
                                                   shiftMax: param
                                                   setTemp: param
                                                   externalTemp: param
                                                   resultingTemperatureMin: param
                                                   resultingTemperatureMax: param
                                                   constant1:  params
                                                   constant2:  params
                                                   constant3:  params
                                                   constant4:  params
                                                   constant5:  params
                                                   patternId: params
                                                   xMin: params
                                                   xMax: params
                                                   yMin: params
                                                   yMax: params
                                                   },
                                               \"duringChange\": null
                                           },

                   (type 29) Heating curve offset / slope - Viessmann
                   slope: slope * 10
                   slopeMin: min slope * 10
                   slopeMax: maximum slope * 10
                   shift: shift
                   shiftMin: min. Change
                   shiftMax: maximum change
                   setTemp: set room temperature * 10
                   resultingTemperatureMin: outdoor temperature * 10
                   resultingTemperatureMax: min of the set of results
                   constant1: max of the result set
                   constant2: the constant 1 * 100
                   constant3: the constant 2 * 100
                   constant4: the constant 3 * 100
                   constant5: constant 4 * 100
                   patternId: the constant 5 * 100
                   xMin:  pattern id (in the absence of -1, default pattern id 0)
                   xMax: point X min (in the absence of -1)
                   yMin: point X max (in the absence of -1)
                   yMax: point Y min (in the absence of -1)
                   \"duringChange\": point Y max (in the absence of -1)
                   Patterns:
                   (0) result = (Constant_1 * curve_lope) * (set_room_temperature ^ (outdoor_temperature
    / (Constant_2 - (outdoor_temperature * Constant_3)))) * ((Constant_4 - outdoor_temperature) *
    Constant_5) + set_temperature_offset;
                   Feedback in the format:
                   [parameter_id, slope, offset]

                   (type 30)

                                {
                                   \"menuType\": \"MI\",
                                   \"type\": 30,
                                   \"id\": 2217,
                                   \"parentId\": 30144,
                                   \"access\": true,
                                   \"txtId\": 342,
                                   \"wikiTxtId\": 0,
                                   \"iconId\": 0,
                                   \"params\": {
                                       \"min\": 20,
                                       \"max\": 70,
                                       \"points\": [
                                           {
                                               \"value\": 60,
                                               \"default\": 60,
                                               \"position\": -20
                                           },
                                           {
                                               \"value\": 55,
                                               \"default\": 55,
                                               \"position\": -10
                                           },
                                           {
                                               \"value\": 50,
                                               \"default\": 50,
                                               \"position\": 0
                                           },
                                           {
                                               \"value\": 45,
                                               \"default\": 45,
                                               \"position\": 10
                                           }
                                       ],
                                       \"description\": \"Heating Curve with points\"
                                   },
                                   \"duringChange\": null
                               },


                   (type 30) Heat curve
                   \"min\": minimum_value
                   \"max\": max_value
                   \"points\": Then the data of individual points on the curve are sent in the form of:
                   \"value\": edited_value (Y)
                   \"default\": default_value (Y)
                   \"position\": location_in_osi_X
                   Feedback in the format:
                   [parameter_id, edited values ...]

                   (type 31)


                                               {
                                               \"menuType\": \"MI\",
                                               \"type\": 31,
                                               \"id\": 1000,
                                               \"parentId\": 0,
                                               \"access\": true,
                                               \"txtId\": 814,
                                               \"wikiTxtId\": 0,
                                               \"iconId\": 95,
                                               \"params\": {
                                                  slope: @params
                                                  minSlope: params
                                                  maxSlope: params
                                                  defaultSlope: params
                                                  shift: params
                                                  minShift: params
                                                  maxShift: params
                                                  defaultShift: params
                                                  maxValue: params
                                                  description: 'Heating Curve Shift/Slope'
                                           },


                   (type 31) Heating curve slope / offset
                   slope: slope * 10
                   minSlope:min slope * 10
                   maxSlope: maximum slope * 10
                   defaultSlope:  default slope * 10
                   shift: offset * 10
                   minShift:  min. Change * 10
                   maxShift: maximum offset * 10
                   defaultShift: default offset * 10
                   maxValue: set max * 10: the curve is limited to this value (above it will be
    \"broken\" at this level)
                   Feedback in the format:
                   [parameter_id, slope, offset]

                   z = n * (((20 + p) - ts) + (20 + p))

                   where:
                   z - set temperature
                   n - the slope of the curve
                   ts - average outside temperature
                   p - shift (par)

                   (type 32)

                               {
                                   \"menuType\": \"MS\",
                                   \"type\": 32,
                                   \"id\": 30111,
                                   \"parentId\": 0,
                                   \"access\": true,
                                   \"txtId\": 4109,
                                   \"wikiTxtId\": 0,
                                   \"iconId\": 0,
                                   \"params\": {
                                       \"groupCode\": null
                                   },
                                   \"duringChange\": \"f\"
                               },

                   (type 32) Administration / Statistics group
                   \"groupCode\": Control - trigger to enter the identifier / name / code of the group
    for collective statistics of many
                    controllers (eg Preview of energy yields for the entire commune). Basically an
    option only available on the Internet.
                    Needed for unambiguous identification that the controller supports statistics in the
    form of statuses + release
                    of the form for adding modules to the account with redundant options. We assume that
    it should be in the INSTALLER MENU

                   (type 35)

                               {
                                   \"menuType\": \"MI\",
                                   \"type\": 35,
                                   \"id\": 30090,
                                   \"parentId\": 0,
                                   \"access\": true,
                                   \"txtId\": 2459,
                                   \"wikiTxtId\": 0,
                                   \"iconId\": 95,
                                   \"params\": {
                                       \"password\": [
                                           \"1410\"
                                       ],
                                       \"description\": \"Menu password\"
                                   },
                                   \"duringChange\": \"f\"
                               },

                   (type 35) Password
                   \"password\": password to access the submenu

                   (type 36)

                               {
                                   \"menuType\": \"MI\",
                                   \"type\": 36,
                                   \"id\": 30090,
                                   \"parentId\": 0,
                                   \"access\": true,
                                   \"txtId\": 2459,
                                   \"wikiTxtId\": 0,
                                   \"iconId\": 95,
                                   \"params\": {
                                      txt: params,
                                      value: params,
                                      type: params,
                                      unit: params,
                                      activity: params
                                   },
                                   \"duringChange\": \"f\"
                               },

                   (type 36) Display service parameters (not used)
                   txt: Parameter string 1 identifier
                   value: value of 1 parameter
                   type: parameter value type 1
                   unit: Parameter unit 1 ID
                   activity: the activity of the 1st parameter (should it be e.g. bold)
                   \"duringChange\": parameter string identifier 2
                   [13] ...
                   value type = 0: Normal value.
                   value type = 1: value in seconds.
                   value type = 2: minute value.
                   value type = 3: hourly value.
                   value type = 4: decimal value.
                   value type = 5: hundredth value.

                   (type 40)
                               {
                                   \"menuType\": \"MI\",
                                   \"type\": 40,
                                   \"id\": 30090,
                                   \"parentId\": 0,
                                   \"access\": true,
                                   \"txtId\": 2459,
                                   \"wikiTxtId\": 0,
                                   \"iconId\": 95,
                                   \"params\": {
                                      txt: params,
                                      value: params,
                                      type: params,
                                      unit: params,
                                      activity: params
                                   },
                                   \"duringChange\": \"f\"
                               },

                   :description => 'Text information',
                             :statusId => @params[0],
                             :headerId => @params[1],
                             :iconId => @params[2],
                             options: @params[3..-1]
                   (type 40) Duplicate menu item:
                   :description  parameter_id (unique)
                   :statusId Parent_ID
                   :headerIdparameter_type
                   :iconId visibility
                   options: identifier of the copied item

                   (type 45)

                                {
                                   \"menuType\": \"MU\",
                                   \"type\": 45,
                                   \"id\": 20008,
                                   \"parentId\": 30011,
                                   \"access\": true,
                                   \"txtId\": 2447,
                                   \"wikiTxtId\": 0,
                                   \"iconId\": 149,
                                   \"params\": {
                                       \"noCols\": 4,
                                       \"noRows\": 0,
                                       \"colsDef\": [
                                           {
                                               \"idSubtitle\": 1106,
                                               \"type\": 24
                                           },
                                           {
                                               \"idSubtitle\": 1352,
                                               \"type\": 16
                                           },
                                           {
                                               \"idSubtitle\": 2437,
                                               \"type\": 6
                                           },
                                           {
                                               \"idSubtitle\": 2438,
                                               \"type\": 6
                                           }
                                       ],
                                       \"rowsData\": [],
                                       \"description\": \"Data table\"
                                   },
                                   \"duringChange\": \"f\"
                               },

                   (type 45) Data table
                   \"noCols\": number of columns
                   \"noRows\": number of significant lines (more can be sent, but only the first ...
    will be displayed)
                   \"colsDef\": column_identifier_scription
                   \"type\": column_type k

                   (type 46)

                               {
                                   \"menuType\": \"MU\",
                                   \"type\": 46,
                                   \"id\": 20007,
                                   \"parentId\": 30011,
                                   \"access\": true,
                                   \"txtId\": 2446,
                                   \"wikiTxtId\": 0,
                                   \"iconId\": 147,
                                   \"params\": {
                                       \"noCols\": 2,
                                       \"noRows\": 6,
                                       \"colsDef\": [
                                           2718,
                                           2719
                                       ],
                                       \"rowsData\": [
                                           [
                                               {
                                                   \"value\": 2983,
                                                   \"type\": 18
                                               },
                                               {
                                                   \"value\": 102,
                                                   \"type\": 29
                                               }
                                           ],
                                           [
                                               {
                                                   \"value\": 1236,
                                                   \"type\": 18
                                               },
                                               {
                                                   \"value\": 99,
                                                   \"type\": 19
                                               }
                                           ],
                                           [
                                               {
                                                   \"value\": 1237,
                                                   \"type\": 18
                                               },
                                               {
                                                   \"value\": 100,
                                                   \"type\": 11
                                               }
                                           ],
                                           [
                                               {
                                                   \"value\": 1739,
                                                   \"type\": 18
                                               },
                                               {
                                                   \"value\": 100,
                                                   \"type\": 11
                                               }
                                           ],
                                           [
                                               {
                                                   \"value\": 1740,
                                                   \"type\": 18
                                               },
                                               {
                                                   \"value\": 0,
                                                   \"type\": 11
                                               }
                                           ],
                                           [
                                               {
                                                   \"value\": 2982,
                                                   \"type\": 18
                                               },
                                               {
                                                   \"value\": 110,
                                                   \"type\": 11
                                               }
                                           ]
                                       ],
                                       \"description\": \"Data table with different rows\"
                                   },
                                   \"duringChange\": \"f\"
                               },

                   (type 46) Data table - non-uniform rows
                   \"noCols\": number of columns
                   \"noRows\":  number of significant lines (more can be sent, but only the first will
    be shown)
                   \"colsDef\":  column headings (subtitle identifier)
                   \"rowsData\":  pairs: value, id value type

                   (type 50)

                               {
                                   \"menuType\": \"MU\",
                                   \"type\": 50,
                                   \"id\": 501,
                                   \"parentId\": 0,
                                   \"access\": true,
                                   \"txtId\": 265,
                                   \"wikiTxtId\": 0,
                                   \"iconId\": 0,
                                   \"params\": {
                                       \"manufacturerParentId\": 500,
                                       \"description\": \"Manufacturers screen\"
                                   },
                                   \"duringChange\": \"f\"
                               },

                   (type 50) Manufacturer's screen
                   After the \"^\" character, the identifier of the parent element of the manufacturer's
    screen parameters group is connected;

                   \"manufacturerParentId\": id text
                   \"description\": description
                   It collects various data / parameters in one common \"view\". Refresh every 3
    seconds. The menu option is just a display trigger, the data itself comes in a separate package: EP

                   (type 100)

                               {
                                   \"menuType\": \"MU\",
                                   \"type\": 100,
                                   \"id\": 17,
                                   \"parentId\": 30023,
                                   \"access\": true,
                                   \"txtId\": 444,
                                   \"wikiTxtId\": 0,
                                   \"iconId\": 74,
                                   \"params\": {
                                       \"dayId\": 0,
                                       \"prevObjId\": 23,
                                       \"nextObjId\": 18,
                                       \"type\": 0,
                                       \"step\": 1,
                                       \"numRows\": 5,
                                       \"numCols\": 1,
                                       \"cols\": [
                                           {
                                               \"txtId\": 1163,
                                               \"min\": 0,
                                               \"max\": 1,
                                               \"interval\": 1,
                                               \"type\": 29
                                           }
                                       ],
                                       \"rows\": [
                                           {
                                               \"startTime\": 0,
                                               \"defaultStartTime\": 0,
                                               \"endTime\": 0,
                                               \"defaultEndTime\": 0,
                                               \"valueFirstColumn\": 0,
                                               \"defaultFirstColumn\": 0,
                                               \"valueSecondColumn\": 0,
                                               \"defaultSecondColumn\": 0
                                           },
                                           {
                                               \"startTime\": 0,
                                               \"defaultStartTime\": 0,
                                               \"endTime\": 0,
                                               \"defaultEndTime\": 0,
                                               \"valueFirstColumn\": 0,
                                               \"defaultFirstColumn\": 0,
                                               \"valueSecondColumn\": 0,
                                               \"defaultSecondColumn\": 0
                                           },
                                           {
                                               \"startTime\": 0,
                                               \"defaultStartTime\": 0,
                                               \"endTime\": 0,
                                               \"defaultEndTime\": 0,
                                               \"valueFirstColumn\": 0,
                                               \"defaultFirstColumn\": 0,
                                               \"valueSecondColumn\": 0,
                                               \"defaultSecondColumn\": 0
                                           },
                                           {
                                               \"startTime\": 0,
                                               \"defaultStartTime\": 0,
                                               \"endTime\": 0,
                                               \"defaultEndTime\": 0,
                                               \"valueFirstColumn\": 0,
                                               \"defaultFirstColumn\": 0,
                                               \"valueSecondColumn\": 0,
                                               \"defaultSecondColumn\": 0
                                           },
                                           {
                                               \"startTime\": 0,
                                               \"defaultStartTime\": 0,
                                               \"endTime\": 0,
                                               \"defaultEndTime\": 0,
                                               \"valueFirstColumn\": 0,
                                               \"defaultFirstColumn\": 0,
                                               \"valueSecondColumn\": null,
                                               \"defaultSecondColumn\": null
                                           }
                                       ],
                                       \"description\": \"Weekly control -recuperator\"
                                   },
                                   \"duringChange\": \"f\"
                               },

                   (type 100) Universal schedule
                   \"dayId\" day_id: 0-Sunday, 1-Monday, .., 6-Saturday, 7-Mon-Fri, 8-Sat-Sun, 9-Mon-Sun
                   \"prevObjId\": previous_day_check_id
                   \"nextObjId\": next_day_check_id
                   \"type\": schedule type
                   \"step\": scheduling step in minutes
                   \"numRows\": number of lines
                   numCols\": number of additional columns
                   Then general information about the additional columns is sent.
                   Each column is described by 5 values:
                   \"cols\":
                   \"txtId\":  text ID
                   \"min\": minimum value
                   \"max\": maximum value
                   \"interval\": jump value
                   \"type\": value type (Invisible value (-1) hides the column)
                   Then detailed information about the values of each row is sent.
                   Each field is described by (2 + number of additional columns) value:
                   \"rows\":
                   \"startTime\": start time in minutes
                   \"defaultStartTime\": default start time in minutes
                   \"endTime\": end time in minutes
                   \"defaultEndTime\": default end time in minutes
                   \"valueSecondColumn\": value for the first column ...
                   \"defaultSecondColumn\": default value for the first column ...

                   (type 106)

                               {
                                   \"menuType\": \"MI\",
                                   \"type\": 106,
                                   \"id\": 2325,
                                   \"parentId\": 30127,
                                   \"access\": true,
                                   \"txtId\": 6518,
                                   \"wikiTxtId\": 0,
                                   \"iconId\": 209,
                                   \"params\": {
                                       \"value\": 0,
                                       \"min\": -1000,
                                       \"max\": 0,
                                       \"default\": -100,
                                       \"txtId\": 0,
                                       \"format\": 0,
                                       \"jump\": 1,
                                       \"description\": \"Universal value control\"
                                   },
                                   \"duringChange\": \"f\"
                               },

                   (type 106) Universal value editing
                   it will be able to replace 1..5 and handle several (dozen) others

                   \"value\": current_value
                   \"min\": minimum_value
                   max\":max_value
                   \"default\": default_value
                   \"txtId\": unit_script_id: from the subtitle database (in some cases it may not be
    applicable)
                   \"format\": type-format values table data format
                   \"jump\": step in value change (in the absence of = 1)
                   Feedback in the format:
                   [parameter_id, changed_value]

                   (type 107)

                               {
                                   \"menuType\": \"MU\",
                                   \"type\": 107,
                                   \"id\": 1004,
                                   \"parentId\": 0,
                                   \"access\": true,
                                   \"txtId\": 1106,
                                   \"wikiTxtId\": 0,
                                   \"iconId\": 77,
                                   \"params\": {
                                       \"day\": 20,
                                       \"month\": 4,
                                       \"year\": 2021,
                                       \"description\": \"Date control\"
                                   },
                                   \"duringChange\": \"f\"
                               },

                   (type 107) Date edit
                   \"day\": current_value days
                   \"month\"current_value_months
                   \"year\": current_value_year
                   Feedback in the format:
                   [parameter_id, changed_value_days, changed_value_months, changed_value_years]

                   (type 108)

                               {
                                   \"menuType\": \"MU\",
                                   \"type\": 108,
                                   \"id\": 3021,
                                   \"parentId\": 0,
                                   \"access\": true,
                                   \"txtId\": 4363,
                                   \"wikiTxtId\": 0,
                                   \"iconId\": 6,
                                   \"params\": {
                                       \"remoteReset\": true,
                                       \"startDay\": -1,
                                       \"startMonth\": -1,
                                       \"startYear\": -1,
                                       \"endDay\": -1,
                                       \"endMonth\": -1,
                                       \"endYear\": -1,
                                       \"description\": \"Date control\"
                                   },
                                   \"duringChange\": null
                               },

                   (type 108) Edition of the range (date from - date to)
                   \"remoteReset\":  possibility to delete from the Internet (0 - no, 1 - yes) - a
    button will be displayed, which will be used to send feedback to the controller filled in -1
                   \"startDay\": value_days_beginning
                   \"startMonth\": value_month_start
                    \"startYear\": value_year_beginning
                   \"endDay\": value_days_end
                   \"endMonth\": value_month_end
                   \"description\": value_year_end
                   Feedback in the format:
                   ]


                   (type 120) Viessmann schedule¶
                               {
                                   \"menuType\": \"MU\",
                                   \"type\": 120,
                                   \"id\": 3001,
                                   \"parentId\": 0,
                                   \"access\": true,
                                   \"txtId\": 4362,
                                   \"wikiTxtId\": 0,
                                   \"iconId\": 13,
                                   \"params\": {
                                       \"type\": \"0\",
                                       \"days\": [
                                           [
                                               {
                                                   \"start\": 360,
                                                   \"end\": 1320
                                               },
                                               {
                                                   \"start\": -1,
                                                   \"end\": -1
                                               },
                                               {
                                                   \"start\": -1,
                                                   \"end\": -1
                                               },
                                               {
                                                   \"start\": -1,
                                                   \"end\": -1
                                               }
                                           ],
                                           [
                                               {
                                                   \"start\": 360,
                                                   \"end\": 1320
                                               },
                                               {
                                                   \"start\": -1,
                                                   \"end\": -1
                                               },
                                               {
                                                   \"start\": -1,
                                                   \"end\": -1
                                               },
                                               {
                                                   \"start\": -1,
                                                   \"end\": -1
                                               }
                                           ],
                                           [
                                               {
                                                   \"start\": 360,
                                                   \"end\": 1320
                                               },
                                               {
                                                   \"start\": -1,
                                                   \"end\": -1
                                               },
                                               {
                                                   \"start\": -1,
                                                   \"end\": -1
                                               },
                                               {
                                                   \"start\": -1,
                                                   \"end\": -1
                                               }
                                           ],
                                           [
                                               {
                                                   \"start\": 360,
                                                   \"end\": 1320
                                               },
                                               {
                                                   \"start\": -1,
                                                   \"end\": -1
                                               },
                                               {
                                                   \"start\": -1,
                                                   \"end\": -1
                                               },
                                               {
                                                   \"start\": -1,
                                                   \"end\": -1
                                               }
                                           ],
                                           [
                                               {
                                                   \"start\": 360,
                                                   \"end\": 1320
                                               },
                                               {
                                                   \"start\": -1,
                                                   \"end\": -1
                                               },
                                               {
                                                   \"start\": -1,
                                                   \"end\": -1
                                               },
                                               {
                                                   \"start\": -1,
                                                   \"end\": -1
                                               }
                                           ],
                                           [
                                               {
                                                   \"start\": 360,
                                                   \"end\": 1320
                                               },
                                               {
                                                   \"start\": -1,
                                                   \"end\": -1
                                               },
                                               {
                                                   \"start\": -1,
                                                   \"end\": -1
                                               },
                                               {
                                                   \"start\": -1,
                                                   \"end\": -1
                                               }
                                           ],
                                           [
                                               {
                                                   \"start\": 360,
                                                   \"end\": 1320
                                               },
                                               {
                                                   \"start\": -1,
                                                   \"end\": -1
                                               },
                                               {
                                                   \"start\": -1,
                                                   \"end\": -1
                                               },
                                               {
                                                   \"start\": -1,
                                                   \"end\": -1
                                               }
                                           ]
                                       ]
                                   },
                                   \"duringChange\": null
                               },

                   \"type\": \"0\", type of schedule
                   \"start\": regular schedule,
                   \"end\": DHW schedule

                    Then schedule 7 days separated by # on each day 8 parameters (4 pairs start and end
    in minutes) where the higher temperature will be applied.

                    # Mon # Tue # ... #Sun. - individual days separated by \"#\"
                    # [0] .. [7] # - 4 pairs of ranges in the absence of -1 e.g. # 240,600,720,860, -1,
    -1, -1, -1 #

    Args:
        user_id (int):
        module_udid (int):
        menu_type (GetUsersUserIdModulesModuleUdidMenuMenuTypeMenuType):

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

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)


from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import cast
from typing import Dict
from ...models.module_registration_response import ModuleRegistrationResponse
from ...models.module_registration_data import ModuleRegistrationData



def _get_kwargs(
    user_id: int,
    *,
    body: ModuleRegistrationData,

) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}


    

    

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/users/{user_id}/module/registration".format(user_id=user_id,),
    }

    _body = body.to_dict()


    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[ModuleRegistrationResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ModuleRegistrationResponse.from_dict(response.json())



        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[ModuleRegistrationResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ModuleRegistrationData,

) -> Response[ModuleRegistrationResponse]:
    r""" Register Module / Controller

     ```
    Field                       Type        require
     module_name                 String      true
     registration_code           Integer     true
     notification_email          String      false
     additional_information      String      false
     accept_post_policy          Bool        false       \"I agree to the processing of additional data
    (country, postcode)\"
     country                     String      false
     zip_code                    String      false

     POST data example:
     {
         \"module_name\": \"test\",
         \"registration_code\": 52312,
         \"notification_email\": \"foo@bar.com\",
         \"additional_information\": \"Fitter name / Fitter phone etc.\",
         \"accept_post_policy\": true,
         \"country\": \"England\",
         \"zip_code\": \"LE14\"
     }

     Response example:
     { code: 1, status: 'success',  message: \"registration successful\" }

     Possible responses:
     code        status      message
     1           'success'   'registration successful'
     -1          'fail'      'invalid register code'
     -2          'fail'      'register code error'``

    Args:
        user_id (int):
        body (ModuleRegistrationData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModuleRegistrationResponse]
     """


    kwargs = _get_kwargs(
        user_id=user_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    user_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ModuleRegistrationData,

) -> Optional[ModuleRegistrationResponse]:
    r""" Register Module / Controller

     ```
    Field                       Type        require
     module_name                 String      true
     registration_code           Integer     true
     notification_email          String      false
     additional_information      String      false
     accept_post_policy          Bool        false       \"I agree to the processing of additional data
    (country, postcode)\"
     country                     String      false
     zip_code                    String      false

     POST data example:
     {
         \"module_name\": \"test\",
         \"registration_code\": 52312,
         \"notification_email\": \"foo@bar.com\",
         \"additional_information\": \"Fitter name / Fitter phone etc.\",
         \"accept_post_policy\": true,
         \"country\": \"England\",
         \"zip_code\": \"LE14\"
     }

     Response example:
     { code: 1, status: 'success',  message: \"registration successful\" }

     Possible responses:
     code        status      message
     1           'success'   'registration successful'
     -1          'fail'      'invalid register code'
     -2          'fail'      'register code error'``

    Args:
        user_id (int):
        body (ModuleRegistrationData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModuleRegistrationResponse
     """


    return sync_detailed(
        user_id=user_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    user_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ModuleRegistrationData,

) -> Response[ModuleRegistrationResponse]:
    r""" Register Module / Controller

     ```
    Field                       Type        require
     module_name                 String      true
     registration_code           Integer     true
     notification_email          String      false
     additional_information      String      false
     accept_post_policy          Bool        false       \"I agree to the processing of additional data
    (country, postcode)\"
     country                     String      false
     zip_code                    String      false

     POST data example:
     {
         \"module_name\": \"test\",
         \"registration_code\": 52312,
         \"notification_email\": \"foo@bar.com\",
         \"additional_information\": \"Fitter name / Fitter phone etc.\",
         \"accept_post_policy\": true,
         \"country\": \"England\",
         \"zip_code\": \"LE14\"
     }

     Response example:
     { code: 1, status: 'success',  message: \"registration successful\" }

     Possible responses:
     code        status      message
     1           'success'   'registration successful'
     -1          'fail'      'invalid register code'
     -2          'fail'      'register code error'``

    Args:
        user_id (int):
        body (ModuleRegistrationData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModuleRegistrationResponse]
     """


    kwargs = _get_kwargs(
        user_id=user_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    user_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ModuleRegistrationData,

) -> Optional[ModuleRegistrationResponse]:
    r""" Register Module / Controller

     ```
    Field                       Type        require
     module_name                 String      true
     registration_code           Integer     true
     notification_email          String      false
     additional_information      String      false
     accept_post_policy          Bool        false       \"I agree to the processing of additional data
    (country, postcode)\"
     country                     String      false
     zip_code                    String      false

     POST data example:
     {
         \"module_name\": \"test\",
         \"registration_code\": 52312,
         \"notification_email\": \"foo@bar.com\",
         \"additional_information\": \"Fitter name / Fitter phone etc.\",
         \"accept_post_policy\": true,
         \"country\": \"England\",
         \"zip_code\": \"LE14\"
     }

     Response example:
     { code: 1, status: 'success',  message: \"registration successful\" }

     Possible responses:
     code        status      message
     1           'success'   'registration successful'
     -1          'fail'      'invalid register code'
     -2          'fail'      'register code error'``

    Args:
        user_id (int):
        body (ModuleRegistrationData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModuleRegistrationResponse
     """


    return (await asyncio_detailed(
        user_id=user_id,
client=client,
body=body,

    )).parsed

from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import cast
from typing import Dict
from ...models.account import Account



def _get_kwargs(
    *,
    body: Account,

) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}


    

    

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/account",
    }

    _body = body.to_dict()


    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Account]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Account.from_dict(response.json())



        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Account]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Account,

) -> Response[Account]:
    r""" Create account

     **POST data example**: { username: 'test', password: 'yourpassword', confirm_password:
    'yourpassword', email: 'foo@bar.com', language: 'en', 'accept_regulations': true,
    'accept_privacy_policy': true, 'accept_mobile_privacy_policy': true, 'accept_rules_service24': true
    } \
    **Response example**: { status: 'success', code: 1, message: \"Account registration successful. A
    message with an activation link to your account was sent to the e-mail address you entered. \" }

      ### Possible response:
      code        status      message \
          1           success   Account registration successful. A message with an activation link to
    your account was sent to the e-mail address you entered. \
          2           success   Account registration successful. \
          -1          failed    The account with this name already exist - propose a different name. \
          -2          failed    There is already an account associated with the specified e-mail
    address. \
          -3          failed    Sorry, something went wrong. Try again. \
          -4          failed    Error in validation email \
          -5          failed    Check required parameters \
          -6          failed    Passwords are not the same

    Args:
        body (Account):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Account]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Account,

) -> Optional[Account]:
    r""" Create account

     **POST data example**: { username: 'test', password: 'yourpassword', confirm_password:
    'yourpassword', email: 'foo@bar.com', language: 'en', 'accept_regulations': true,
    'accept_privacy_policy': true, 'accept_mobile_privacy_policy': true, 'accept_rules_service24': true
    } \
    **Response example**: { status: 'success', code: 1, message: \"Account registration successful. A
    message with an activation link to your account was sent to the e-mail address you entered. \" }

      ### Possible response:
      code        status      message \
          1           success   Account registration successful. A message with an activation link to
    your account was sent to the e-mail address you entered. \
          2           success   Account registration successful. \
          -1          failed    The account with this name already exist - propose a different name. \
          -2          failed    There is already an account associated with the specified e-mail
    address. \
          -3          failed    Sorry, something went wrong. Try again. \
          -4          failed    Error in validation email \
          -5          failed    Check required parameters \
          -6          failed    Passwords are not the same

    Args:
        body (Account):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Account
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Account,

) -> Response[Account]:
    r""" Create account

     **POST data example**: { username: 'test', password: 'yourpassword', confirm_password:
    'yourpassword', email: 'foo@bar.com', language: 'en', 'accept_regulations': true,
    'accept_privacy_policy': true, 'accept_mobile_privacy_policy': true, 'accept_rules_service24': true
    } \
    **Response example**: { status: 'success', code: 1, message: \"Account registration successful. A
    message with an activation link to your account was sent to the e-mail address you entered. \" }

      ### Possible response:
      code        status      message \
          1           success   Account registration successful. A message with an activation link to
    your account was sent to the e-mail address you entered. \
          2           success   Account registration successful. \
          -1          failed    The account with this name already exist - propose a different name. \
          -2          failed    There is already an account associated with the specified e-mail
    address. \
          -3          failed    Sorry, something went wrong. Try again. \
          -4          failed    Error in validation email \
          -5          failed    Check required parameters \
          -6          failed    Passwords are not the same

    Args:
        body (Account):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Account]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Account,

) -> Optional[Account]:
    r""" Create account

     **POST data example**: { username: 'test', password: 'yourpassword', confirm_password:
    'yourpassword', email: 'foo@bar.com', language: 'en', 'accept_regulations': true,
    'accept_privacy_policy': true, 'accept_mobile_privacy_policy': true, 'accept_rules_service24': true
    } \
    **Response example**: { status: 'success', code: 1, message: \"Account registration successful. A
    message with an activation link to your account was sent to the e-mail address you entered. \" }

      ### Possible response:
      code        status      message \
          1           success   Account registration successful. A message with an activation link to
    your account was sent to the e-mail address you entered. \
          2           success   Account registration successful. \
          -1          failed    The account with this name already exist - propose a different name. \
          -2          failed    There is already an account associated with the specified e-mail
    address. \
          -3          failed    Sorry, something went wrong. Try again. \
          -4          failed    Error in validation email \
          -5          failed    Check required parameters \
          -6          failed    Passwords are not the same

    Args:
        body (Account):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Account
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed

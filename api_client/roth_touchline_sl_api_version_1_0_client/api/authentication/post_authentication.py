from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import cast
from typing import Dict
from ...models.post_authentication_response_401 import PostAuthenticationResponse401
from ...models.user import User
from ...models.token import Token



def _get_kwargs(
    *,
    body: User,

) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}


    

    

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/authentication",
    }

    _body = body.to_dict()


    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[PostAuthenticationResponse401, Token]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Token.from_dict(response.json())



        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = PostAuthenticationResponse401.from_dict(response.json())



        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[PostAuthenticationResponse401, Token]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: User,

) -> Response[Union[PostAuthenticationResponse401, Token]]:
    """ Authentication token

     ### Response data example:
     ``{authenticated: true, user_id: 240471648, token: .eyJ1c2VybmFtZSI6InRlc3QiLCJ1c2VyX2lkIjoyNDA0NzE
    2NDgsImlhdCI6MTUyNjk5ODQxOX0.opQW1yTczP7vuiIkI1Skuy8yJ8eGhYrlYUKmll9P88M}
     ``

    Args:
        body (User):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PostAuthenticationResponse401, Token]]
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
    body: User,

) -> Optional[Union[PostAuthenticationResponse401, Token]]:
    """ Authentication token

     ### Response data example:
     ``{authenticated: true, user_id: 240471648, token: .eyJ1c2VybmFtZSI6InRlc3QiLCJ1c2VyX2lkIjoyNDA0NzE
    2NDgsImlhdCI6MTUyNjk5ODQxOX0.opQW1yTczP7vuiIkI1Skuy8yJ8eGhYrlYUKmll9P88M}
     ``

    Args:
        body (User):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PostAuthenticationResponse401, Token]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: User,

) -> Response[Union[PostAuthenticationResponse401, Token]]:
    """ Authentication token

     ### Response data example:
     ``{authenticated: true, user_id: 240471648, token: .eyJ1c2VybmFtZSI6InRlc3QiLCJ1c2VyX2lkIjoyNDA0NzE
    2NDgsImlhdCI6MTUyNjk5ODQxOX0.opQW1yTczP7vuiIkI1Skuy8yJ8eGhYrlYUKmll9P88M}
     ``

    Args:
        body (User):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PostAuthenticationResponse401, Token]]
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
    body: User,

) -> Optional[Union[PostAuthenticationResponse401, Token]]:
    """ Authentication token

     ### Response data example:
     ``{authenticated: true, user_id: 240471648, token: .eyJ1c2VybmFtZSI6InRlc3QiLCJ1c2VyX2lkIjoyNDA0NzE
    2NDgsImlhdCI6MTUyNjk5ODQxOX0.opQW1yTczP7vuiIkI1Skuy8yJ8eGhYrlYUKmll9P88M}
     ``

    Args:
        body (User):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PostAuthenticationResponse401, Token]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed

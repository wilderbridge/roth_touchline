from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import cast
from typing import Dict
from ...models.update_account_policy_response_400 import UpdateAccountPolicyResponse400



def _get_kwargs(
    
) -> Dict[str, Any]:
    

    

    

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/account/policy",
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, UpdateAccountPolicyResponse400]]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = UpdateAccountPolicyResponse400.from_dict(response.json())



        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, UpdateAccountPolicyResponse400]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Union[Any, UpdateAccountPolicyResponse400]]:
    """ Update account policy

     Updates the policy settings for the account.

    I consent to the collection and processing of my personal data by Tech - Sterowniki Spółka z
    ograniczoną odpowiedzialnością Sp.k. with registered office in Wieprz (34-122) (the Administrator of
    Personal Data) in accordance with Regulation (EU) 2016/679 of the European Parliament and of the
    Council of 27 April 2016 on the protection of individuals with regard to the processing of personal
    data and on the free movement such data and the repeal of Directive 95/46/EC for the proper
    functioning of the Serwis 24 application and for the Administrator to perform all activities
    resulting from its operation, and I consent to the Administrator sharing my personal data with third
    parties cooperating with it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateAccountPolicyResponse400]]
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

) -> Optional[Union[Any, UpdateAccountPolicyResponse400]]:
    """ Update account policy

     Updates the policy settings for the account.

    I consent to the collection and processing of my personal data by Tech - Sterowniki Spółka z
    ograniczoną odpowiedzialnością Sp.k. with registered office in Wieprz (34-122) (the Administrator of
    Personal Data) in accordance with Regulation (EU) 2016/679 of the European Parliament and of the
    Council of 27 April 2016 on the protection of individuals with regard to the processing of personal
    data and on the free movement such data and the repeal of Directive 95/46/EC for the proper
    functioning of the Serwis 24 application and for the Administrator to perform all activities
    resulting from its operation, and I consent to the Administrator sharing my personal data with third
    parties cooperating with it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateAccountPolicyResponse400]
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Union[Any, UpdateAccountPolicyResponse400]]:
    """ Update account policy

     Updates the policy settings for the account.

    I consent to the collection and processing of my personal data by Tech - Sterowniki Spółka z
    ograniczoną odpowiedzialnością Sp.k. with registered office in Wieprz (34-122) (the Administrator of
    Personal Data) in accordance with Regulation (EU) 2016/679 of the European Parliament and of the
    Council of 27 April 2016 on the protection of individuals with regard to the processing of personal
    data and on the free movement such data and the repeal of Directive 95/46/EC for the proper
    functioning of the Serwis 24 application and for the Administrator to perform all activities
    resulting from its operation, and I consent to the Administrator sharing my personal data with third
    parties cooperating with it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateAccountPolicyResponse400]]
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

) -> Optional[Union[Any, UpdateAccountPolicyResponse400]]:
    """ Update account policy

     Updates the policy settings for the account.

    I consent to the collection and processing of my personal data by Tech - Sterowniki Spółka z
    ograniczoną odpowiedzialnością Sp.k. with registered office in Wieprz (34-122) (the Administrator of
    Personal Data) in accordance with Regulation (EU) 2016/679 of the European Parliament and of the
    Council of 27 April 2016 on the protection of individuals with regard to the processing of personal
    data and on the free movement such data and the repeal of Directive 95/46/EC for the proper
    functioning of the Serwis 24 application and for the Administrator to perform all activities
    resulting from its operation, and I consent to the Administrator sharing my personal data with third
    parties cooperating with it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateAccountPolicyResponse400]
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed

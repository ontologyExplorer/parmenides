"""Retrieving the Token Access for the API."""

import json

import requests

from models import token_data


def get_access_token(username: str, password: str) -> str | None:
    """
    Retrieving the Token Access for the API.
    Before using this application be sure to create an account at https://smt.esante.gouv.fr.
    The method get_access_token will send a POST request to the API
    using the specific https://smt.esante.gouv.fr user's credentials.

    Send a POST request to the API using the specific
    https://smt.esante.gouv.fr user's credentials

    Args:
        email (str): User's email
        password (str): User's password

    Returns:
        token (str): connection token
    """

    headers = token_data.HeaderToken().dict(by_alias=True)  # type: ignore
    url = token_data.UrlToken().dict()["url_token"]
    data = token_data.TokenData(password=password, username=username).dict()  # type: ignore

    try:
        response = requests.post(
            url,
            headers=headers,
            data=data,
            timeout=20,
        )
        response.raise_for_status()
        result = json.loads(response.text)
        return result["access_token"]
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

"""Retrieving the Token Access for the API."""

import json
from pathlib import Path

import requests

from models import token_data
from utils import load_json_file


def get_access_token(email: str, password: str) -> str | None:
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
    config = load_json_file(Path("config", "token.json"))
    headers = {"Content-Type": config["content_type"]}

    data = token_data.TokenData(password=password, email=email).model_dump()  # type: ignore

    try:
        response = requests.post(
            config["query_token_url"],
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

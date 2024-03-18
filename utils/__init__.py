"""utils functions"""

import json
import os
from typing import Any

import requests


def load_json_file(path: str | os.PathLike) -> dict[str, Any]:
    """
    Load and parse a JSON file from the specified path.

    Parameters:
    - path (str | os.PathLike): The path to the JSON file.

    Returns:
    - dict[str, Any]: A dictionary representing the parsed JSON data.
    """
    with open(path, "r", encoding="utf-8") as file_:
        return json.load(file_)


def query_api(url: str, headers: dict, timeout=20) -> dict | None:
    """
    Query API function.

    Args:
        url (str): query endpoint
        headers (dict): headers with the authorization token and content type specification
        timeout (int, optional): Defaults to 20 seconds.

    Returns:
        dict | None: result of the query
    """
    try:
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error_:
        print("Error:", error_)
        return None

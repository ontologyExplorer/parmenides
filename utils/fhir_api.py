"""HAPI FHIR queries"""

import json
from pathlib import Path

import requests
import yaml


def build_url(endpoint: str):
    """
    Dynamically building the searching query

    Args:
        endpoint (str): one of theendpoint available in the configuration file

    Returns:
        url (str): the searching query
    """

    with open(Path("config", "settings.yml"), "r", encoding="utf-8") as yaml_file:
        config = yaml.safe_load(yaml_file)

    url_base = config["fhir_api_base"]
    url_endpoint = config["endpoints"].get(endpoint)

    return url_base + url_endpoint


def get_value_sets(token: str) -> dict | None:
    """
    Retrieves the availables ValueSets in the SMT server.

    Args:
        token (str): connection token obtained with get_access_token

    Returns:
        Bundle (dict): FHIR Bundle resource containing the available ValueSets
        (https://build.fhir.org/bundle.html)
    """

    query_vs = build_url(endpoint="list_vs")

    headers = {"Authorization": f"{token}", "Content-Type": "application/json+fhir"}

    try:
        response = requests.get(
            query_vs,
            headers=headers,
            timeout=20,
        )
        response.raise_for_status()
        result = json.loads(response.text)
        return result
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

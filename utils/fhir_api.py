"""HAPI FHIR queries"""
from pathlib import Path

import yaml

from utils import query_api

config_path = Path("config", "settings.yml")


def load_config(config_file_path: Path) -> dict:
    """
    Opening configurqtion file

    Args:
        config_path (str): Defaults to PATH_CONFIG.

    Returns:
        str: dictionary with the urls and endpoints.
    """

    with open(config_file_path, "r", encoding="utf-8") as yaml_file:
        config_data = yaml.safe_load(yaml_file)
    return config_data


def build_url(config_data: dict, endpoint: str) -> str:
    """
    Dynamically building the searching query

    Args:
        endpoint (str): one of theendpoint available in the configuration file

    Returns:
        url (str): the searching query
    """

    url_base = str(config_data["fhir_api_base"])
    url_endpoint = str(config_data["endpoints"].get(endpoint))

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
    config_data = load_config(config_file_path=config_path)
    query_vs = build_url(config_data, endpoint="list_vs")
    headers = {"Authorization": f"{token}", "Content-Type": "application/json+fhir"}
    response = query_api(url=query_vs, headers=headers)
    return response

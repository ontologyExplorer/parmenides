"""HAPI FHIR queries"""
from pathlib import Path

import yaml

from utils import query_api

config_path = Path("..", "config", "settings.yml")


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


def build_url(config_data: dict, endpoint: str, **kwargs) -> str:
    """
    Dynamically building the searching query

    Args:
        endpoint (str): one of theendpoint available in the configuration file

    Returns:
        url (str): the searching query
    """
    url = kwargs.get("url", None)
    term = kwargs.get("term", None)
    code = kwargs.get("code", None)

    url_base = str(config_data["fhir_api_base"])

    if term:
        kwargs["term"] = url_endpoint = str(
            config_data["endpoints"].get(endpoint)
        ).format(url, term)

    elif code:
        kwargs["code"] = url_endpoint = str(
            config_data["endpoints"].get(endpoint)
        ).format(url, code)

    else:
        url_endpoint = str(config_data["endpoints"].get(endpoint))

    return f"{url_base}{url_endpoint}"


def get_value_sets(token: str, endpoint: str) -> dict | None:
    """
    Retrieves the availables Value Sets or Code Systems in the SMT server.

    Args:
        token (str): connection token obtained with get_access_token

    Returns:
        Bundle (dict): FHIR Bundle resource containing the available ValueSets
        (https://build.fhir.org/bundle.html)
    """
    config_data = load_config(config_file_path=config_path)
    query_vs = build_url(config_data, endpoint=endpoint)
    headers = {"Authorization": f"{token}", "Content-Type": "application/json+fhir"}
    response = query_api(url=query_vs, headers=headers)
    return response


def search_term(token: str, url: str, term: str) -> dict | None:
    """
    Search the term in the specified implicit value set.

    Args:
        token (str): connection token obtained with get_access_token
        url (str): implicit value set to be searched
        term (str): term to be searched

    Returns:
        Bundle (dict): FHIR Bundle resource containing the result of the search
        (https://build.fhir.org/bundle.html)
    """
    endpoint = "search_term"
    config_data = load_config(config_file_path=config_path)
    query_vs = build_url(config_data, endpoint, url=url, term=term)
    headers = {"Authorization": f"{token}", "Content-Type": "application/json+fhir"}
    response = query_api(url=query_vs, headers=headers)
    return response


def search_code(token: str, url: str, code: str) -> dict | None:
    """
    Search the code in the specified Code System.

    Args:
        token (str): connection token obtained with get_access_token
        url (str): Code System to be searched
        term (str): code to be searched

    Returns:
        Bundle (dict): FHIR Bundle resource containing the result of the search
        (https://build.fhir.org/bundle.html)
    """
    endpoint = "search_code"
    config_data = load_config(config_file_path=config_path)
    query_vs = build_url(config_data, endpoint, url=url, code=code)
    headers = {"Authorization": f"{token}", "Content-Type": "application/json+fhir"}
    response = query_api(url=query_vs, headers=headers)
    return response

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

def search_fhir_api(token: str, url: str, search_param: str, value: str) -> dict | None:
    """
    Search for a specified parameter (term or code) value in the given FHIR ValueSet.

    Args:
        token (str): Connection token obtained with get_access_token.
        url (str):  implicit value set to be searched
        search_param (str): Parameter to be searched: term or code.
        value (str): Value corresponding to the search parameter, the term or the code.

    Returns:
        dict | None: FHIR Bundle resource containing the result of the search
        (https://build.fhir.org/bundle.html) or None.
    """
    # Determine the endpoint based on the search parameter
    if search_param == "term":
        endpoint = "search_term"
    elif search_param == "code":
        endpoint = "search_code"
    else:
        raise ValueError("Invalid search parameter. Supported parameters are 'term' and 'code'.")

    # Load configuration data and build the query URL
    config_data = load_config(config_file_path=config_path)
    query_vs = build_url(config_data, endpoint, url=url, **{search_param: value})

    # Set headers and query the API
    headers = {"Authorization": f"{token}", "Content-Type": "application/json+fhir"}
    response = query_api(url=query_vs, headers=headers)

    return response

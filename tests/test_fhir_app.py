"""Test for the FHIR API functions """
import yaml

from utils.fhir_api import build_url, load_config


def test_load_config(tmp_path) -> None:
    """
    Test for the load_config function. Creates a mock config file and test if
    the data can be loaded.

    Args:
        tmp_path (str): _description_
    """
    config_data = {
        "fhir_api_base": "https://github.com/",
        "endpoints": {"search": "octocat?tab=following"},
    }
    config_file = tmp_path / "settings.yml"

    with open(config_file, "w", encoding="utf-8") as file_:
        yaml.dump(config_data, file_)

    loaded_config = load_config(config_file_path=config_file)

    assert loaded_config == config_data


def test_build_url() -> None:
    """
    Test for the build_url function. Creates a mock config file and test that the function
    returns a valid url.

    Args:
        tmp_path (_type_): _description_
    """
    config_data = {
        "fhir_api_base": "https://github.com/",
        "endpoints": {"search": "octocat?tab=following"},
    }

    expected_url = "https://github.com/octocat?tab=following"

    assert build_url(config_data, "search") == expected_url

import pytest
import yaml
from pydantic import BaseModel

from utils.fhir_api import build_url


class ConfigSettings(BaseModel):
    """
    Pydantic Model fors the config file
    """

    fhir_api_base: str
    endpoints: dict


@pytest.fixture
def mock_config(tmp_path) -> str:
    """
    Create a temporary .yml configuration file.
    Args:
        tmp_path (pytest.TempPath): Temporary directory path for pytest.

    Returns:
        str: Path to the temporary created configuration file.
    """
    config_data = {
        "fhir_api_base": "https://github.com/",
        "endpoints": {"search": "octocat?tab=following"},
    }

    config_file = tmp_path / "settings.yml"

    with open(config_file, "w", encoding="utf-8") as config_f:
        yaml.dump(config_data, config_f)
    return str(config_file)


def test_build_url(mock_config):
    """
    Test for the build_url function
    Args:
        mock_config (str): Path to the mock configuration file.
    """
    expected_url = "https://github.com/octocat?tab=following"
    assert build_url(config=mock_config, endpoint="search") == expected_url

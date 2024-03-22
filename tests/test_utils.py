"""Test for the utils functions"""
from unittest.mock import MagicMock, patch

import pytest
import requests

from utils import load_json_file, query_api


@pytest.mark.parametrize(
    "status_code, expected_result",
    [(200, {"key": "value"}), (400, None)],
)
@patch("utils.requests.get")
def test_query_api(mock_requests_get, status_code, expected_result) -> None:
    """Test for the query_api function"""

    mock_response = MagicMock()
    if status_code == 200:
        mock_response.json.return_value = {"key": "value"}
    else:
        mock_response.json.return_value = None
    mock_response.status_code = status_code
    mock_requests_get.return_value = mock_response
    result = query_api(url="http://example.com/api", headers={}, timeout=20)
    assert result == expected_result


@patch(
    "utils.requests.get",
    side_effect=requests.exceptions.RequestException("Error"),
)
def test_exception_query_api(mock_requests_get):
    """Error handling test for quey_api"""

    result = query_api(url="http://example.com/api", headers={}, timeout=20)
    assert result is None


def test_load_json_file():
    """Test for the load_json_file function"""
    data = {"key": "value"}
    assert load_json_file("tests/test.json") == data

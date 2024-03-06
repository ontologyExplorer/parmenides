"""utils functions"""

import json
from typing import Any


def load_json_file(path: str) -> dict[str, Any]:
    """
    Load and parse a JSON file from the specified path.

    Parameters:
    - path (str): The path to the JSON file.

    Returns:
    - dict[str, Any]: A dictionary representing the parsed JSON data.
    """
    with open(path, "r", encoding="utf-8") as file_:
        return json.load(file_)

"""utils functions"""

import json
import os
from typing import Any


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

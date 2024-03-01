import json


def load_config(config_path: str) -> dict:
    """
    Read the configuration file

    Args:
        config_path (str): The path to the configuration file.

    Returns:
        dict: Configuratino parameters
    """
    with open(config_path, "r", encoding="utf-8") as file:
        return json.load(file)

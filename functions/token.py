import json

import requests


class AccessTokenRetriever:
    
    """ 
    Retrieving the Token Access for the API.
    Before using this application be sure to create an account at https://smt.esante.gouv.fr.
    The method get_access_token will send a POST request to the API using the specific https://smt.esante.gouv.fr user's credentials.

    Attributes:
        query_token_url (str): The URL of the token endpoint.
        client_id (str): The client ID for authentication.
        refresh_token (str): The refresh token for authentication.
        content_type (str): The content type for HTTP headers.

    Method:
        get_access_token(mail,password)
    """

    def __init__(self, config_path="functions/config_token.json"):

        """
        Initializes the AccessTokenRetriever using a configuration file.

        Args:
            config_path (str): The path to the configuration file.
        """
        self.config = self.load_config(config_path)
        self.query_token_url = self.config["query_token_url"]
        self.client_id = self.config["client_id"]
        self.refresh_token = self.config["refresh_token"]
        self.content_type = self.config["content_type"]

    def load_config(self, config_path: str)->dict:
        """
        Read the configuration file
        
        Args:
            config_path (str): The path to the configuration file.

        Returns:
            dict: Configuratino parameters
        """
        with open(config_path, "r") as file:
            return json.load(file)

    def get_access_token(self, mail: str, password: str) -> str|None:
        """
        Send a POST request to the API using the specific https://smt.esante.gouv.fr user's credentials

        Args:
            mail (str): User's mail 
            password (str):User's password

        Returns:
            token (str): connection token
        """
        headers = {"Content-Type": self.content_type}

        data = {
            "grant_type": "password",
            "client_id": self.client_id,
            "username": f"{mail}",
            "password": f"{password}",
            "refresh_token": self.refresh_token,
        }

        try:
            response = requests.post(self.query_token_url, headers=headers, data=data)
            response.raise_for_status()
            result = json.loads(response.text)
            return result["access_token"]
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None
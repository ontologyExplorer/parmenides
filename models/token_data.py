"""Models for the ANS API token"""

from pathlib import Path

from pydantic import BaseModel, EmailStr

from utils import load_json_file


class ReadConfig(BaseModel):
    """the ReadConfig Data class"""

    config: dict[str, str] = load_json_file(Path("config", "token.json"))


class TokenData(BaseModel):
    """the TokenData class"""

    email: EmailStr
    password: str
    grant_type: str = "password"
    refresh_token: str = ReadConfig().config["refresh_token"]
    client_id: str = ReadConfig().config["client_id"]

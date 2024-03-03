"""Models for the ANS API token"""

from pathlib import Path

from pydantic import BaseModel, EmailStr

from utils import load_config


class ReadConfig(BaseModel):
    """the ReadConfig class"""

    config: dict[str, str] = load_config(Path("config/token.json"))  # type: ignore


class TokenData(BaseModel):
    """the TokenData class"""

    email: EmailStr
    password: str
    grant_type: str = "password"
    refresh_token: str = ReadConfig().config["refresh_token"]
    client_id: str = ReadConfig().config["client_id"]

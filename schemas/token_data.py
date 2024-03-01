from pydantic import EmailStr, BaseModel
from bla.utils import load_config


class ReadConfig(BaseModel):
    """the ReadConfig class"""

    config: dict[str, str] = load_config("functions/config_token.json")


class TokenData(BaseModel):
    """the TokenData class"""

    email: EmailStr
    password: str
    grant_type: str = "password"
    refresh_token: str = ReadConfig().config["refresh_token"]
    client_id: str = ReadConfig().config["client_id"]

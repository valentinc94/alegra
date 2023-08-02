from dataclasses import dataclass


@dataclass
class ApiConfig:
    username: str
    token_auth: str
    api_base_url: str
    api_version: str = ""

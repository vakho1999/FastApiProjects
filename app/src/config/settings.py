# from typing import Optional
# import os
#
# from fastapi_keycloak import FastAPIKeycloak
import os
from dataclasses import field

from pydantic import BaseSettings, Field, PostgresDsn

from dotenv import load_dotenv
load_dotenv(".env")
from pydantic.class_validators import Optional


class KeycloakSettings(BaseSettings):
    server_url: str
    client_id: str
    client_secret: str
    admin_client_secret: str
    realm: str
    callback_uri: str


class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    mode: str
    SQLALCHEMY_DATABASE_URL: Optional[str] = Field(default="")

    # idp = FastAPIKeycloak(**KeycloakSettings().dict())
    # """setting correct db path for either dev and prod"""
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        # super().__init__(Settings)
        db_url = "postgresql://{database_username}:{database_password}@{database_hostname}:{database_port}/{database_name}"
        self.mode = os.getenv("mode")
        self.database_hostname = os.getenv("database_hostname")
        self.database_port = os.getenv("database_port")
        self.database_password = os.getenv("database_password")
        self.database_name = os.getenv("database_name")
        self.database_username = os.getenv("database_username")
        self.SQLALCHEMY_DATABASE_URL = db_url.format(**self.dict())

        if self.mode == "dev":
            self.SQLALCHEMY_DATABASE_URL += "_test"

    """setting env file path"""

    class Config:
        env_file = ".env"




settings = Settings()

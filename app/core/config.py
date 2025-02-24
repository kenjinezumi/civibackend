# app/core/config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "CiviBackend"
    SQLALCHEMY_DATABASE_URI: str  


    class Config:
        env_file = ".env"  # load from .env if present

settings = Settings()

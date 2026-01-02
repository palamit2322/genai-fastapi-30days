from  pydantic_settings import BaseSettings
from functools import lru_cache
import os

class Settings(BaseSettings):
    ENV: str="dev"
    OPENAI_API_KEY: str
    MODEL_NAME: str
    TEMPERATURE: float=0.7

    class Config():
        env_file=f"env/.env.{os.getenv('dev','prod')}"
        case_sensitive=True

@lru_cache
def get_settings():
    return Settings()

from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    openai_api_key: Optional[str] = None
    openai_model: str = 'gpt-4o-mini'
    openai_temperature: float = 0.7
    max_tokens: int = 2000
    function_calling: bool = True
    database_url: str = 'sqlite:///./assistant.db'
    log_level: str = 'INFO'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        extra = 'ignore'


settings = Settings()
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # Database settings
    database_url: str = "postgresql+asyncpg://postgres:postgres@db:5432/user"
    
    # Security settings
    secret_key: str = "supersecretkey"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # Redis settings
    redis_url: str = "redis://localhost:6379"
    cache_ttl: int = 300
    
    # Celery settings
    celery_broker_url: str = "redis://redis:6379/0"
    celery_result_backend: str = "redis://redis:6379/0"
    
    # Application settings
    app_host: str = "0.0.0.0"
    app_port: int = 8000
    debug: bool = False
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


# Create global settings instance
settings = Settings() 
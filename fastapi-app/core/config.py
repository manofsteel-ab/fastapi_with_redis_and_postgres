from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    postgres_url: str = "postgresql://user:password@localhost:5432/mydatabase"
    redis_url: str = "redis://localhost:6379/0"

    class Config:
        env_file = ".env"

settings = Settings()

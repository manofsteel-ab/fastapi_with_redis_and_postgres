from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    REDIS_URL: str
    # Add other configuration variables here

    class Config:
        env_file = ".env"

settings = Settings()

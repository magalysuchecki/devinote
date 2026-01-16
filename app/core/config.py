from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = Field(
        ...,  # obligatorio
        env="DATABASE_URL",
    )
    JWT_SECRET: str = Field(..., env="JWT_SECRET")
    JWT_ALGORITHM: str = Field(default="HS256", env="JWT_ALGORITHM")
    JWT_EXPIRES_MIN: int = Field(default=60 * 24, env="JWT_EXPIRES_MIN")
    PROJECT_NAME: str = "Devinote"

    class Config:
        env_file = ".env"


settings = Settings()

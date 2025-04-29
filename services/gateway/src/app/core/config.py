from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    USERS_SERVICE_URL: str = "http://users:8001/api/v1/auth"
    JWT_SECRET_KEY: str = "your_secret_key"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"


settings = Settings()

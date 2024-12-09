from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = 'sqlite:///db.sqlite3'

    APP_NAME: str
    APP_VERSION: str
    APP_DESCRIPTION: str
    APP_SLUG: str


settings = Settings()

from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_FILE = Path(__file__).parent.parent / '.env'


class Settings(BaseSettings):

    db_host: str = Field(default='localhost', env='DB_HOST')
    db_port: int = Field(default=5432, env='DB_PORT')
    db_name: str = Field(default='db_name', env='DB_NAME')
    db_user: str = Field(default='db_user', env='DB_USER')
    db_pass: str = Field(default='db_pass', env='DB_PASS')

    db_url: str = f'postgres+asyncpg://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'

    model_config = SettingsConfigDict(env_file=ENV_FILE)


settings = Settings()

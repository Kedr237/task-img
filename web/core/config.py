from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    project_name: str = 'test-img'

    db_host: str = Field(default='localhost', env='DB_HOST')
    db_port: int = Field(default=5432, env='DB_PORT')
    db_name: str = Field(default='db_name', env='DB_NAME')
    db_user: str = Field(default='db_user', env='DB_USER')
    db_pass: str = Field(default='db_pass', env='DB_PASS')

    @property
    def db_url(self) -> str:
        return f'postgresql+asyncpg://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}'


settings = Settings()

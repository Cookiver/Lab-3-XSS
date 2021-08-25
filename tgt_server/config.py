from pydantic import BaseSettings


class Settings(BaseSettings):
    api_log_level: str = 'info'
    api_v1_str: str = ''
    api_base: str = '/'
    api_host: str = '0.0.0.0'
    api_port: int = 5000
    autoescape: bool = False
    unsafe_edit_pages = False


settings = Settings()

from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    api:str
    class Config:
        env_file = '.env'


settings = Settings()
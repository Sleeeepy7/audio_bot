from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    bot_token: str
    max_audio_duration: int = 180 # макс длительность аудио в секундах

    class Config:
        env_file = ".env"

settings = Settings()
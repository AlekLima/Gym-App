from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Gym App"
    API_V1_STR: str = "/api/v1"
    DATABASE_URL: str = "postgresql://gymapp:gymapp_password@localhost/gymapp"
    SECRET_KEY: str = "your-secret-key-here"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    
    class Config:
        case_sensitive = True

settings = Settings()
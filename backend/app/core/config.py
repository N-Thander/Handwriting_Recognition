import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    UPLOAD_FOLDER: str = os.path.join("app", "static", "uploaded_files")
    MODEL_PATH: str = os.path.join("models", "handwriting_model.h5")
    ALLOWED_EXTENSIONS: set = {"jpg", "jpeg", "png"}

    class Config:
        env_file = ".env"

settings = Settings()

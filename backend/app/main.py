from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.routes import router
from app.core.config import settings
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

os.makedirs(settings.UPLOAD_FOLDER, exist_ok=True)

app.include_router(router, prefix="/api")

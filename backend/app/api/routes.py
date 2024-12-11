from fastapi import APIRouter, UploadFile, File
from app.core.config import settings
from app.core.model import HandwritingModel
import os
import shutil

router = APIRouter()
model = HandwritingModel()

@router.post("/predict/")
async def predict(file: UploadFile = File(...)):
    if file.filename.split(".")[-1].lower() not in settings.ALLOWED_EXTENSIONS:
        return {"error": "Invalid file format. Only JPG, JPEG, and PNG are supported."}

    file_path = os.path.join(settings.UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    prediction = model.predict(file_path)
    return {"filename": file.filename, "prediction": prediction}

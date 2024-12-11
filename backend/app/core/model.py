from tensorflow.keras.models import load_model
import numpy as np
from app.utils.preprocessing import preprocess_image
from app.utils.postprocessing import decode_prediction
from app.core.config import settings

class HandwritingModel:
    def __init__(self):
        self.model = load_model(settings.MODEL_PATH)

    def predict(self, image_path: str) -> str:
        preprocessed_image = preprocess_image(image_path)
        prediction = self.model.predict(preprocessed_image)
        return decode_prediction(prediction)

import cv2
import numpy as np

def preprocess_image(image_path: str):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (256, 64))
    image = image / 255.0
    image = np.expand_dims(image, axis=-1)
    return np.expand_dims(image, axis=0)

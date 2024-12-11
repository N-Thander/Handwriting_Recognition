from app.core.model import HandwritingModel

def test_model_prediction():
    model = HandwritingModel()
    prediction = model.predict("path_to_test_image.jpg")
    assert isinstance(prediction, str)

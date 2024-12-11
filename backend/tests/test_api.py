from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict_endpoint():
    with open("path_to_test_image.jpg", "rb") as f:
        response = client.post("/api/predict/", files={"file": ("test.jpg", f, "image/jpeg")})
    assert response.status_code == 200
    assert "prediction" in response.json()

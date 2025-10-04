# api_tests.py
from app import app
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200

def test_predict_endpoint():
    client = app.test_client()
    data = {"Make":"Toyota","Model":"Corolla","Year":2019}
    response = client.post("/predict", json=data)
    assert response.status_code == 200


from fastapi.testclient import TestClient
from src.functions.crud_function import app


client = TestClient(app)

def test_read_items():
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == [{
            "name": "santi",
            "id": 1, 
            "email": "santii@gmail.com"
        }]
    
    
from fastapi.testclient import TestClient
from src.functions.crud_function import app  # Asume que tu aplicación FastAPI se llama main.py

client = TestClient(app)

def test_read_items():
    response = client.get("/api/v1/users/items")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_item():
    response = client.post("/api/v1/users/items", json={"name": "santi", "id": 1, "email": "santii@gmail.com"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "santi"
    assert "id" in data

def test_update_item():
    # Primero, crea un item para tener algo que actualizar.
    create_response = client.post("/api/v1/users/items", json={"name": "santi", "id": 1, "email": "santii@gmail.com"})
    item_id = create_response.json()["id"]
    response = client.put(f"/api/v1/users/items/{item_id}", json={"name": "santi o", "id": 1, "email": "santiago@gmail.com", "id": item_id})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "santi o"
    assert data["id"] == item_id

def test_delete_item():
    # Primero, crea un item para después eliminarlo.
    create_response = client.post("/api/v1/users/items", json={"name": "santi", "id": 1, "email": "santii@gmail.com"})
    item_id = create_response.json()["id"]
    response = client.delete(f"/api/v1/users/items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Item deleted"

def test_math_operation():
    num = 4
    response = client.get(f"/api/v1/users/math/{num}")
    assert response.status_code == 200
    assert response.json() == num * num
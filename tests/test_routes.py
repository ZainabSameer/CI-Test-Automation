from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check_status_code():
    response = client.get("/health")
    assert response.status_code == 200

def test_health_check_content():
    response = client.get("/health")
    assert response.json() == {"status": "ok"}

def test_health_invalid_path():
    response = client.get("/healthz")
    assert response.status_code == 404


def test_hello_with_name():
    response = client.get("/hello/Zainab")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Zainab!"}

def test_hello_with_another_name():
    response = client.get("/hello/Mohamed")
    assert response.json() == {"message": "Hello, Mohamed!"}

def test_hello_missing_name():
    response = client.get("/hello/")  
    assert response.status_code == 404



def test_create_item_valid():
    response = client.post("/items", json={"name": "Book", "price": 12.5})
    assert response.status_code == 200
    assert response.json() == {"item": {"name": "Book", "price": 12.5}}

def test_create_item_missing_field():
    response = client.post("/items", json={"name": "Book"})
    assert response.status_code == 422  

def test_create_item_invalid_price():
    response = client.post("/items", json={"name": "Book", "price": "not-a-number"})
    assert response.status_code == 422  

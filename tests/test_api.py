from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "active"}

def test_create_sensor():
    response = client.post("/sensors", params={"name": "sensor1", "type": "temperatura"})
    assert response.status_code == 200

def test_get_sensors():
    response = client.get("/sensors")
    assert response.status_code == 200

def test_create_reading_valido():
    response = client.post("/readings", json={
        "sensor_id": 1,
        "sensor_type": "temperatura",
        "value": 25.5,
        "unit": "°C"
    })
    assert response.status_code == 200

def test_create_reading_invalido_unidad():
    response = client.post("/readings", json={
        "sensor_id": 1,
        "sensor_type": "temperatura",
        "value": 25.5,
        "unit": "%"
    })
    assert response.status_code == 422

def test_create_reading_fuera_de_rango():
    response = client.post("/readings", json={
        "sensor_id": 1,
        "sensor_type": "temperatura",
        "value": 200,
        "unit": "°C"
    })
    assert response.status_code == 422

def test_get_readings():
    response = client.get("/readings")
    assert response.status_code == 200
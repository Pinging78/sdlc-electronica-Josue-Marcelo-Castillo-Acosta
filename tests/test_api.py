from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "active"}

def test_create_sensor(client):
    response = client.post("/sensors", params={"name": "sensor1", "type": "temperatura"})
    assert response.status_code == 200

def test_get_sensors(client):
    response = client.get("/sensors")
    assert response.status_code == 200

def test_create_reading_valido(client):
    response = client.post("/readings", json={
        "sensor_id": 1,
        "sensor_type": "temperatura",
        "value": 25.5,
        "unit": "°C"
    })
    assert response.status_code == 200

def test_create_reading_invalido_unidad(client):
    response = client.post("/readings", json={
        "sensor_id": 1,
        "sensor_type": "temperatura",
        "value": 25.5,
        "unit": "%"
    })
    assert response.status_code == 422

def test_create_reading_fuera_de_rango(client):
    response = client.post("/readings", json={
        "sensor_id": 1,
        "sensor_type": "temperatura",
        "value": 200,
        "unit": "°C"
    })
    assert response.status_code == 422

def test_get_readings(client):
    response = client.get("/readings")
    assert response.status_code == 200

#5 tests nuevos
def test_get_sensor_not_found(client):
    response = client.get("/sensors/99999")
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()

def test_delete_sensor_not_found(client):
    response = client.delete("/sensors/99999")
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()

def test_get_sensor_found(client):
    create_response = client.post("/sensors", params={"name": "sensor_test", "type": "humedad"})
    sensor_id = create_response.json()["id"]
    response = client.get(f"/sensors/{sensor_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "sensor_test"

def test_delete_sensor_found(client):
    create_response = client.post("/sensors", params={"name": "sensor_borrar", "type": "temperatura"})
    sensor_id = create_response.json()["id"]
    response = client.delete(f"/sensors/{sensor_id}")
    assert response.status_code == 200

def test_root_endpoint(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
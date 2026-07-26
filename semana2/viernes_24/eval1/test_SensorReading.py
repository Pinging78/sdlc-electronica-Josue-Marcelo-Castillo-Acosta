from SensorReading import SensorReading

def test_crear_lectura_valida():
    lectura = SensorReading(sensor_id="S1", temperatura=25.5, humedad=60.0)
    assert lectura.sensor_id == "S1"
    assert lectura.temperatura == 25.5
    assert lectura.humedad == 60.0
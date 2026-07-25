# test_sensor_registry.py
from SensorRegistry import SensorRegistry

def test_registrar_sensor():
    registry = SensorRegistry()
    registry.registrar(sensor_id="S1", tipo="temperatura", ubicacion="zona-A")
    assert registry.existe("S1")
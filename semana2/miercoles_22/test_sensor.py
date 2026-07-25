from SensorRegistry import SensorRegistry

#no tiene conflicto con la nueva clase 
def test_registrar_sensor():
    registry = SensorRegistry()
    registry.registrar(sensor_id="S1", tipo="temperatura", ubicacion="zona-A")
    assert registry.existe("S1")
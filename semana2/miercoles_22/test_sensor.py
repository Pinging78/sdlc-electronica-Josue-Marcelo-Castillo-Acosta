from SensorRegistry import SensorRegistry

#GREEN ahora con la clase definida ya puede funcionar
def test_registrar_sensor():
    registry = SensorRegistry()
    registry.registrar(sensor_id="S1", tipo="temperatura", ubicacion="zona-A")
    assert registry.existe("S1")
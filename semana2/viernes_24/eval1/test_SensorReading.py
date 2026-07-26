import pytest
from SensorReading import SensorReading

def test_temperatura_invalida_lanza_error():
    with pytest.raises(ValueError): #espera que mande un error y lo manda si pasa el test, si no lo manda o es otro falla el test
        SensorReading(sensor_id="S1", temperatura="no-numero", humedad=60.0)
#pytest.raises es para confirmar si se lanzo el error esperado

def test_crear_lectura_valida():
    lectura = SensorReading(sensor_id="S1", temperatura=25.5, humedad=60.0)
    assert lectura.sensor_id == "S1" #verifica si son los datos
    assert lectura.temperatura == 25.5
    assert lectura.humedad == 60.0

def test_marca_sensor_sin_respuesta_tras_reintentos():
    intentos = [None, None, None]  # simula 3 fallos seguidos
    resultado = intentar_leer_sensor(intentos, max_intentos=3)
    assert resultado is None  # se agotaron los reintentos

def intentar_leer_sensor(lecturas_simuladas, max_intentos=3):
    for intento in lecturas_simuladas[:max_intentos]: #si no responde en 3 intentos
        if intento is not None:
            return intento #realiza un ciclo si responde lo regresa y se detiene
    return None #si no lo hace en esas 3 veces regresa None que es que se agotaron los reintentos
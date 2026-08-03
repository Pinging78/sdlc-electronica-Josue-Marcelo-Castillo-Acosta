from reading import Reading, SensorType, celsius_to_fahrenheit, humedad_a_porcentaje, alerta_temperatura_alta, alerta_humedad_baja, to_dict

#1
def test_celsius_to_fahrenheit(): #se define la función de prueba para convertir de Celsius a Fahrenheit
    lectura = Reading("TEMP-01", 25.0, SensorType.TEMPERATURE)  # se crea una lectura de temperatura y se asigna el valor de 25°C
    resultado = celsius_to_fahrenheit(lectura)                   # se convierte el valor
    assert resultado.value == 77.0                                # compruebo: ¿de verdad dio 77°F?

#2
def test_humedad_a_porcentaje(): #se define la función de prueba para convertir de humedad a porcentaje
    lectura = Reading("HUM-01", 0.45, SensorType.HUMIDITY) #valores del sensor
    resultado = humedad_a_porcentaje(lectura) #se convierte el valor
    assert resultado.value == 45.0 #comprueba el resultado

#3
def test_alerta_temperatura_alta_true(): #se define para comprobar si la alerta funciona
    lectura = Reading("TEMP-01", 35.0, SensorType.TEMPERATURE)#valores del sensor
    assert alerta_temperatura_alta(lectura) is True #comprueba si es verdadero o falso dependiendo del umbral


def test_alerta_temperatura_alta_false():
    lectura = Reading("TEMP-01", 22.0, SensorType.TEMPERATURE)
    assert alerta_temperatura_alta(lectura) is False #comprueba si es verdadero o falso

#4
def test_alerta_humedad_baja_true(): #se define para comprobar si la alerta funciona
    lectura = Reading("HUM-01", 15.0, SensorType.HUMIDITY) #valores del sensor
    assert alerta_humedad_baja(lectura) is True #comprueba si es verdadero o falso


def test_alerta_humedad_baja_false():
    lectura = Reading("HUM-01", 40.0, SensorType.HUMIDITY)
    assert alerta_humedad_baja(lectura) is False

#5
def test_to_dict(): #se define la función de prueba para convertir un objeto Reading a un diccionario
    lectura = Reading("TEMP-01", 25.0, SensorType.TEMPERATURE) #valores del sensor
    resultado = to_dict(lectura) #convierte el reading a un diccionario
    assert resultado == {
        "sensor_id": "TEMP-01",
        "value": 25.0,
        "sensor_type": "TEMPERATURE",
    } #comprueba el resultado
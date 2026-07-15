# [14/07/2026] — Semana 1 / Lunes — Funciones puras sobre Reading
## Herramienta usada: Claude / Gemini

## Prompt: Dame ideas de 5 funciones puras sobre reading (conversion de unidades, deteccion de umbral, serializacion) en base a este codigo (codigo proporcionado en la guia del estudiante)

Claude propuso varias ideas como coversion de celsius a farenheit o al reves, si pasaba el umbral o si estaba dentro de un rango y convertir el reading a un diccionario

Y de una forma más visual lo hizo de esta forma:
    Lectura original: Reading(sensor_id='TEMP-01', value=25.0, sensor_type=<SensorType.TEMPERATURE: 1>)
    En Fahrenheit: Reading(sensor_id='TEMP-01', value=77.0, ...)
    De vuelta a Celsius: Reading(sensor_id='TEMP-01', value=25.0, ...)   ← ida y vuelta, coincide

    ¿Excede 30 grados? False
    ¿Excede 20 grados? True
    ¿Esta entre 20 y 30? True

    Como diccionario: {'sensor_id': 'TEMP-01', 'value': 25.0, 'sensor_type': 'TEMPERATURE'}

Gemini por otro lado me dio un ejemplo, el cual no me gusto por que principalmente senti que estaba poniendo cosas irrelevantes como por ejemplo estas lineas:

class Transport(Protocol):
    def send(self, payload: bytes) -> None: ...

def to_frame(r: Reading) -> bytes:
    return f"{r.sensor_id}:{r.value:.2f}".encode()

def celsius_to_fahrenheit(r: Reading) -> Reading:
    """Ejercicio 1: Convierte la temperatura a Fahrenheit si corresponde."""
    if r.sensor_type != SensorType.TEMPERATURE:
        return r
    
    nuevo_valor = (r.value * 1.8) + 32
    # Al ser frozen=True, usamos 'replace' para clonar el objeto con el nuevo valor
    return replace(r, value=nuevo_valor)

Por lo que lo deje de lado mejor y me regrese a claude para ver una mejor propuesta y obtuve este codigo:

def to_csv_line(r: Reading) -> str:
    """Convierte una Reading a una linea CSV: sensor_id,value,tipo"""
    return f"{r.sensor_id},{r.value:.2f},{r.sensor_type.name}"

El cual aunque no vaya a usar un csv es una funcion más costa y sencilla, por lo que me decante a hacer un codigo con esta base

Despues de eso le pedi que me explicara ciertas funciones y son estas:
- qué es dataclass, frozen, Enum y el patrón Arrange-Act-Assert y como hacerlo correctamente


### ¿Qué hice yo?
Fui adaptando estos ejemplos de poco en poco teniendo cuidado por posibles errores, todo en torno a los sensores de humedad y temperatura para hacerlo mas facil, en caso de tener duda o problemas consultaba a la IA para saber que es lo que estaba haciendo mal (regularmente por escribir algo mal)

Al final corrí mypy y ruff para verificar el código, y despues de varios intentos funciono


### ¿Qué aprendí?
El funcionamiento de la funcion `replace()` en dataclasses inmutables, que en pocas palabras en lugar de sobre escribir la lectura crea una nueva continuamente y utilizar el Patrón Arrange-Act-Assert para escribir pruebas o realizar acciones de una manera facil que a mi parecer es muy sencillo y muy buena opcion
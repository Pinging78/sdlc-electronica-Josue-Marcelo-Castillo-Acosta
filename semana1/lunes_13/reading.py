from dataclasses import dataclass, replace
from enum import Enum, auto
#from typing import Protocol

class SensorType(Enum): #se define una enumeración para los tipos de sensores
    TEMPERATURE = auto() #se define automaticamente el valor de TEMPERATURE
    HUMIDITY = auto() #se define automaticamente el valor de HUMIDITY

@dataclass(frozen=True) #una vez que se cree el objeto no se puede modificar los valores de sus atributos (inmutable)
#si se modifica marcará error
class Reading: #se define la clase de lectura del sensor
    sensor_id: str #se define el ID del sensor
    value: float #se define el valor de la lectura
    sensor_type: SensorType #se define el tipo de sensor

#1
def celsius_to_fahrenheit(r: Reading):      #se define la función que recibe un objeto de tipo Reading
    if r.sensor_type != SensorType.TEMPERATURE: #verifica si el sensor es de temperatura
        raise ValueError("Esto solo es aplicable a lecturas de temperatura") #si no lo es manda este mensaje
    nuevo_valor = (r.value * 9/5) + 32 #convierte el valor del sensor de Celsius a Fahrenheit
    return replace(r, value=nuevo_valor) # retorna un nuevo objeto Reading con el valor convertido a Fahrenheit 

#2 
def humedad_a_porcentaje(r: Reading): #se define la función que recibe un objeto de tipo Reading
    if r.sensor_type != SensorType.HUMIDITY: #verifica si el sensor es de humedad
        raise ValueError("Esto solo es aplicable a lecturas de humedad") #si no lo es manda este mensaje
    nuevo_valor = r.value * 100 #convierte el valor del sensor a porcentaje
    return replace(r, value=nuevo_valor) #retorna un nuevo objeto Reading con el valor convertido a porcentaje

#3
def alerta_temperatura_alta(r: Reading, umbral: float = 30.0) -> bool: #se define el tipo reading y un umbral por defecto de 30.0°C
    if r.sensor_type != SensorType.TEMPERATURE: #verifica si el sensor es de temperatura
        raise ValueError("Solo aplica a lecturas de temperatura") #si no lo es manda este mensaje
    return r.value > umbral #retorna true si es mayor al umbral y false si es menor o igual 

#4
def alerta_humedad_baja(r: Reading, umbral: float = 20.0) -> bool: #se define el tipo reading y un umbral por defecto de 20.0%
    if r.sensor_type != SensorType.HUMIDITY: #sensor tipo humedad
        raise ValueError("Solo aplica a lecturas de humedad")
    return r.value < umbral #retorna true si es menor al umbral y false si es mayor o igual

#5
def to_dict(r: Reading) -> dict[str, str | float]: #se define tipo reading y retorna los valores en un diccionario con claves de tipo string
    return { 
        "sensor_id": r.sensor_id,
        "value": r.value,
        "sensor_type": r.sensor_type.name,
    } #retorna un diccionario con los datos del sensor
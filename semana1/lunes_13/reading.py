from dataclasses import dataclass, replace
from enum import Enum, auto
#from typing import Protocol

class SensorType(Enum): #se define una enumeración para los tipos de sensores
    TEMPERATURE = auto() #se define automaticamente el valor de TEMPERATURE
    HUMIDITY = auto() #se define automaticamente el valor de HUMIDITY

@dataclass #se define una clase de datos para representar una lectura del sensor
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
def alerta_temperatura_alta(r: Reading, umbral: float = 30.0) -> bool:
    if r.sensor_type != SensorType.TEMPERATURE:
        raise ValueError("Solo aplica a lecturas de temperatura")
    return r.value > umbral

#4
def alerta_humedad_baja(r: Reading, umbral: float = 20.0) -> bool:
    if r.sensor_type != SensorType.HUMIDITY:
        raise ValueError("Solo aplica a lecturas de humedad")
    return r.value < umbral

#5
def to_dict(r: Reading) -> dict[str, str | float]:
    return {
        "sensor_id": r.sensor_id,
        "value": r.value,
        "sensor_type": r.sensor_type.name,
    }
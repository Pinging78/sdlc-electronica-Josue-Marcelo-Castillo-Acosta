from dataclasses import dataclass


@dataclass #genera automaticamente el __init__
class SensorReading: 
    sensor_id: str
    temperatura: float
    humedad: float

    def __post_init__(self): #dataclass lo llama despues del __init__ generado
        if not isinstance(self.temperatura, (int, float)): 
    #pregunta si es entero o decimal e invierte la respuesta y pasa a preguntar no es un numero?
            raise ValueError("temperatura debe ser numérica") #si no es un numero manda un error
        if not isinstance(self.humedad, (int, float)):
            raise ValueError("humedad debe ser numérica")
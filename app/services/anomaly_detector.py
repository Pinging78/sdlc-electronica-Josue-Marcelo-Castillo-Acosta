UMBRALES = {
    "temperatura": 35,
    "humedad": 80,
}

#clase basica para que funcione correctamente los test
class AnomalyDetector:
    def es_anomalia(self, tipo_sensor: str, value: float) -> bool:
        umbral = UMBRALES.get(tipo_sensor)
        if umbral is None:
            return False
        return value > umbral
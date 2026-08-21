from enum import Enum


class Nivel(str, Enum):
    OK = "OK"
    WARNING = "WARNING"
    CRITICAL = "CRITICAL"


# umbrales dobles por tipo de sensor: WARNING es la alerta temprana,
# CRITICAL es la que de verdad importa
UMBRALES = {
    "temperatura": {"warning": 35, "critical": 45},
    "humedad": {"warning": 80, "critical": 90},
}


class AnomalyDetector:
    def evaluar(self, tipo_sensor: str, value: float) -> Nivel:
        umbral = UMBRALES.get(tipo_sensor)
        if umbral is None:
            return Nivel.OK
        if value > umbral["critical"]:
            return Nivel.CRITICAL
        if value > umbral["warning"]:
            return Nivel.WARNING
        return Nivel.OK

    def es_anomalia(self, tipo_sensor: str, value: float) -> bool:
        # se mantiene por compatibilidad con codigo/tests existentes
        return self.evaluar(tipo_sensor, value) != Nivel.OK
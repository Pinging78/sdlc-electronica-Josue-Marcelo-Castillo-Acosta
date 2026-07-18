# [15/07/2026] — Semana 1 / Miercoles — SOLID en la practica: S, O y L

## Herramienta usada: Claude 

## Prompt: en base al codigo base (codigo de la guia del estudiante) dame un ejemplo bueno y malo de un principio

Aqui me lo puso en resumen de cada uno los cuales se me hicieron interesantes en particular 2 

def notificar_anomalia(alert: AlertStrategy,    reading: SensorReading, threshold: float) -> None:
    detector = AnomalyDetector(alert=alert, threshold=threshold)
    detector.check(reading)

class ConsoleAlertMalaI(AlertStrategyGordaMalaI):
    def send(self, message: str) -> None:
        print(message)
 
    def retry(self, message: str, intentos: int) -> None:
        raise NotImplementedError("consola no reintenta, no aplica")

que los ocupe como base para hacer las demas funciones, las otras senti que eran muy complicadas de entender y mejor las descarte

### ¿En qué me ayudó?
a solucionar dudas al respecto del abstract y las clases que todavia no comprendia bien como se utilizaban

### ¿Qué hice yo?
formar el codigo basandome en la misma estructura para que fuera más sencillo tanto para mi como para el lector verlo

### ¿Qué aprendí?
como puedo usar correctamente las clases y el abstract
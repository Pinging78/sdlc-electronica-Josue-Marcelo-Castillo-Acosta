# S - Una clase, una responsabilidad: SensorReader lee; DataLogger persiste.
# O - AlertStrategy (ABC) con ConsoleAlert y FileAlert: agregar EmailAlert
#     manana NO toca el codigo existente.
# L - TemperatureSensor y HumiditySensor son intercambiables donde se espera
#     BaseSensor: process_sensor(sensor: BaseSensor) funciona con cualquiera.
from abc import ABC, abstractmethod
from dataclasses import dataclass
#abc y abstractmethod se usa para crear moldes o funciones que solo se pueden heredar
#dataclass solo es para evitar el __init__ cuando una clase solo guarda datos

@dataclass(frozen = True) #la hace inmutable
class SensorReading:
    sensor_id: str #datos del sensor
    value: float

class BaseSensor(ABC):
    @abstractmethod  #obliga a que cualquier clase que se herede debe implementar
    def read(self) -> SensorReading: ... #un metodo read() como obligación


class TemperatureSensor(BaseSensor): #funcion heredada
    def __init__(self, sensor_id: str, value: float) ->None:
        self._sensor_id = sensor_id #datos sensor
        self._value = value

    def read(self) -> SensorReading: #@abstract con funcion read()
        return SensorReading(self._sensor_id, self._value)

class AlertStrategy(ABC): #lo mismo que BaseSensor pero dirigido a las alertas
    @abstractmethod
    def send(self, message: str) -> None: ...


# S - Single Responsibility (una clase, una razon para cambiar)
#ejemplo bueno: detecta la anomalia, deja el envio a quien implemente el AlertStrategy y solo tiene que comparar con el threshold
#solo detecta el error y lo manda
class AnomalyDetectorB:
    def __init__(self, alert: AlertStrategy, threshold: float) -> None:
        self._alert = alert 
        self._threshold = threshold
 
    def check(self, reading: SensorReading) -> None:
        if reading.value > self._threshold: #self._alert decide a quien le pasa el mensaje
            self._alert.send(f"Anomalia en {reading.sensor_id}")

#ejemplo malo: detecta la anomalia, pero arma el texto y lo imprime
class AnomalyDetectorM:
    def __init__(self, threshold: float) -> None:
        self._threshold = threshold
 
    def check(self, reading: SensorReading) -> None:
        if reading.value > self._threshold:
            texto= f"Anomalia en {reading.sensor_id} (valor={reading.value})"
            print(texto)


#O - Open/Closed (abierto a extension, cerrado a modificacion)
#ejemplo bueno: ConsoleAlert y FileAlert ya existen, EmailAlert se agrega como una clase nueva sin modificar a las anteriores
class ConsoleAlert(AlertStrategy):
    def send(self, message: str) -> None: #se cumple lo del abstrac
        print(message) 

class FileAlert(AlertStrategy):
    def __init__(self, path: str = "alertas.log") -> None:
        self._path = path

    def send(self, message: str) -> None:
        with open(self._path, "error en el archivo") as f:
            f.write(message + "\n") 

class EmailAlert(AlertStrategy):
    def __init__(self, destinatario: str) -> None:
        self._destinatario = destinatario
    def send(self, message: str) -> None:
        print(f"[EMAIL a {self._destinatario}]{message}")


#ejemplo malo: para agregar un canal de alerta nuevo se tiene que modificar el elif
def enviar_alerta_mala(canal: str, mensaje: str) -> None:
    if canal == "console":
        print(mensaje)
    elif canal == "file":
        with open("alertas.log", "a") as f:
            f.write(mensaje + "\n")


#L - Liskov Substitution (una subclase debe poder sustituir a su base sin romper el comportamiento esperado)
#ejemplo bueno: cualquier AlertStrategy (ConsoleAlert, FileAlert, EmailAlert) pueden sustituirse entre si sin que falle
#el comportamiento esperado por el AnomalyDetector: todas envian el mensaje de una u otra forma
def notificar_anomalia(alert: AlertStrategy, reading: SensorReading, threshold: float) -> None:
    detector = AnomalyDetectorB(alert = alert, threshold = threshold)
    detector.check(reading)

#ejemplo malo: se hereda de AlertStrategy, pero en lugar de enviar el mensaje, envia una excepcion.
#si se llega a sustituir AlertStrategy por esta clase AnomalyDetector.check() deja de funcionar en lugar de notificar
class AlertaMala(AlertStrategy):
    def send(self, message: str) -> None:
        raise RuntimeError("Esto nunca va a funcionar")


#I - Interface Segregation (no obligues a implementar metodos que no usas)
#ejemplo bueno: separa interfaces chicas. AlertStrategy solo pide send(), pero se immplementa RetryableAlert para funciones
#que si lo requieran
class RetryableAlert(ABC):
    @abstractmethod
    def retry(self, message: str, intentos: int) -> None: ...

class EmailAlertConReintento(AlertStrategy, RetryableAlert):
    def __init__(self, destinatario: str) -> None:
        self._destinatario = destinatario

    def send (self, message:str) -> None:
        print(f"[EMAIL a {self._destinatario}] {message}")

    def retry(self, message: str, intentos: int) -> None:
        for _ in range(intentos):
            self.send(message)


# MALO: esta interfaz "gorda" obliga a las alertas a implementar retry() y configure(), aunque a ConsoleAlert no le haga sentido reintentar
# ni configurarse con credenciales.
class AlertStrategyGordaMalaI(ABC):
    @abstractmethod
    def send(self, message: str) -> None: ...
 
    @abstractmethod
    def retry(self, message: str, intentos: int) -> None: ...
 
    @abstractmethod
    def configure(self, credenciales: dict) -> None: ...
 
 
class ConsoleAlertMalaI(AlertStrategyGordaMalaI):
    def send(self, message: str) -> None:
        print(message)
 
    def retry(self, message: str, intentos: int) -> None:
        raise NotImplementedError("consola no reintenta, no aplica")  # forzado a implementarlo igual
 
    def configure(self, credenciales: dict) -> None:
        raise NotImplementedError("consola no necesita credenciales")  # idem


#D - Dependency python3 solid_srp_ocp_lsp.pyacciones, no de clases concretas)
#ejemplo bueno: no necesita


# ejemplo malo:: AnomalyDetector crea su propia ConsoleAlert por dentro. Queda
# amarrado a esa clase concreta 
class AnomalyDetectorMaloD:
    def __init__(self, threshold: float) -> None:
        self._alert = ConsoleAlert()  # dependencia concreta, quemada aqui
        self._threshold = threshold
 
    def check(self, reading: SensorReading) -> None:
        if reading.value > self._threshold:
            self._alert.send(f"Anomalia en {reading.sensor_id}")



#test

class AlertaFalsa(AlertStrategy):
#guarda los mensajes, para verificar en el test sin depender de consola, archivos ni correo real.
     def __init__(self) -> None:
        self.mensajes: list[str] = []
 
     def send(self, message: str) -> None:
        self.mensajes.append(message)
 
 
def test_anomaly_detector_dispara_alerta_si_supera_umbral() -> None:
#Comportamiento base: solo se dispara la alerta si el valor supera el threshold.
    alerta = AlertaFalsa()
    detector = AnomalyDetectorB(alert=alerta, threshold=30.0)
 
    detector.check(SensorReading("temp1", 25.0))
    assert alerta.mensajes == []  # no debio dispararse nada
 
    detector.check(SensorReading("temp1", 40.0))
    assert alerta.mensajes == ["Anomalia en temp1"]
 
 
def test_dependency_inversion_acepta_cualquier_alert_strategy() -> None:
#Verifica D y L al mismo tiempo: AnomalyDetector debe funcionar igual sin importar que implementacion concreta de AlertStrategy ya que depende del abstract
    alerta_falsa = AlertaFalsa()
    reading = SensorReading("hum1", 99.0)
 
    for alerta in (alerta_falsa,):
        detector = AnomalyDetectorB(alert=alerta, threshold=50.0)
        detector.check(reading)
 
    assert alerta_falsa.mensajes == ["Anomalia en hum1"]
 
 
if __name__ == "__main__":
    test_anomaly_detector_dispara_alerta_si_supera_umbral()
    test_dependency_inversion_acepta_cualquier_alert_strategy()
    print("Todos los tests pasaron correctamente.")

from abc import ABC, abstractmethod

class AlertStrategy(ABC):
    @abstractmethod #todas las clases deben de contar con esto
    def enviar(self, mensaje: str) -> None:
        pass

class ConsoleAlertStrategy(AlertStrategy):
    def enviar(self, mensaje: str) -> None: #se crea el mensaje
        print(mensaje) #se manda

class AlertManager:
    def __init__(self, strategy: AlertStrategy): #recibe cualquier strategy que cumpla el molde de AlertStrategy
        self.strategy = strategy

    def notificar(self, mensaje: str) -> None:
        self.strategy.enviar(mensaje) #como se notifica
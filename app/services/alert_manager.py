from abc import ABC, abstractmethod


class AlertStrategy(ABC):
    @abstractmethod
    def enviar(self, mensaje: str) -> None:
        pass


class ConsoleAlertStrategy(AlertStrategy):
    def enviar(self, mensaje: str) -> None:
        print(mensaje)


class FileAlertStrategy(AlertStrategy):
    def __init__(self, path: str):
        self.path = path

    def enviar(self, mensaje: str) -> None:
        with open(self.path, "a") as f:
            f.write(mensaje + "\n")


class AlertManager:
    def __init__(self, strategy: AlertStrategy | None = None):
        self.strategy = strategy or ConsoleAlertStrategy()
        self.alertas: list[str] = []

    def notificar(self, mensaje: str) -> None:
        self.alertas.append(mensaje)
        self.strategy.enviar(mensaje)
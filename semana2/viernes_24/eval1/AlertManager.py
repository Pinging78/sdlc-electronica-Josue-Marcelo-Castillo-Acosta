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

class FileAlertStrategy(AlertStrategy):
    def __init__(self, filepath: str):
        self.filepath = filepath
#se define donde queremos guardar las alertas y se guarda como atributo

    def enviar(self, mensaje: str) -> None:
        with open(self.filepath, "a") as f: #abre el archivo de forma segura y terminando el bloque lo cierra
            f.write(mensaje + "\n") #escribe el mensaje y agrega una linea nueva para el siguiente mensaje
#abre el archivo en la ruta guardada "a" (agregar/append) y cada nueva alerta se agrega
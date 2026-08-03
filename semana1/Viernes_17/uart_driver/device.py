from config import UartConfig
from parsers import MessageParser

class UartDevice: #configuracion del dispositivo
    def __init__(self, config: UartConfig, parser: MessageParser) -> None:
        self._config = config
        self._parser = parser
        self._connected = False
    
    def connect(self) -> None:
        self._connected = True

    def disconnect(self) -> None:
        self._connected = False

    def read_and_parse(self, raw: bytes) -> dict:
        if not self._connected:
            raise RuntimeError("dispositivo desconectado")

        if not self._parser.can_parse(raw):
            raise ValueError("no se pudo parsear el frame recibido")

        return self._parser.parse(raw)

import pytest
from device import UartDevice
from parsers import MessageParser
from config import UartConfig


class DummyParser(MessageParser):
    def __init__(self, valido=True):
        self._valido = valido

    def can_parse(self, raw: bytes) -> bool:
        return self._valido

    def parse(self, raw: bytes) -> dict:
        if not self._valido:
            raise ValueError("frame invalido")
        return {"protocolo": "dummy", "contenido": raw}


CONFIG_DUMMY = UartConfig(baudrate=9600, parity="N", stop_bits=1, timeout=1.0)


def test_read_and_parse_sin_conectar_lanza_error() -> None:
    """Verifica que UartDevice rechace leer datos si no se ha llamado
    a connect() antes, aventando RuntimeError."""
    parser = DummyParser(valido=True)
    device = UartDevice(config=CONFIG_DUMMY, parser=parser)
    with pytest.raises(RuntimeError):
        device.read_and_parse(b"1234")


def test_read_and_parse_conectado_devuelve_datos_parseados() -> None:
    """Verifica que, tras connect(), UartDevice pueda leer y regresar
    los datos ya parseados usando el parser inyectado."""
    parser = DummyParser(valido=True)
    device = UartDevice(config=CONFIG_DUMMY, parser=parser)
    device.connect()
    raw = b"abcd"
    resultado = device.read_and_parse(raw)
    assert resultado["protocolo"] == "dummy"
    assert resultado["contenido"] == raw


def test_disconnect_impide_seguir_leyendo() -> None:
    """Verifica que despues de disconnect(), UartDevice vuelva a
    rechazar la lectura, igual que si nunca se hubiera conectado."""
    parser = DummyParser(valido=True)
    device = UartDevice(config=CONFIG_DUMMY, parser=parser)
    device.connect()
    device.disconnect()
    with pytest.raises(RuntimeError):
        device.read_and_parse(b"5678")
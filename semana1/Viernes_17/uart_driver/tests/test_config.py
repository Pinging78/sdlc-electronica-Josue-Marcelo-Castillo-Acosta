import pytest
from dataclasses import FrozenInstanceError
from config import UartConfig

def test_baudrate_invalido() -> None:
    """Verifica que UartConfig rechace un baudrate fuera de la lista
    de valores permitidos, con el mensaje de error correspondiente."""
    with pytest.raises(ValueError) as excinfo:
        UartConfig(baudrate=12345, parity="N", stop_bits=1, timeout=1.0)
    assert "baudrate invalido" in str(excinfo.value)

def test_config_es_inmutable() -> None:
    """Verifica que UartConfig no se pueda modificar despues de creada,
    aventando FrozenInstanceError al intentar cambiar un campo."""
    config = UartConfig(baudrate=9600, parity="N", stop_bits=1, timeout=1.0)
    with pytest.raises(FrozenInstanceError):
        config.baudrate = 19200  # type: ignore[misc]

def test_config_valida_creada_correctamente() -> None:
    """Verifica que UartConfig se cree sin problema cuando todos los
    valores son validos, y que los campos queden con los valores dados."""
    config = UartConfig(baudrate=9600, parity="N", stop_bits=1, timeout=1.0)
    assert config.baudrate == 9600
    assert config.parity == "N"
    assert config.stop_bits == 1
    assert config.timeout == 1.0
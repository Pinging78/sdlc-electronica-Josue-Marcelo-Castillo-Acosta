import pytest
from parsers import ModbusParser, NMEAParser


def test_modbus_frame_valido_se_parsea_correctamente() -> None:
    """Verifica que un frame Modbus con CRC correcto sea aceptado por
    can_parse y que parse() extraiga bien todos los campos."""
    parser = ModbusParser()
    cuerpo = bytes([1, 3, 0x10, 0x20])
    crc = parser._calcular_crc(cuerpo)
    frame = cuerpo + crc
    assert parser.can_parse(frame) is True
    resultado = parser.parse(frame)
    assert resultado["protocolo"] == "modbus"
    assert resultado["direccion"] == 1
    assert resultado["funcion"] == 3
    assert resultado["datos"] == b"\x10\x20"


def test_modbus_frame_con_crc_invalido_es_rechazado() -> None:
    """Verifica que un frame Modbus con CRC corrupto sea rechazado por
    can_parse, y que parse() truene con ValueError si se intenta usar."""
    parser = ModbusParser()
    cuerpo = bytes([1, 3, 0x10, 0x20])
    frame = cuerpo + b"\x00\x00"
    assert parser.can_parse(frame) is False
    with pytest.raises(ValueError):
        parser.parse(frame)


def test_nmea_sentencia_valida_se_parsea_correctamente() -> None:
    """Verifica que una sentencia NMEA $GPGGA con checksum correcto,
    calculado dinamicamente, sea aceptada y parseada correctamente."""
    parser = NMEAParser()
    sentencia = "$GPGGA,123519,4807.038,N,01131.000,E*"
    cuerpo = sentencia[1:].split("*")[0]
    checksum = 0
    for char in cuerpo:
        checksum ^= ord(char)
    sentencia += f"{checksum:02X}"
    raw = sentencia.encode("ascii")
    assert parser.can_parse(raw) is True
    resultado = parser.parse(raw)
    assert resultado["protocolo"] == "nmea"
    assert resultado["tipo"] == "$GPGGA"
    assert resultado["hora"] == "123519"
    assert resultado["latitud"] == "4807.038"
from typing import Protocol
from dataclasses import dataclass


@dataclass(frozen=True)
class SensorReading:
    sensor_id: str
    value: float


# I - Interface Segregation

# Ejemplo malo: Cualquier dispositivo que la implemente esta
# obligado a tener los 4 metodos, aunque no todos los dispositivos calibren o se reseteen 
class DeviceGordoMalo(Protocol):
    def read(self) -> SensorReading: ...
    def write(self, reading: SensorReading) -> None: ...
    def calibrate(self) -> None: ...
    def reset(self) -> None: ...


# BUENO: se divide en varios protocolos cada uno con una sola
# responsabilidad. Cada clase implementa solo lo que en verdad necesita
class Readable(Protocol):
    def read(self) -> SensorReading: ...


class Writable(Protocol):
    def write(self, reading: SensorReading) -> None: ...


class Calibratable(Protocol):
    def calibrate(self) -> None: ...


class Resettable(Protocol):
    def reset(self) -> None: ...


# Un sensor de solo lectura -> solo implementa Readable
# No esta obligado a tener write/calibrate/reset como en la otra version
class TemperatureSensor:
    def __init__(self, sensor_id: str, value: float) -> None:
        self._sensor_id = sensor_id
        self._value = value

    def read(self) -> SensorReading:
        return SensorReading(self._sensor_id, self._value)


# Un actuador que si necesita calibrarse y resetearse, ademas de leer/escribir
# Para ello se implementan protocolos pequeños para un acceso más facil
class ServoActuador:
    def __init__(self, sensor_id: str) -> None:
        self._sensor_id = sensor_id
        self._value = 0.0
        self._calibrado = False

    def read(self) -> SensorReading:
        return SensorReading(self._sensor_id, self._value)

    def write(self, reading: SensorReading) -> None:
        self._value = reading.value

    def calibrate(self) -> None:
        self._calibrado = True

    def reset(self) -> None:
        self._value = 0.0
        self._calibrado = False


# D - Dependency Inversion

# Un Protocol no necesita herencia explicita: cualquier clase que tenga save() y get_latest() con
# esta firma "cuenta" como DataRepository automaticamente
class DataRepository(Protocol):
    def save(self, reading: SensorReading) -> None: ...
    def get_latest(self, sensor_id: str) -> SensorReading | None: ...


# ejemplo malo: DataProcessor crea su propia PostgreSQLRepository por dentro queda trabado y si se quiere probar en el test
# necesitaria una base de datos funcionando
class PostgreSQLRepositoryFalso:
   #Placeholder: en la vida real aqui habria una conexion real a PostgreSQL. 

    def save(self, reading: SensorReading) -> None:
        print(f"[SQL] INSERT INTO readings VALUES ({reading.sensor_id}, {reading.value})")

    def get_latest(self, sensor_id: str) -> SensorReading | None:
        print(f"[SQL] SELECT * FROM readings WHERE sensor_id={sensor_id}")
        return None  # simulado


class DataProcessorMaloD:
    def __init__(self) -> None:
        self._repo = PostgreSQLRepositoryFalso()  # dependencia concreta, quemada aqui

    def process(self, reading: SensorReading) -> None:
        self._repo.save(reading)


# BUENO: DataProcessor recibe la abstraccion (DataRepository) por
# constructor No importa si por dentro hay PostgreSQL, un archivo, o memoria RAM.
class DataProcessor:
    #Depende de la abstraccion

    def __init__(self, repository: DataRepository) -> None:
        self._repo = repository  # dependencias externas

    def process(self, reading: SensorReading) -> None:
        self._repo.save(reading)

    def latest_for(self, sensor_id: str) -> SensorReading | None:
        return self._repo.get_latest(sensor_id)


class InMemoryRepository:
    def __init__(self) -> None:
        self._data: dict[str, SensorReading] = {}

    def save(self, reading: SensorReading) -> None:
        self._data[reading.sensor_id] = reading

    def get_latest(self, sensor_id: str) -> SensorReading | None:
        return self._data.get(sensor_id)


# En produccion:  DataProcessor(PostgreSQLRepositoryFalso())
# En tests:       DataProcessor(InMemoryRepository())  


# TESTS

def test_isp_sensor_de_solo_lectura() -> None:
# Verifica ISP: TemperatureSensor cumple Readable
    sensor = TemperatureSensor("temp1", 22.5)

    lectura = sensor.read()
    assert lectura == SensorReading("temp1", 22.5)

    # confirma que de verdad no existen esos metodos en la clase
    assert not hasattr(sensor, "write")
    assert not hasattr(sensor, "calibrate")
    assert not hasattr(sensor, "reset")


def test_dip_data_processor_funciona_con_repositorio_en_memoria() -> None:
# Verifica DIP: DataProcessor no sabe que esta usando InMemoryRepository en vez de una base de datos real
    repo = InMemoryRepository()
    processor = DataProcessor(repository=repo)

    reading = SensorReading("hum1", 55.0)
    processor.process(reading)

    assert processor.latest_for("hum1") == reading
    assert processor.latest_for("no_existe") is None


if __name__ == "__main__":
    test_isp_sensor_de_solo_lectura()
    test_dip_data_processor_funciona_con_repositorio_en_memoria()
    print("Todos los tests pasaron correctamente.")
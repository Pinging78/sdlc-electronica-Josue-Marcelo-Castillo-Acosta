## refactor, mejora sin hacer error con el test
class Sensor:
    def __init__(self, sensor_id, tipo, ubicacion):
        self.sensor_id = sensor_id
        self.tipo = tipo
        self.ubicacion = ubicacion

class SensorRegistry:
    def __init__(self):
        self._sensores = {}

    def registrar(self, sensor_id, tipo, ubicacion):
        self._sensores[sensor_id] = Sensor(sensor_id, tipo, ubicacion)

    def existe(self, sensor_id):
        return sensor_id in self._sensores
## se define la clase para que ya funcione
class SensorRegistry:
    def __init__(self):
        self._sensores = {}

    def registrar(self, sensor_id, tipo, ubicacion):
        self._sensores[sensor_id] = {"tipo": tipo, "ubicacion": ubicacion}

    def existe(self, sensor_id):
        return sensor_id in self._sensores
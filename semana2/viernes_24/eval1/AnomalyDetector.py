
class AnomalyDetector:
    def __init__(self, temp_max, humedad_max):
        self.temp_max = temp_max
        self.humedad_max = humedad_max

    def evaluar(self, temp_max, humedad_max):
        return temperatura > self.temp_max or humedad > self.humedad_max
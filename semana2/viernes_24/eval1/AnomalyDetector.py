
class AnomalyThreshold:
    def __init__(self, temp_max, humedad_max): #valores dados en el test
        self.temp_max = temp_max #umbral
        self.humedad_max = humedad_max

class AnomalyDetector:
    def __init__(self, threshold: AnomalyThreshold):
        self.threshold = threshold

    def evaluar(self, temp_max, humedad_max):
        return self._temperatura_excedida(temperatura) or self._humedad_excedida(humedad)
    #compara temperatura que se mando desde el test con el umbral y verifica si es true o false
    #or junta las comparaciones como una compuerta or y si una es true el resultado va a ser true

    def _temperatura_excedida(self, temperatura):
        return temperatura > self.threshold.temp_max 
#busca en el threshold el valor

    def _humedad_excedida(self, humedad):
        return humedad > self.threshold.humedad_max
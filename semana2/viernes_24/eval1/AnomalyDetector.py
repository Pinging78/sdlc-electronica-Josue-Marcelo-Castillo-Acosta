
class AnomalyDetector:
    def __init__(self, temp_max, humedad_max): #valores dados en el test
        self.temp_max = temp_max #umbral
        self.humedad_max = humedad_max

    def evaluar(self, temp_max, humedad_max):
        return temperatura > self.temp_max or humedad > self.humedad_max
    #compara temperatura que se mando desde el test con el umbral y verifica si es true o false
    #or junta las comparaciones como una compuerta or y si una es true el resultado va a ser true
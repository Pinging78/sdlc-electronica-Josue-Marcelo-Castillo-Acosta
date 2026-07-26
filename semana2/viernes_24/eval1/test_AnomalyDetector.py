from AnomalyDetector import AnomalyDetector, AnomalyThreshold


def test_detecta_temperatura_alta(): #se define la funcion
    threshold = AnomalyThreshold(temp_max=35, humedad_max=80) #umbral maximo
    detector = AnomalyDetector(threshold) #detecta el valor del umbral y lo asigna 
    resultado = detector.evaluar(temperatura=40, humedad=50) #valores medidos ejemplo
    assert resultado is True # verifica si es cierto
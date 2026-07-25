from AnomalyDetector import AnomalyDetector

#RED
def test_detecta_temperatura_alta(): #se define la funcion
    detector = AnomalyDetector(temp_max=35, humedad_max=80) #umbral maximo
    resultado = detector.evaluar(temperatura=40, humedad=50) #valores medidos ejemplo
    assert resultado is True # verifica si es cierto
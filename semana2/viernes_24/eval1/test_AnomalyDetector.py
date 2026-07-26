from AnomalyDetector import AnomalyDetector, AnomalyThreshold


def test_detecta_temperatura_alta(): #se define la funcion
    threshold = AnomalyThreshold(temp_max=35, humedad_max=80) #umbral maximo
    detector = AnomalyDetector(threshold) #detecta el valor del umbral y lo asigna 
    resultado = detector.evaluar(temperatura=40, humedad=50) #valores medidos ejemplo
    assert resultado is True # verifica si es cierto

def test_no_detecta_anomalia_dentro_del_rango():
    threshold = AnomalyThreshold(temp_max=35, humedad_max=80)
    detector = AnomalyDetector(threshold)
    resultado = detector.evaluar(temperatura=25, humedad=50)
    assert resultado is False


def test_detecta_humedad_alta():
    threshold = AnomalyThreshold(temp_max=35, humedad_max=80)
    detector = AnomalyDetector(threshold)
    resultado = detector.evaluar(temperatura=20, humedad=90)
    assert resultado is True


def test_umbral_distinto_por_sensor():
    threshold_zona_fria = AnomalyThreshold(temp_max=5, humedad_max=60)
    detector = AnomalyDetector(threshold_zona_fria)
    resultado = detector.evaluar(temperatura=10, humedad=40)
    assert resultado is True  # 10°C ya rebasa el umbral de zona fría (5°C)


def test_caso_limite_justo_en_el_umbral():
    threshold = AnomalyThreshold(temp_max=35, humedad_max=80)
    detector = AnomalyDetector(threshold)
    resultado = detector.evaluar(temperatura=35, humedad=80)
    assert resultado is False  # exactamente en el límite, no lo supera
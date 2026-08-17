from app.services.anomaly_detector import AnomalyDetector

def test_temperatura_dentro_de_rango_no_es_anomalia():
    detector = AnomalyDetector()
    assert detector.es_anomalia("temperatura", 30) is False
    #si el valor no sobrepasa el umbral no es una anomalia


def test_temperatura_supera_umbral_es_anomalia():
    detector = AnomalyDetector()
    assert detector.es_anomalia("temperatura", 36) is True

def test_humedad_dentro_de_rango_no_es_anomalia():
    detector = AnomalyDetector()
    assert detector.es_anomalia("humedad", 70) is False

def test_humedad_supera_umbral_es_anomalia():
    detector = AnomalyDetector()
    assert detector.es_anomalia("humedad", 85) is True

def test_tipo_sensor_desconocido_no_es_anomalia():
    detector = AnomalyDetector()
    assert detector.es_anomalia("presion", 999) is False
    #tipo de sensor desconocido: no se evalua como anomalia, se ignora en silencio
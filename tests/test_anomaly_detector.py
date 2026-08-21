from app.services.anomaly_detector import AnomalyDetector, Nivel


def test_temperatura_dentro_de_rango_es_ok():
    detector = AnomalyDetector()
    assert detector.evaluar("temperatura", 30) == Nivel.OK


def test_temperatura_supera_warning_es_warning():
    detector = AnomalyDetector()
    assert detector.evaluar("temperatura", 36) == Nivel.WARNING


def test_temperatura_supera_critical_es_critical():
    detector = AnomalyDetector()
    assert detector.evaluar("temperatura", 46) == Nivel.CRITICAL


def test_humedad_dentro_de_rango_es_ok():
    detector = AnomalyDetector()
    assert detector.evaluar("humedad", 70) == Nivel.OK


def test_humedad_supera_warning_es_warning():
    detector = AnomalyDetector()
    assert detector.evaluar("humedad", 85) == Nivel.WARNING


def test_humedad_supera_critical_es_critical():
    detector = AnomalyDetector()
    assert detector.evaluar("humedad", 95) == Nivel.CRITICAL


def test_tipo_sensor_desconocido_es_ok():
    detector = AnomalyDetector()
    assert detector.evaluar("presion", 999) == Nivel.OK
    #tipo de sensor desconocido: no se evalua, se ignora en silencio


def test_es_anomalia_mantiene_compatibilidad_bool():
    detector = AnomalyDetector()
    assert detector.es_anomalia("temperatura", 30) is False
    assert detector.es_anomalia("temperatura", 36) is True
    assert detector.es_anomalia("temperatura", 46) is True
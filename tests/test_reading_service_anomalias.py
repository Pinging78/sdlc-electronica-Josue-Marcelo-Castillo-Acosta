# tests/test_reading_service_anomalias.py

from unittest.mock import MagicMock

from app.services.alert_manager import AlertManager
from app.services.reading_service import ReadingService


def test_registrar_reading_normal_no_genera_alerta():
    repo_falso = MagicMock() 
    #crea un objeto que simula cómo se comportaría otro objeto real, sin necesitarlo
    #Aquí lo usamos para simular el ReadingRepository sin necesitar una base de datos real conectada
    repo_falso.create.return_value = {"id": 1, "sensor_id": 1, "value": 25, "unit": "°C"}
    alert_manager = AlertManager()

    service = ReadingService(repo_falso, alert_manager)
    service.register_reading(1, 25, "°C", "temperatura")
    #se comprueba que no hay anomalias, esto para tener un ejemplo y comprobacion de funcionamiento
    assert len(alert_manager.alertas) == 0


def test_registrar_reading_anomalo_genera_alerta():
    repo_falso = MagicMock()
    repo_falso.create.return_value = {"id": 1, "sensor_id": 1, "value": 40, "unit": "°C"}
    alert_manager = AlertManager()

    service = ReadingService(repo_falso, alert_manager)
    service.register_reading(1, 40, "°C", "temperatura")

    assert len(alert_manager.alertas) == 1
    assert "40" in alert_manager.alertas[0]
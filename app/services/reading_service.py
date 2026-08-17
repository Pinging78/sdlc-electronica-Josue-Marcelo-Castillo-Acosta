from datetime import datetime

from app.repositories.reading_repository import ReadingRepository
from app.services.alert_manager import AlertManager
from app.services.anomaly_detector import UMBRALES, AnomalyDetector


#esta la logica de negocio como reglas, validaciones o calculos
class ReadingService:
    def __init__(self, repository: ReadingRepository, alert_manager: AlertManager | None = None):
        self.repository = repository  #guarda el repositorio que le pasan, para usarlo despues
        self.alert_manager = alert_manager or AlertManager()
        self.detector = AnomalyDetector()

    def list_readings(
        self,
        skip: int = 0,
        limit: int = 10,
        sensor_id: int | None = None,
        fecha_inicio: datetime | None = None,
        fecha_fin: datetime | None = None,
    ):
        return self.repository.get_all(
            skip=skip, limit=limit, sensor_id=sensor_id,
            fecha_inicio=fecha_inicio, fecha_fin=fecha_fin
        )  #obtiene la lista de los sensores

    def get_reading(self, reading_id: int):
        return self.repository.get_by_id(reading_id)

    def update_reading(self, reading_id: int, value: float | None = None, unit: str | None = None):
        return self.repository.update(reading_id, value, unit)

    def register_reading(self, sensor_id: int, value: float, unit: str, sensor_type: str):
        reading = self.repository.create(sensor_id, value, unit)  # delega la creacion al repositorio
        if self.detector.es_anomalia(sensor_type, value):
            umbral = UMBRALES.get(sensor_type)
            self.alert_manager.notificar(
                f"ALERTA: sensor {sensor_id} ({sensor_type}) reporto {value}{unit}, supera umbral de {umbral}"
            )
        return reading

    def remove_reading(self, reading_id: int):
        return self.repository.delete(reading_id)
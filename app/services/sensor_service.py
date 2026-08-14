from app.repositories.sensor_repository import SensorRepository


#esta la logica de negocio como reglas, validaciones o calculos
class SensorService:
    def __init__(self, repository: SensorRepository):
        self.repository = repository  #guarda el repositorio que le pasan, para usarlo despues

    def list_sensors(self, skip: int = 0, limit: int = 10):
        return self.repository.get_all(skip=skip, limit=limit)  #obtiene la lista de los sensores

    def get_sensor(self, sensor_id: int):
        sensor = self.repository.get_by_id(sensor_id)
        if sensor is None:
            raise ValueError(f"Sensor with ID {sensor_id} not found.")
        return sensor

    def register_sensor(self, name: str, type: str):
        return self.repository.create(name, type)

    def remove_sensor(self, sensor_id: int):
        sensor = self.repository.get_by_id(sensor_id)
        if sensor is None:
            raise ValueError(f"Sensor with ID {sensor_id} not found.")
        return self.repository.delete(sensor_id)

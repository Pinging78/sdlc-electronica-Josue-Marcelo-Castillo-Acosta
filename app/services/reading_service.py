from app.repositories.reading_repository import ReadingRepository

#esta la logica de negocio como reglas, validaciones o calculos
class ReadingService:
    def __init__(self, repository: ReadingRepository):
        self.repository = repository  #guarda el repositorio que le pasan, para usarlo despues

    def list_readings(self):
        return self.repository.get_all()  #solo delega al repositorio

    def register_reading(self, sensor_id: int, value: float, unit: str):
        return self.repository.create(sensor_id, value, unit)  # delega la creacion al repositorio
        #podriamos tener validaciones como por ejemplo: rechazar value negativo. pero de momento asi esta bien
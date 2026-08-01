from sqlalchemy.orm import Session
from app.models.reading import Reading
from datetime import datetime

#es la unica clase que habla con la base de datos
class ReadingRepository:
    def __init__(self, db: Session):
        self.db = db  #guarda la sesion de base de datos que le pasan (viene de get_db)

    def get_all(
        self,
        skip: int = 0,
        limit: int = 10,
        sensor_id: int | None = None,
        fecha_inicio: datetime | None = None,
        fecha_fin: datetime | None = None,
    ):
        # trae registros de la tabla readings, con paginacion (skip/limit) y filtro opcional por sensor_id
        query = self.db.query(Reading)
        if sensor_id is not None:
            query = query.filter(Reading.sensor_id == sensor_id)
        if fecha_inicio is not None:
            query = query.filter(Reading.timestamp >= fecha_inicio)
        if fecha_fin is not None:
            query = query.filter(Reading.timestamp <= fecha_fin)
        return query.offset(skip).limit(limit).all()

    def create(self, sensor_id: int, value: float, unit: str):
        reading = Reading(sensor_id=sensor_id, value=value, unit=unit)  # crea el objeto (no guardado aun)
        self.db.add(reading)      #lo marca para insertar
        self.db.commit()          #confirma la transaccion, ya queda guardado en la base
        self.db.refresh(reading)  #actualiza el objeto con datos generados por la BD (como el id)
        return reading            #regresa el registro ya guardado, con su id
    
    def delete(self, sensor_id: int):
        reading = self.db.query(Reading).filter(Reading.id == sensor_id).first()
        if reading:
            self.db.delete(reading)
            self.db.commit()
        return reading
from sqlalchemy.orm import Session
from app.models.sensor import Sensor

#es la unica clase que habla con la base de datos
class SensorRepository:
    def __init__(self, db: Session):
        self.db = db  #guarda la sesion de base de datos que le pasan (viene de get_db)

    def get_all(self, skip: int = 0, limit: int = 10):
        # trae registros de la tabla sensors, con paginacion (skip/limit)
        return self.db.query(Sensor).offset(skip).limit(limit).all()

    def get_by_id(self, sensor_id: int):
        return self.db.query(Sensor).filter(Sensor.id == sensor_id).first()

    def create(self, name: str, type: str):
        sensor = Sensor(name=name, type=type)  # crea el objeto (no guardado aun)
        self.db.add(sensor)      #lo marca para insertar
        self.db.commit()          #confirma la transaccion, ya queda guardado en la base
        self.db.refresh(sensor)  #actualiza el objeto con datos generados por la BD (como el id)
        return sensor            #regresa el registro ya guardado, con su id

    def delete(self, sensor_id: int):
        sensor = self.get_by_id(sensor_id)
        if sensor:
            self.db.delete(sensor)
            self.db.commit()
        return sensor
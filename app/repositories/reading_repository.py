from sqlalchemy.orm import Session
from app.models.reading import Reading

#es la unica clase que habla con la base de datos
class ReadingRepository:
    def __init__(self, db: Session):
        self.db = db  #guarda la sesion de base de datos que le pasan (viene de get_db)

    def get_all(self):
        return self.db.query(Reading).all()  #trae todos los registros de la tabla readings

    def create(self, sensor_id: int, value: float, unit: str):
        reading = Reading(sensor_id=sensor_id, value=value, unit=unit)  # crea el objeto (no guardado aun)
        self.db.add(reading)      #lo marca para insertar
        self.db.commit()          #confirma la transaccion, ya queda guardado en la base
        self.db.refresh(reading)  #actualiza el objeto con datos generados por la BD (como el id)
        return reading            #regresa el registro ya guardado, con su id
#creacion de la api
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.db import Base, engine, get_db
from app.models.reading import Reading
from app.repositories.reading_repository import ReadingRepository
from app.repositories.sensor_repository import SensorRepository
from app.services.reading_service import ReadingService
from app.services.sensor_service import SensorService
from app.schemas.reading import ReadingCreate

Base.metadata.create_all(bind=engine) #crea una tabla con este engine de esta base de datos

app = FastAPI() #app es la instancia fastapi

def get_reading_service(db: Session = Depends(get_db)):
    return ReadingService(ReadingRepository(db))

def get_sensor_service(db: Session = Depends(get_db)):
    return SensorService(SensorRepository(db))

#/health ruta o url del endpoint
@app.get("/health") #cuando hagan la peticion get a esta ruta
def health():
    return {"status": "active"} #ejecuta esto

@app.get("/readings")
def readings(
    skip: int = 0,
    limit: int = 10,
    sensor_id: int | None = None,
    service: ReadingService = Depends(get_reading_service)
):
    return service.list_readings(skip=skip, limit=limit, sensor_id=sensor_id)

@app.post("/readings")
def create_reading(data: ReadingCreate, service: ReadingService = Depends(get_reading_service)):
    return service.register_reading(data.sensor_id, data.value, data.unit)

@app.delete("/readings/{reading_id}")
def delete_reading(reading_id: int, service: ReadingService = Depends(get_reading_service)):
    return service.remove_reading(reading_id)

@app.get("/sensors")
def sensors(
    skip: int = 0,
    limit: int = 10,
    service: SensorService = Depends(get_sensor_service)
):
    return service.list_sensors(skip=skip, limit=limit)

@app.post("/sensors")
def create_sensor(name: str, type: str, service: SensorService = Depends(get_sensor_service)):
    return service.register_sensor(name, type)

@app.delete("/sensors/{sensor_id}")
def delete_sensor(sensor_id: int, service: SensorService = Depends(get_sensor_service)):
    return service.remove_sensor(sensor_id)
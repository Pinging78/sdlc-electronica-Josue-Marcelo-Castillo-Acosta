#creacion de la api
from datetime import datetime

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app.db import Base, engine, get_db
from app.repositories.reading_repository import ReadingRepository
from app.repositories.sensor_repository import SensorRepository
from app.schemas.reading import ReadingCreate, ReadingUpdate
from app.services.reading_service import ReadingService
from app.services.sensor_service import SensorService

Base.metadata.create_all(bind=engine) #crea una tabla con este engine de esta base de datos

app = FastAPI() #app es la instancia fastapi

def get_reading_service(db: Session = Depends(get_db)):
    return ReadingService(ReadingRepository(db))

def get_sensor_service(db: Session = Depends(get_db)):
    return SensorService(SensorRepository(db))

#/health ruta o url del endpoint
@app.get("/")
def root():
    return {
        "message": "Welcome to the Sensor API!",
        "docs_url": "/docs"
    }

@app.get("/health") #cuando hagan la peticion get a esta ruta
def health():
    return {"status": "active"} #ejecuta esto

@app.get("/readings")
def readings(
    skip: int = 0,
    limit: int = 10,
    sensor_id: int | None = None,
    fecha_inicio: datetime | None = None,
    fecha_fin: datetime | None = None,
    service: ReadingService = Depends(get_reading_service)
):
    return service.list_readings(
        skip=skip, limit=limit, sensor_id=sensor_id,
        fecha_inicio=fecha_inicio, fecha_fin=fecha_fin
    )
@app.post("/readings")
def create_reading(data: ReadingCreate, service: ReadingService = Depends(get_reading_service)):
    return service.register_reading(data.sensor_id, data.value, data.unit, data.sensor_type)

@app.get("/readings/{reading_id}")
def get_reading(reading_id: int, service: ReadingService = Depends(get_reading_service)):
    return service.get_reading(reading_id)

@app.patch("/readings/{reading_id}")
def update_reading(reading_id: int, data: ReadingUpdate, service: ReadingService = Depends(get_reading_service)):
    return service.update_reading(reading_id, data.value, data.unit)

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
    try:
        return service.remove_sensor(sensor_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

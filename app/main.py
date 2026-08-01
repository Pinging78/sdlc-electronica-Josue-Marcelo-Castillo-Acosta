#creacion de la api
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.db import Base, engine, get_db
from app.models.reading import Reading
from app.repositories.reading_repository import ReadingRepository
from app.services.reading_service import ReadingService

#ahora solo le pide al reading_service las lecturas o que las registre

Base.metadata.create_all(bind=engine) #crea una tabla con este engine de esta base de datos
  
app = FastAPI() #app es la instancia fastapi

def get_reading_service(db: Session = Depends(get_db)):
    return ReadingService(ReadingRepository(db))

#/health ruta o url del endpoint
@app.get("/health") #cuando hagan la peticion get a esta ruta
def health():
    return {"status": "active"} #ejecuta esto

@app.get("/readings")
def readings(
    skip: int = 0,
    limit: int = 10, #configuraciones predeterminadas
    sensor_id: int | None = None,
    service: ReadingService = Depends(get_reading_service) 
):
    return service.list_readings(skip=skip, limit=limit, sensor_id=sensor_id) #regresa la lista

@app.post("/readings")
def create_reading(sensor_id: int, value: float, unit: str, service: ReadingService = Depends(get_reading_service)):
    return service.register_reading(sensor_id, value, unit)
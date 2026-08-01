#creacion de la api
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.db import Base, engine, get_db
from app.models.reading import Reading

Base.metadata.create_all(bind=engine) #crea una tabla con este engine de esta base de datos
  
app = FastAPI() #app es la instancia fastapi

#/health ruta o url del endpoint
@app.get("/health") #cuando hagan la peticion get a esta ruta
def health():
    return {"status": "active"} #ejecuta esto

@app.get("/readings")
def readings(db: Session = Depends(get_db)):
    return db.query(Reading).all()

@app.post("/readings")
def create_reading(sensor_id: int, value: float, unit: str, db: Session = Depends(get_db)):
    reading = Reading(sensor_id=sensor_id, value=value, unit=unit)
    db.add(reading)
    db.commit()
    db.refresh(reading)
    return reading
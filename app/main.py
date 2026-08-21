#creacion de la api
import os
import subprocess
from datetime import datetime

from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.db import get_db
from app.logging_config import logger
from app.repositories.reading_repository import ReadingRepository
from app.repositories.sensor_repository import SensorRepository
from app.schemas.reading import ReadingCreate, ReadingUpdate
from app.services.reading_service import ReadingService
from app.services.sensor_service import SensorService


def run_migrations() -> None:
    # aplica migraciones pendientes de Alembic al arrancar, en vez de create_all()
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    result = subprocess.run(
        ["alembic", "upgrade", "head"],
        cwd=project_root,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        logger.error(f"Fallo alembic upgrade head: {result.stderr}")
        raise RuntimeError(f"No se pudieron aplicar migraciones: {result.stderr}")
    logger.info("Migraciones de Alembic aplicadas correctamente")


run_migrations()

app = FastAPI() #app es la instancia fastapi


@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    # atrapa cualquier error no manejado para no exponer tracebacks internos al cliente
    logger.error(f"Error no manejado en {request.method} {request.url.path}: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Ocurrio un error interno, intenta de nuevo mas tarde."},
    )

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
def health(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        db_status = "ok"
    except Exception as e:
        logger.error(f"Healthcheck: fallo conexion a BD: {e}")
        db_status = "error"
    return {"status": "active", "database": db_status}

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
    logger.info(f"Registrando lectura: sensor_id={data.sensor_id} tipo={data.sensor_type} value={data.value}")
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

@app.get("/sensors/{sensor_id}")
def get_sensor(sensor_id: int, service: SensorService = Depends(get_sensor_service)):
    try:
        return service.get_sensor(sensor_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.post("/sensors")
def create_sensor(name: str, type: str, service: SensorService = Depends(get_sensor_service)):
    return service.register_sensor(name, type)

@app.delete("/sensors/{sensor_id}")
def delete_sensor(sensor_id: int, service: SensorService = Depends(get_sensor_service)):
    try:
        return service.remove_sensor(sensor_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
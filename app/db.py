import os

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./sensorhub.db")

connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(DATABASE_URL, connect_args=connect_args)
#engine es como una fabrica que crea nuevas conexiones de datos y mantiene las conexiones
#dentro de un grupo de conexiones para su reutilizacion rapida

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #configuraciones de la sesion
#el bind=engine indica que cada sesion que se cree con esta fabrica se usa para hablar con el engine o base de datos
#en otras palabras es la conexion entre el sensorhub.db y el bind=engine
class Base(DeclarativeBase): #se declara la base
    pass

def get_db(): #para obtener la configuracion del db
    db = SessionLocal()
    try:
        yield db #entrega la sesion db a quien la use
    finally:
        db.close() #cierra la base de datos
        
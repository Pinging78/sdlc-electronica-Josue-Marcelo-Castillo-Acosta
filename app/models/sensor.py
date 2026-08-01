from sqlalchemy.orm import Mapped, mapped_column
from app.db import Base

class Sensor(Base):
    __tablename__ = "sensors"
#datos del sensor
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    type: Mapped[str]  # "temperatura" o "humedad"
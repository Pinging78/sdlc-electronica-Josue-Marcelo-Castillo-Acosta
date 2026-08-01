from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


#se crea la clase para asignar los valores desde la api
class Reading(Base):
    __tablename__ = "readings" 

    id: Mapped[int] = mapped_column(primary_key=True)
    sensor_id: Mapped[int]
    value: Mapped[float]
    unit: Mapped[str]
    timestamp: Mapped[datetime] = mapped_column(default=datetime.utcnow)
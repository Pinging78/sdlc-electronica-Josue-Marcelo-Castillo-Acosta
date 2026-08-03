from pydantic import BaseModel, field_validator

RANGOS = {
    "temperatura": {"unidad": "°C", "min": -40, "max": 80}, #rango fisico del fabricante
    "humedad": {"unidad": "%", "min": 0, "max": 100},
}

class ReadingCreate(BaseModel):
    sensor_id: int 
    sensor_type: str  # "temperatura" o "humedad"
    value: float
    unit: str

    @field_validator("unit")
    @classmethod
    def unidad_valida(cls, v, info): #verifica que la unidad sea correcta
        sensor_type = info.data.get("sensor_type")
        esperado = RANGOS.get(sensor_type, {}).get("unidad")
        if esperado and v != esperado:
            raise ValueError(f"unidad invalida para {sensor_type}, se esperaba {esperado}")
        return v

    @field_validator("value")
    @classmethod
    def rango_fisico_valido(cls, v, info): #verifica que no sobrepase el rango fisico
        sensor_type = info.data.get("sensor_type")
        rango = RANGOS.get(sensor_type)
        if rango and not (rango["min"] <= v <= rango["max"]):
            raise ValueError(f"value fuera de rango fisico para {sensor_type}")
        return v

class ReadingUpdate(BaseModel):
    value: float | None = None
    unit: str | None = None
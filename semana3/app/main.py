from fastapi import FastAPI

app = FastAPI() #app es la instancia fastapi

#/health ruta o url del endpoint
@app.get("/health") #cuando hagan la peticion get a esta ruta
def health():
    return {"status": "active"} #ejecuta esto

@app.get("/readings")
def readings():
    return [
    {"sensor_id": 1, "value": 25, "unit": "°C"},
    {"sensor_id": 2, "value": 68.3, "unit": "%"},
    ]
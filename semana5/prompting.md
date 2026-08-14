# Prompting efectivo

Un buen prompt tiene 4 partes: contexto + tarea + restricciones + formato

## 1. Agregar un endpoint

**Prompt pobre:**
> Agrega un endpoint para borrar sensores

**Prompt bueno:**
> Contexto: Tengo una API FastAPI en app/main.py con arquitectura de 4 capas (routers/services/repositories/models)El servicio SensorService ya tiene remove_sensor(sensor_id) implementado en app/services/sensor_service.py

> Tarea: Agrega el endpoint DELETE /sensors/{sensor_id} en app/main.py que llame a ese metodo

> Restricciones: Sigue el mismo patron que uso en los demas endpoints DELETE (usa Depends para inyectar el servicio, status_code=204, no regreses cuerpo)

> Formato: Solo el codigo del endpoint nuevo, sin reescribir el archivo completo

## 2. Explicar un error

**Prompt pobre:**
> por que sale este error

**Prompt bueno:**
> Contexto: Corro `docker compose up` y mi API (FastAPI + SQLAlchemy) no conecta a PostgreSQL. Aqui esta el traceback completo: [pegar error]

> Tarea: Explica la causa mas probable del error

> Restricciones: No asumas que uso SQLite, mi docker-compose.yml usa PostgreSQL con host "db". Dime que archivo revisar primero

> Formato: Explicacion breve (3-4 lineas) + un comando o cambio concreto a probar

## 3. Refactorizar código

**Prompt pobre:**
> mejora este codigo

**Prompt bueno:**
> Contexto: Este es mi ReadingRepository (SQLAlchemy 2.x), usado por ReadingService en una API de sensores IoT

> Tarea: Revisa si get_all() tiene algun problema de rendimiento o diseño

> Restricciones: No cambies la firma del metodo (otros archivos ya lo llaman asi). No agregues librerias nuevas

> Formato: Lista corta de hallazgos, cada uno con el numero de linea y una propuesta de una sola linea de codigo si aplica
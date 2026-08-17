# Registro de Asistencia y Trazabilidad por IA (AI Log)

## 1. Configuración del Entorno
* **Herramienta:** Aider CLI v0.86.2
* **Entorno de ejecución:** WSL2 Ubuntu (`/venv/bin/aider`)
* **Modelo principal utilizado:** `github_copilot/gpt-4o`
* **Modelos alternativos probados:** `claude-sonnet-4-5` (Anthropic), `groq/llama-3.3-70b-versatile`
* **Proyecto:** SensorHub IoT API (FastAPI en 4 capas: routers → services → repositories → models)

---

## 2. Historial de Sesiones, Prompts y Commits

### Sesión 1: Configuración inicial y Endpoint raíz
* **Fecha:** 2026-08-14 04:52:24
* **Modelo:** `github_copilot/gpt-4o`
* **Archivo:** `app/main.py`
* **Prompt:**
  > *Add a GET / endpoint in app/main.py that returns a simple welcome message with the API name and a link to /docs*
* **Commit generado por Aider:**
  * `20d5d44` — `feat: add root endpoint with welcome message and docs link`

---

### Sesión 2: Code Review y Manejo de Excepciones
* **Fecha:** 2026-08-14 05:23:51
* **Modelo:** `github_copilot/gpt-4o`
* **Archivos:** `app/services/sensor_service.py`, `app/main.py`
* **Actividad:**
  1. **Revisión estática:** Análisis de 8 puntos críticos en la capa de servicios (validación de `skip`/`limit`, docstrings, manejo de sensores nulos, tipado).
  2. **Refactorización de errores:** Actualización de `get_sensor` y `remove_sensor` para lanzar `ValueError` en caso de no existir el ID, y captura en `app/main.py` retornando HTTP 404.
* **Commits generados por Aider:**
  * `fa9b29f` — `fix: raise ValueError for missing sensors and handle as 404 HTTPException`
  * `aa5a6bc` — `feat: add GET /sensors/{sensor_id} endpoint with error handling`

---

### Sesión 3: Documentación Arquitectónica (ADR)
* **Fecha:** 2026-08-14 07:08:56 – 07:24:47
* **Archivo generado:** `docs/adr/0001-arquitectura-en-capas.md`
* **Prompt:**
  > *Create a file docs/adr/0001-arquitectura-en-capas.md documenting the architecture decision to use a layered monolith (routers -> services -> repositories -> models) instead of microservices for this project...*
* **Contenido documentado:** Decisión de monolito en capas vs microservicios fundamentada en Martin Fowler (*Microservices* y *MonolithFirst*), citando hallazgos del peer review sobre aislamiento de capas.

---

## 3. Registro de Fallbacks y Manejo de Proveedores (Consigna)

1. **Intento con Anthropic Claude (`--model sonnet`):**
   * **Comando:** `aider --model sonnet`
   * **Resultado:** Fallo de autenticación (`litellm.AuthenticationError: Missing Anthropic API Key`).
   * **Acción tomada:** Documentación del intento y cambio de proveedor.

2. **Intento con Groq Llama 3.3:**
   * **Comando:** `aider --model groq/llama-3.3-70b-versatile --api-key groq=***`
   * **Resultado:** Conexión exitosa y generación del borrador inicial del ADR.

3. **Modelo de Producción Estable:**
   * Se consolidó el flujo de trabajo mediante el backend oficial `github_copilot/gpt-4o`.
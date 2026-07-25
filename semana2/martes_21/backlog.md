# Product Backlog

## US1 - Lectura periodica de los sensores
Para este sistema se requiere leer 10 sensores de temperatura y humedad cada 30 segundos para tenerlos datos actualizados

**Story points:** 3
**Priorización MoSCoW:** Must Have

```gherkin
Scenario: lectura de los sensores activos
Given: los sensores actualizan su lectura
When: pasan 30 segundos
Then: el sistema registra una nueva lectura de todos los sensores
```
    **Auditoria IA: Correcto como base, pero falta robustez en manejo de errores.

    Claridad: Bien definido, se entiende que son 10 sensores y cada 30 segundos.
    
    Riesgos:
    ¿Qué pasa si un sensor tarda más en responder?
    
    ¿Se requiere tolerancia a fallos o reintentos?
    
    Mejora: Especificar formato de almacenamiento de las lecturas (JSON, DB, etc.) y qué ocurre si un sensor falla.


## US2 - Deteccion de anomalias
Como desarrollador quiero detectar anomalias en las lecturas o falsos positivos de una alerta por lo que se hace la deteccion de estos casos y evitamos problemas a futuro

**Story points:** 5
**Priorización MoSCoW:** Must Have

```gherkin
Scenario: deteccion de anomalias
Given: al recibir una lectura nueva
When: la temperatura es mayor a a 35°C o la humedad es mayor al 80%
Then: existe una anomalia
```
    **Auditoria IA: Bien planteado, pero limitado si el sistema escala.
    Claridad: Condiciones explícitas (temp > 35°C, humedad > 80%).
    
    Riesgos:
    Umbrales fijos pueden ser insuficientes; ¿se ajustan dinámicamente?
    
    No se contempla ruido o variaciones pequeñas.

    Mejora: Definir si se usarán algoritmos estadísticos o reglas simples.



## US3 - Generacion de alertas
Los encargados de la bodega deben de recibir una alerta cuando una anomalia se presente, esto para que puedan actuar en tiempo y forma para no dañar su mercancia

**Story points:** 3
**Priorización MoSCoW:** Must Have

```gherkin
Scenario: anomalia encontrada
Given: se detecto la anomalia
When: el sistema la procesa y verifica que no solo sea un falso positivo
Then: envia una alerta en menos de 5 segundos por medio de correo
```
    **Auditoria IA: Correcto, pero incompleto en resiliencia.

    Claridad: Envío de alerta en menos de 5 segundos vía correo.

    Riesgos:
    ¿Qué pasa si el correo falla?

    ¿Se requiere redundancia (SMS, app, dashboard)?

    Mejora: Definir canales alternativos y asegurar SLA de envío.


## US4 - Identificar el sensor de origen
Una vez que la alerta se detecte se debe de localizar para saber en donde es el problema

**Story points:** 2
**Priorización MoSCoW:** Should Have

```gherkin
Scenario: el rango maximo fue rebasado
Given: se genera una alerta
When: se registra la lectura
Then: incluye el ID del sensor y en donde se encuentra
```
    **Auditoria IA: Bien definido, pero requiere integración con inventario de sensores.

    Claridad: Se incluye ID y ubicación.

    Riesgos:
    ¿Dónde se guarda la ubicación? ¿Base de datos de sensores?

    ¿Qué pasa si el sensor fue movido físicamente?

    Mejora: Añadir validación periódica de ubicación.


## US5 - Deteccion de sensor desconectado o descompuesto
Por prevencion se debe de manejar el caso de la perdida de algun sensor, esto para evitar daños por silencio o la ultima lectura guardada que se repite constantemente

**Story points:** 2
**Priorización MoSCoW:** Could Have

```gherkin
Scenario: un sensor deja de responder
Given: un sensor dejo de enviar datos en los 30 segundos que se asigno
When: pasa el tiempo limite
Then: se marca ese sensor y crea una alerta para revisarlo
```
    **Auditoria IA: Correcto, pero necesita mayor precisión en diagnóstico.

    Claridad: Se marca sensor y se genera alerta.

    Riesgos:
    Puede haber falsos positivos si hay retraso en red.

    ¿Se diferencia entre desconectado y descompuesto?

    Mejora: Añadir lógica de reintentos antes de marcarlo como fallido.


## US6 - Historial de lecturas y anomalias
Como desarrollador quisiera un historial de lecturas y anomalias para tener un mejor control y la capacidad de analizar los datos cuando se requiera

**Story points:** 5
**Priorización MoSCoW:** Could Have

```gherkin
Scenario: los sensores estan activos
Given: se realizan lecturas o alertas constantes
When: se procesan
Then: se almacena con un timestamp en la base de datos 
```
    **Auditoria IA: Bien planteado, pero falta estrategia de almacenamiento y explotación de datos.

    Claridad: Se almacenan lecturas con timestamp.

    Riesgos:
    ¿Qué motor de base de datos se usará?

    ¿Se requiere compresión o limpieza de datos antiguos?

    Mejora: Definir retención de datos y acceso para análisis (dashboards, exportación).
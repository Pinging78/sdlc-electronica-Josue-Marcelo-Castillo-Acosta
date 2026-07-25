# Product Backlog

## US1 - Lectura periodica de los sensores
Para este sistema se requiere leer 10 sensores de temperatura y humedad cada 30 segundos para tenerlos datos actualizados

**Story points:** 3
**Priorización MoSCoW:** Must Have

```gherkin
Scenario: lectura de los sensores activos
Given: los sensores están conectados y operando
When: pasan 30 segundos
Then: el sistema registra una nueva lectura de todos los sensores
```

```gherkin
Scenario: sensor no responde a tiempo
Given: un sensor no envía su lectura dentro del ciclo de 30 segundos
When: se cumple el tiempo límite
Then: el sistema reintenta una vez antes de marcarlo como fallido
```


## US2 - Deteccion de anomalias
Como desarrollador quiero detectar anomalias en las lecturas o falsos positivos de una alerta por lo que se hace la deteccion de estos casos y evitamos problemas a futuro

**Story points:** 5
**Priorización MoSCoW:** Must Have

```gherkin
Scenario: deteccion de anomalias
Given: al recibir una lectura nueva
When: supera el umbral configurado del sensor
Then: existe una anomalia
```


## US3 - Generacion de alertas
Los encargados de la bodega deben de recibir una alerta cuando una anomalia se presente, esto para que puedan actuar en tiempo y forma para no dañar su mercancia

**Story points:** 3
**Priorización MoSCoW:** Must Have

```gherkin
Scenario: anomalia encontrada
Given: se detecto la anomalia
When: el sistema la procesa y verifica que no solo sea un falso positivo
Then: envia una alerta en menos de 5 segundos por el canal configurado
```


## US4 - Identificar el sensor de origen
Una vez que la alerta se detecte se debe de localizar para saber en donde es el problema

**Story points:** 2
**Priorización MoSCoW:** Should Have

```gherkin
Scenario: alerta incluye el sensor de origen
Given: se genera una alerta
When: se registra
Then: incluye el ID del sensor y su ultima ubicacion conocida
```
    

## US5 - Deteccion de sensor desconectado o descompuesto
Por prevencion se debe de manejar el caso de la perdida de algun sensor, esto para evitar daños por silencio o la ultima lectura guardada que se repite constantemente

**Story points:** 2
**Priorización MoSCoW:** Could Have

```gherkin
Scenario: un sensor deja de responder
Given: un sensor no envia datos en 2 ciclos consecutivos 
When: se confirma la ausencia tras el reintento
Then: se marca como 'sin respuesta' y se genera una alerta separada
```
    


## US6 - Historial de lecturas y anomalias
Como desarrollador quisiera un historial de lecturas y anomalias para tener un mejor control y la capacidad de analizar los datos cuando se requiera

**Story points:** 5
**Priorización MoSCoW:** Could Have

```gherkin
Scenario: los sensores estan activos
Given: se realizan lecturas o alertas
When: se procesan
Then: se almacena con un timestamp en SQlite para consultas posteriores
```

## US7- Configurar umbrales para cada sensor
como desarrollador deberia de tener una opcion para cambiar los umbrales para tener una mayor variedad de productos sin perdidas economicas

**Story points:** 5
**Priorización MoSCoW:** Should Have

```gherkin
Scenario: modificar umbral de un sensor
Given: existe un sensor registrado con un umbral por defecto
When: el desarrollador asigna un nuevo umbral a ese sensor
Then: el sistema usa el nuevo umbral en la siguiente detección de anomalías
```


## US8 - Exportar el historial de lecturas
como desarrollador tengo que verificar los datos guardados y analizar el historial para determinar el origen de las anomalias 

**Story points:** 3
**Priorización MoSCoW:** Could Have

```gherkin
Scenario: exportar historial a archivo
Given: existen lecturas y anomalías almacenadas en el sistema
When: el desarrollador solicita exportar el historial
Then: se genera un archivo (CSV o JSON) con las lecturas y su clasificación
```


## US9 - Registrar o eliminar sensores del sistema
si el sensor necesita un cambio por falla y no se cuenta con el mismo sensor seria mas practico reemplazarlo por un sensor compatible a esperar el mismo modelo

**Story points:** 8
**Priorización MoSCoW:** Should Have

```gherkin
Scenario: reemplazar un sensor dado de baja
Given: un sensor fue marcado como descompuesto
When: se registra un nuevo sensor compatible en su lugar
Then: el sistema asocia las nuevas lecturas al sensor reemplazado sin perder el historial anterior
```

## US10 - Consultar estado de los sensores en tiempo real
como encargado debo de saber el estado actual de los sensores y si presenta una anomalia cambiarlo lo antes posible

**Story points:** 5
**Priorización MoSCoW:** Should Have

```gherkin
Scenario: consultar estado general de sensores
Given: el sistema tiene sensores activos y algunos con anomalías
When: el encargado solicita el estado actual
Then: se muestra una lista con el estado (normal/anomalía/sin respuesta) de cada sensor
```
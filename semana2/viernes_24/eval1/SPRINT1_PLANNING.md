# Sprint 1 Planning

## Sprint Goal
Contar con un sistema capaz de leer los sensores de la bodega, detectar 
condiciones anómalas de temperatura y humedad, y notificar al encargado 
en tiempo real, para prevenir daños a la mercancía

## Historias seleccionadas para este sprint

### US1 - Lectura periódica de sensores
**Justificación:** Es la base de todo el sistema, sin esto no hay datos y no se puede analizar
**Tareas:**
- [ ] Implementar clase SensorReading (2h)
- [ ] Test de lectura individual y validación de datos (2h)
- [ ] Manejo de sensor sin respuesta con reintento (3h)

### US2 - Detección de anomalías
**Justificación:** Es el corazón del sprint goal, sin este apartado no hay sistema de monitoreo real
**Tareas:**
- [ ] Implementar AnomalyDetector con umbrales inyectados en el constructor (3h)
- [ ] Tests con distintos umbrales por sensor (2h)
- [ ] Test de caso límite (justo en el umbral) (1h)

### US3 - Generación de alertas
**Justificación:** Sin al detectar la anomalía no se notifica una alerta no sirve de nada para el encargado
**Tareas:**
- [ ] Definir interfaz abstracta AlertStrategy (2h)
- [ ] Implementar ConsoleAlertStrategy (1h)
- [ ] Implementar FileAlertStrategy (2h)
- [ ] Tests de ambas estrategias (2h)

### US4 - Identificar el sensor de origen
**Justificación:** Una alerta sin saber cuál sensor falló no permite actuar rápido
**Tareas:**
- [ ] Incluir sensor_id y ubicación en el objeto de alerta (2h)
- [ ] Test de que la alerta contiene el origen correcto (1h)

### US5 - Detección de sensor desconectado
**Justificación:** Previene que el sistema confunda silencio con normalidad esto seria un riesgo para la bodega
**Tareas:**
- [ ] Lógica de reintento tras 2 ciclos sin respuesta (3h)
- [ ] Test de sensor desconectado vs sensor lento (2h)

### US7 - Configurar umbrales por sensor
**Justificación:** Distintos productos necesitan distintos umbrales; sin esto AnomalyDetector sería rígido
**Tareas:**
- [ ] Método para asignar/actualizar umbral de un sensor (2h)
- [ ] Test de cambio de umbral en caliente (2h)

## Historias fuera de este sprint (quedan en el backlog)
US6 (historial), US8 (exportar), US9 (registrar/eliminar sensores), US10 
(consulta en tiempo real)
no son fundamentales para este Sprint Goal y se pueden abordar en un sprint posterior

## Definition of Done
Ver `DEFINITION_OF_DONE.md`
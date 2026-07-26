# Sprint Retrospective

## Qué salió bien
- Se completaron las 3 historias núcleo (SensorReading, AnomalyDetector, AlertManager) con TDD estricto
- Cobertura de tests se mantuvo arriba del 80%
- Se aplicó el patrón Strategy correctamente en AlertManager, permitiendo agregar canales sin modificar código existente

## Qué mejorar
- Resolver problemas de entorno (venv, WSL, permisos) consumió tiempo que pudo ir a más historias
- Faltó completar US4, US5 y US7 del planning por límite de tiempo
- Conocer mas formas de tener los mismos resultados y mejor o más extensos

## Acción concreta
- Documentar el setup del entorno (venv + WSL) en un README para no perder tiempo en el siguiente sprint si se repite un problema similar.
- Investigar mas formas de hacer el mismo proceso
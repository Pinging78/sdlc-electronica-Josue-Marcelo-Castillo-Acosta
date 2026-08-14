# Resumen Arquitectónico: Microservicios y la Estrategia "Monolith First"

## 1. Fowler — "Microservices: a definition of this new architectural term"

### Idea Central
La arquitectura de microservicios consiste en diseñar una aplicación como un conjunto de servicios pequeños e independientes. Cada uno corre en su propio proceso, se comunica a través de la red (HTTP/REST, RPC o mensajería) y es desplegable de forma totalmente autónoma

### 9 Características Clave

1. Componentización vía servicios: En lugar de librerías compartidas en un mismo proceso, cada pieza es un servicio independiente que se puede actualizar, desplegar o reemplazar sin tocar el resto del sistema

2. Organizados alrededor de capacidades de negocio (Ley de Conway): Equipos multifuncionales (*cross-functional*) dueños de un flujo completo (ej. "pedidos" o "facturación"), en vez de silos divididos por capas técnicas (frontend, backend, DBAs)

3. Productos, no proyectos: Rige el principio *"You build it, you run it"*. El equipo mantiene la propiedad y responsabilidad del servicio durante toda su vida en producción, no solo hasta la entrega inicial

4. Smart endpoints and dumb pipes: La lógica de negocio reside exclusivamente en los microservicios; se evitan middlewares complejos orquestadores (como los ESB tradicionales) a favor de protocolos estándar y buses de eventos simples

5. Gobierno descentralizado: Cada equipo tiene la libertad técnica de elegir el lenguaje, framework o herramienta óptima para resolver su problema específico (Polyglot Programming)

6. Datos descentralizados: Cada microservicio administra su propia base de datos (Polyglot Persistence). Se eliminan las bases de datos monolíticas compartidas y las transacciones ACID globales se reemplazan por consistencia eventual y compensaciones

7. Automatización de infraestructura: CI/CD continuo, pruebas automatizadas y despliegues sin fricción son un requisito técnico obligatorio, no un lujo opcional

8. Diseño para el fallo: Se asume desde el diseño que cualquier dependencia de red puede fallar. Se implementan patrones como Circuit Breaker, degradación elegante y observabilidad en tiempo real

9. Diseño evolutivo: Permite cambiar, refactorizar o reescribir un microservicio puntual versionando sus contratos sin romper el funcionamiento de los consumidores

### El Costo Real ("Microservice Premium")
Fowler enfatiza que los microservicios introducen una sobrecarga considerable: latencia de red, complejidad en consistencia de datos, pruebas distribuidas y monitoreo exigente. Solo valen la pena cuando la complejidad del dominio y el tamaño de la organización lo demandan

## 2. Fowler — "MonolithFirst"

### Idea Central
Fowler aconseja iniciar casi cualquier nuevo desarrollo con un monolito modular bien estructurado, incluso si la meta a largo plazo es una arquitectura de microservicios

### Razones Clave
Fricción al definir límites (Bounded Contexts): Al inicio de un proyecto es cuando menos se conoce el dominio. Definir fronteras de microservicios a ciegas suele resultar en límites incorrectos

Costo de refactorización: Corregir límites entre módulos dentro de un monolito requiere simples refactorizaciones de código; corregir límites entre microservicios ya desplegados exige migrar esquemas de base de datos, adaptar APIs y coordinar múltiples repositorios

Patrón de éxito en la industria: Casi todos los sistemas de microservicios exitosos comenzaron como monolitos que se dividieron gradualmente cuando apareció el dolor real (múltiples equipos pisándose código o necesidades puntuales de escalado independiente)

Riesgo del inicio distribuido: Arrancar de cero con microservicios acumula la complejidad operativa de la distribución antes de haber validado siquiera el modelo de negocio

#### Conclusión: 
con esta informacion puedo apreciar que el proyecto que ibamos desarrollando siguió el consejo de "MonolithFirst" desde la semana 3: empezamos con un monolito en capas, sin microservicios, porque en ese momento ni siquiera sabíamos bien dónde estarían los límites naturales del dominio (sensor vs reading vs alerta). Con el tiempo esos límites se fueron aclarando solos (por ejemplo, separar ReadingService de SensorService en la semana 3), lo cual coincide justo con lo que dice Fowler: los límites se descubren mejor con el código en la mano, no se adivinan de antemano

De las 9 caracteristicas de microservicios, la que mas resalta para un proyecto como este es la del "Microservice Premium" — el costo de red, consistencia de datos, y monitoreo distribuido no tendria sentido para una API que corre para un solo desarrollador y una bodega. Si SensorHub creciera a monitorear varias bodegas con equipos distintos manteniendo sensores vs alertas vs reportes, ahi si empezaria a justificarse dividir en servicios
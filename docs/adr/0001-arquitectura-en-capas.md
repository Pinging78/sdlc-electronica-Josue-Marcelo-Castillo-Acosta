# Estado
La arquitectura del proyecto SensorHub se basa en un monolito en capas.

# Contexto
SensorHub es un proyecto académico de un solo desarrollador para un API de monitoreo de sensores de temperatura y humedad en un almacén industrial. No hay una necesidad actual de escalar componentes de manera independiente.

# Decisión
Se ha decidido utilizar una arquitectura de monolito en capas (routers -> services -> repositories -> models) en lugar de microservicios para este proyecto.

# Alternativas consideradas
Se consideró la arquitectura de microservicios, pero se rechazó debido a la complejidad adicional que introduce y la falta de necesidad de escalar componentes de manera independiente en este proyecto. Según Martin Fowler en su artículo "Microservices", los microservicios son adecuados para proyectos que requieren una gran escalabilidad y flexibilidad, lo que no es el caso de SensorHub. Además, en su artículo "MonolithFirst", Fowler sugiere comenzar con un monolito y luego refactorizar a microservicios si es necesario.

# Consecuencias
La decisión de utilizar un monolito en capas simplifica la arquitectura del proyecto y reduce la complejidad. Sin embargo, también limita la capacidad de escalar componentes de manera independiente. En la revisión paralela de la semana pasada, un revisor encontró un router que llamaba directamente al repositorio, saltándose la capa de servicios. Esto destaca la importancia de hacer cumplir la separación de capas para evitar acoplamiento innecesario y mejorar la mantenibilidad del código.

# Referencias
- Martin Fowler: "Microservices" (https://martinfowler.com/articles/microservices.html)
- Martin Fowler: "MonolithFirst" (https://martinfowler.com/bliki/MonolithFirst.html)

## Nota sobre modelos usados
Se probaron tres modelos distintos con Aider para esta tarea: GitHub Copilot (gpt-4o), Anthropic Claude (sin API key disponible, se documenta el intento sin completarlo) y Groq (llama-3.3-70b-versatile), que finalmente genero este documento.
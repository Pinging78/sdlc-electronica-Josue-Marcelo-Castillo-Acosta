# [14/07/2026] — Semana 1 / Lunes — Funciones puras sobre Reading
## Herramienta usada: Claude / GitHub Copilot / Gemini

### ¿En qué me ayudó?
- Les pedi codigos de ejemplo para adaptarlo después en codigos simples (conversión, umbral, serialización)
- Explicar qué es dataclass, frozen, Enum y el patrón Arrange-Act-Assert y como hacerlo correctamente

### ¿Qué hice yo?
- Adapté los ejemplos a mi propio caso  (temperatura y humedad) y si tenia dudas preguntaba a la IA para tener una mejor retroalimentación
- Corrí mypy y ruff para verificar mi código
- Corregi ciertos errores que provocaba por olvidarme de colocar definiciones o escribir mal los nombres

### ¿Qué aprendí?
- Cómo funciona `replace()` en dataclasses inmutables, que en pocas palabras en lugar de sobre escribir la lectura crea una nueva continuamente 
- Patrón Arrange-Act-Assert para escribir pruebas o realizar acciones de una manera facil
# [16/07/2026] — Semana 1 / Jueves - SOLID completo: I y D

## Herramienta usada: Claude 

## Prompt: En base este codigo dame ejemplos de los protocolos DIP y ISP
primero me dio la direfencia de usar el protocol en lugar del ABC, que es que con ABC se tiene que heredar de forma explicita y con protocol no se necesario heredarlo por el structural subtyping

el ISP hace que en una interfaz los metodos de read/write/calibrate/reset se implementan en protocolos chicos y cada sensor por ejemplo un sensor pueda usar los metodos que necesite

el DIP no crea ni depende de forma directa de una implementacion concreta, depende de la abstracion y que tenga una implementacion externa

### ¿En qué me ayudó?
a entender mejor los conceptos ya dados, ademas de evitar los errores que tuve en el camino que pasaban por faltas de ortografia que no podia ver

### ¿Qué hice yo?
intentar seguir una estructura parecida a los codigos anteriores, en caso de quedarme trabado preguntar por alguna solucion y seguir adelante

### ¿Qué aprendí?
el uso de los ISP y DIP que pueden ser mas utiles que los dataclass por el apartado de la herencia

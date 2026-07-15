# [14/07/2026] — Semana 1 / Martes — FSM orientada a objetos

## Herramienta usada: Claude 

## Prompt: ¿Que es fsm?
Ya que no me acordaba que significaban las siglas le pedi que me lo explicara y me brindo un ejemplo que es igual de un semaforo que seria este: 

    Estados: ROJO, VERDE, AMARILLO

    ROJO → (pasa el tiempo) → VERDE
    VERDE → (pasa el tiempo) → AMARILLO
    AMARILLO → (pasa el tiempo) → ROJO

Y en el codigo que me brindo lo hizo de esta forma:

    def next_state(self) -> None:
    if self._state == TrafficLightState.RED:
        self._state = TrafficLightState.GREEN
    elif self._state == TrafficLightState.GREEN:
        self._state = TrafficLightState.YELLOW
    elif self._state == TrafficLightState.YELLOW:
        self._state = TrafficLightState.RED
        self._cycle_count += 1

Pero no me agrado ya que es complicado de entender y un poco más tedioso asi que elegi el codigo ya brindado

Despues recorde la estructura del codigo del lunes y me parecio buena idea seguir la misma logica

### ¿En qué me ayudó?
A comprender mejor el codigo brindado en la guia del estudiante, como por ejemplo el apartado del __init__ que no comprendi completamente y solucionar posibles errores como uno que tuve de sangria y no encontraba el error

### ¿Qué hice yo?
Adapté los codigos del test_reading para hacer funcionar correctamente y facil los ejercicios, ya teniendo esa base fue más facil de terminarlos


### ¿Qué aprendí?
Como funcionan el .transition(), utilizar correctamente las variables y el ._cycle_count 
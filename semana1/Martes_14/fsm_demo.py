from enum import Enum, auto


class TrafficLightState(Enum): #define los estados del semaforo y le asigna valores automaticamente
    RED = auto()
    GREEN = auto()
    YELLOW = auto()

class TrafficLightFSM:
    def __init__(self) -> None: #constuye la clase TrafficLightFSM y la establece en rojo
        self._state = TrafficLightState.RED
        self._cycle_count = 0
        #el guion bajo despues del punto indica que es interno y no se debe de modificar desde fuera de la clase


    @property #convierte el metodo a modo lectura como si fuera un atributo normal y no hay necesidad de usar parentesis
    def state(self) -> TrafficLightState:#define el metodo state y regresa el TrafficLightState
        return self._state #regresa el valor definido en el __init__

#esto hace que la unica forma de cambiar el estado sea con metodos controlados
#como el next_state y asi evitar que no se cambie de otra forma

    def transition(self) -> TrafficLightState: #hace el cambio de estado y regresa el nuevo
        transitions = { #crea un diccionario las cuales son los cambios de estado
            TrafficLightState.RED: TrafficLightState.GREEN,
            TrafficLightState.GREEN: TrafficLightState.YELLOW,
            TrafficLightState.YELLOW: TrafficLightState.RED
        }
        self._state = transitions[self._state] #busca en el diccionario cual es el siguiente estado en self._state y lo asigna
        self._cycle_count += 1 #incrementa 1 al contador cada que hay una transicion
        return self._state #regresa el nuevo estado
from fsm_demo import TrafficLightFSM, TrafficLightState


def test_estado_inicial_rojo(): 
    semaforo = TrafficLightFSM() #se crea un semaforo
    assert semaforo.state == TrafficLightState.RED #revisa si inicia en rojo

def test_cambio_de_rojo_a_verde():
    semaforo = TrafficLightFSM() #semaforo nuevo
    nuevo_estado = semaforo.transition() #pasa de rojo a verde
    assert nuevo_estado == TrafficLightState.GREEN #comprueba si hizo el cambio

def test_cambio_de_verde_a_amarillo():
    semaforo = TrafficLightFSM() #otro semaforo
    semaforo.transition() #pasa de rojo a verde
    nuevo_estado = semaforo.transition() #ahora de verde a amarillo
    assert nuevo_estado == TrafficLightState.YELLOW

def test_cambio_de_amarillo_a_rojo():
    semaforo = TrafficLightFSM() #otro semaforo
    semaforo.transition() #rojo a verde
    semaforo.transition() #verde a amarillo
    nuevo_estado = semaforo.transition() #amarillo a rojo
    assert nuevo_estado == TrafficLightState.RED
#la diferencia entre el cambio de amarillo a rojo y el ciclo completo
#es que solo esta hecho para probar que cambie de amarillo a rojo y solo es una transicion puntual


def test_ciclo_completo():
    semaforo = TrafficLightFSM() #otro semaforo
    semaforo.transition() #rojo a verde
    semaforo.transition() #verde a amarillo
    semaforo.transition() #amarillo a rojo
    assert semaforo.state == TrafficLightState.RED
    assert semaforo._cycle_count == 3
#aqui es el resultado acumulado, entonces se asegura que el cambio correctamente y termino donde debia
#ademas el contador llevo bien la cuenta, por eso se utiliza el ._cycle_count ya que si importa
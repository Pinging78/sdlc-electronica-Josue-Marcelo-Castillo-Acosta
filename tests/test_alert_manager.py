from app.services.alert_manager import AlertManager


def test_alerta_se_registra():
    manager = AlertManager()
    manager.notificar("sensor 1 (temperatura) reporto 40, supera umbral de 35")
    assert len(manager.alertas) == 1

def test_multiples_alertas_se_acumulan():
    manager = AlertManager()
    manager.notificar("alerta 1")
    manager.notificar("alerta 2")
    assert len(manager.alertas) == 2

def test_alerta_guarda_el_mensaje_correcto():
    manager = AlertManager()
    manager.notificar("mensaje de prueba")
    assert manager.alertas[0] == "mensaje de prueba"
from AlertManager import AlertManager, ConsoleAlertStrategy

def test_enviar_alerta_por_consola(capsys): #capsys captura lo que imprime en la consola y lo verifica
    strategy = ConsoleAlertStrategy()
    manager = AlertManager(strategy)
    manager.notificar("Temperatura alta en S1")
    
    capturado = capsys.readouterr()
    assert "Temperatura alta en S1" in capturado.out
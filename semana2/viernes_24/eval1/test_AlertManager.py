from AlertManager import AlertManager, ConsoleAlertStrategy, FileAlertStrategy


def test_enviar_alerta_por_consola(capsys): #capsys captura lo que imprime en la consola y lo verifica
    strategy = ConsoleAlertStrategy()
    manager = AlertManager(strategy)
    manager.notificar("Temperatura alta en S1") #llama a strategy.enviar() y lo imprime
    
    capturado = capsys.readouterr() #recoge lo de la consola
    assert "Temperatura alta en S1" in capturado.out #verificamos si fue impreso

def test_enviar_alerta_por_archivo(tmp_path): #carpeta temporal
    archivo = tmp_path / "alertas.log" #ubicacion
    strategy = FileAlertStrategy(str(archivo))
    manager = AlertManager(strategy)
    manager.notificar("Humedad alta en S2")
    
    contenido = archivo.read_text()
    assert "Humedad alta en S2" in contenido
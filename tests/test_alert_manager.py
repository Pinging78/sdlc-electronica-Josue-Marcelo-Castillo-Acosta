# test OCP

from app.services.alert_manager import (
    AlertManager,
    ConsoleAlertStrategy,
    FileAlertStrategy,
)


def test_console_strategy_registra_en_consola(capsys):
    manager = AlertManager(strategy=ConsoleAlertStrategy())
    manager.notificar("alerta de prueba")
    captured = capsys.readouterr()
    assert "alerta de prueba" in captured.out


def test_file_strategy_escribe_en_archivo(tmp_path):
    archivo = tmp_path / "alertas.log"
    manager = AlertManager(strategy=FileAlertStrategy(str(archivo)))
    manager.notificar("alerta de archivo")
    contenido = archivo.read_text()
    assert "alerta de archivo" in contenido
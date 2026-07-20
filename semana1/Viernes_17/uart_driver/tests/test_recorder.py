import json
from recorder import DataRecorder

def test_save_escribe_json_valido_en_archivo(tmp_path) -> None:
    """Verifica que DataRecorder.save() escriba un JSON valido y
    legible en el archivo especificado."""
    archivo = tmp_path / "datos.jsonl" #crea una carpeta temporal con el nombre "datos.jsonl"
    recorder = DataRecorder(str(archivo)) #los datos del archivo los pasa a texto por aqui
    recorder.save({"protocolo": "modbus", "direccion": 1})
    contenido = archivo.read_text().strip()
    data = json.loads(contenido) #lee el texto y lo verifica
    assert data["protocolo"] == "modbus"
    assert data["direccion"] == 1


def test_save_convierte_bytes_a_hexadecimal(tmp_path) -> None:
    """Verifica que un campo bytes se convierta a texto hexadecimal
    antes de guardarse, ya que JSON no soporta bytes directamente."""
    archivo = tmp_path / "datos.jsonl"
    recorder = DataRecorder(str(archivo))
    recorder.save({"datos": b"\x10\x20"}) #convierte los bytes en hexadecimal
    contenido = archivo.read_text().strip() 
    data = json.loads(contenido) 
    assert data["datos"] == "1020"


def test_save_multiples_veces_agrega_lineas_json(tmp_path) -> None:
    """Verifica que llamar save() varias veces agregue una linea de
    JSON por cada llamada, sin sobrescribir las anteriores."""
    archivo = tmp_path / "datos.jsonl"
    recorder = DataRecorder(str(archivo))
    recorder.save({"protocolo": "modbus"})
    recorder.save({"protocolo": "nmea"})    #verifica los datos y los pone en lista
    lineas = archivo.read_text().splitlines()
    assert len(lineas) == 2 #comprueba si estan en lista
    data1 = json.loads(lineas[0])
    data2 = json.loads(lineas[1])   #los asigna en el byte 1 y en en 2
    assert data1["protocolo"] == "modbus" #verifica
    assert data2["protocolo"] == "nmea"
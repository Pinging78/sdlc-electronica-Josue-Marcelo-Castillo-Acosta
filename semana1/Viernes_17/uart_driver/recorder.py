import json

class DataRecorder:

    def __init__(self, path: str) -> None:
        self._path = path

    def save(self, data: dict) -> None:
        data_serializable = self._hacer_serializable(data)
        with open(self._path, "a") as f:
            f.write(json.dumps(data_serializable) + "\n")

    def _hacer_serializable(self, data: dict) -> dict:
        resultado = {}
        for clave, valor in data.items():
            if isinstance(valor, bytes):
                resultado[clave] = valor.hex()
            else:
                resultado[clave] = valor
        return resultado
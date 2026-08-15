class AlertManager:
    def __init__(self):
        self.alertas = []

    def notificar(self, mensaje: str):
        self.alertas.append(mensaje)
#codigo base para funcionamiento de las alertas
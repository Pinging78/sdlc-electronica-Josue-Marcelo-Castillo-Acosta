from abc import ABC, abstractmethod

class MessageParser(ABC):
    @abstractmethod
    def can_parse(self, raw: bytes) -> bool: ...
    @abstractmethod
    def parse(self, raw: bytes) -> dict: ...

class ModbusParser(MessageParser): #frames modbus RTU
    def can_parse(self, raw: bytes) -> bool:
#un frame necesita 1 byte de direccion + 1 byte de funcion + 2 bytes de CRC
        if len(raw) < 4: #si el byte es menor a 4 no es valido
            return False
        return self._crc_valido(raw)

    def parse(self, raw: bytes) -> dict:
        if not self.can_parse(raw):
            raise ValueError("frame Modbus invalido")

        direccion = raw[0]    
        funcion = raw[1]
        datos = raw [2:-2] 

        return {
            "protocolo": "modbus",
            "direccion": direccion,
            "funcion": funcion,
            "datos": datos,
        }

    def _crc_valido(self, raw: bytes) -> bool:
        crc_recibido = raw[-2:]
        crc_calculado = self._calcular_crc(raw[:-2])
        return crc_recibido == crc_calculado

    def _calcular_crc(self, data: bytes) -> bytes:
        crc = 0xFFFF
        for byte in data:
            crc ^= byte
            for _ in range (8):
                if crc & 1:
                    crc = (crc >> 1) ^ 0xA001
                else:
                    crc >>= 1
        return crc.to_bytes(2, byteorder = "little")
#algoritmo estándar de CRC-16 Modbus: agarra todos los bytes de data y los "mezcla" matemáticamente en un solo número de 16 bits
#y si un solo bit cambia en el mensaje original, el resultado sale completamente distinto

class NMEAParser(MessageParser):
    def can_parse(self, raw: bytes) -> bool: #llega el mensaje como bytes
        try:
            texto = raw.decode("ascii") #se convierte a texto legible
        except UnicodeDecodeError:
            return False
    
        if not texto.startswith("$GPGGA"): #si el texto no incia con $GPGGA no es valido
            return False
    
        if "*" not in texto: #revisa si hay un * y si si llama a _checksum_valido para verificarlo
            return False
        return self._checksum_valido(texto)
#se convierten los bytes → str con .decode(), despues verifica 3 cosas en cadena: que sea texto válido, que empiece con $GPGGA, y que checksum (*) sea correcto


    def _checksum_valido(self, texto: str) ->  bool:
        cuerpo, checksum_recibido = texto[1:].split("*")
        #texto[1:] quita el primer caracter que es $ y .split("*") divide en 2 el texto en donde esta *
        checksum_calculado = 0
        for char in cuerpo:
            checksum_calculado ^= ord(char)
        #calculamos un checksum del cuerpo letra por letra utilizando una XOR
        checksum_hex = f"{checksum_calculado:02X}"
        return checksum_hex == checksum_recibido.strip()
        #se convierte el numero calculado en hexadecimal y se compara con el recibido si no coinciden esta corrupto

    def parse(self, raw: bytes) -> dict:
        if not self.can_parse(raw):
            raise ValueError("NMEA invalida")
    
        texto = raw.decode("ascii")
        cuerpo = texto.split("*")[0] #antes del * ya esta validado
        campos = cuerpo.split(",") #divide el texto en una lista y la corta en cada coma

        return {
            "protocolo": "nmea",
            "tipo": campos[0],
            "hora": campos[1],
            "latitud": campos[2],
        }
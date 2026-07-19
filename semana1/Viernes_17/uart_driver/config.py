from dataclasses import dataclass

BaudRate_Validos = {1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200}
Parity_validos = {"N", "E", "O"} #None, Even, Odd
Stop_Bits_validos = {1, 2}

@dataclass(frozen = True)
class UartConfig:
    baudrate: int
    parity: str
    stop_bits: int
    timeout: float

    def __post_init__(self): #despues de ingresar los datos los verifica que esten correctos
        if self.baudrate not in BaudRate_Validos:
            raise ValueError (f"baudrate invalido: {self.baudrate}")
        
        if self.parity not in Parity_validos:
            raise ValueError(f"parity invalido: {self.parity}")
        
        if self.stop_bits not in Stop_Bits_validos:
            raise ValueError(f"stop_bits invalido: {self.stop_bits}")
        
        if self.timeout <= 0:
            raise ValueError(f"timeout debe ser mayor que 0: {self.timeout}")

# [17/07/2026] — Semana 1 / Viernes - Ejercicio integrador: “El Driver Modernizado”

## Herramienta usada: Claude/Copilot

## Prompt: ayudame a tener una base para la comunicacion uart
ya que no sabia nada acerca de la comunicacion uart no tuve de otra que investigar y empaparme de informacion, una vez con el conocimiento iba avanzando y cada que tenia duda iba a preguntar

copilot sugirio varias ideas para los test de config y son los siguientes:
1.-
    def test_baudrate_invalido()
    """Verifica que UartConfig rechace un baudrate fuera de la lista
    de valores permitidos, con el mensaje de error correspondiente."""
        with pytest.raises(ValueError) as excinfo:
            config = UartConfig(baudrate=12345, parity="N", stop_bits=1, timeout=1.0)
        assert "baudrate invalido" in str(excinfo.value)

se ve bien, utilizo bien las variables solo le falto el -> None al final del def ya que esa estructura segui en el codigo y la variable config talvez se pueda quitar y dejar solo UartConfig

2.-
    def test_config_es_inmutable() -> None
    """Verifica que UartConfig no se pueda modificar despues de creada,
    aventando FrozenInstanceError al intentar cambiar un campo."""
    config = UartConfig(baudrate=9600, parity="N", stop_bits=1, timeout=1.0)
    with pytest.raises(dataclasses.FrozenInstanceError):
        config.baudrate = 19200

para evitar que fallara se importo la funcion FrozenInstanceError de dataclasses

3.-
    def test_config_valida_creada_correctamente() -> None
 """Verifica que UartConfig se cree sin problema cuando todos los
    valores son validos, y que los campos queden con los valores dados."""
    config = UartConfig(baudrate=9600, parity="N", stop_bits=1, timeout=1.0)
    assert config.baudrate == 9600
    assert config.parity == "N"
    assert config.stop_bits == 1
    assert config.timeout == 1.0

este ultimo me parecio bien ya que define los valores y despues comprueba que cada uno sea correcto

para test_parser:
Copilot sugirió los 3 tests, tenian la logica correcta y abarcaba más que mi primer idea (verificaba más campos, calculaba el checksum de NMEA dinámicamente en vez de fijo). Le agregué solo los docstrings y el type hint -> None en las 3 firmas

para test_device:
Copilot sugirió usar un DummyParser que es una implementación falsa de MessageParser en vez del ModbusParser real, para probar UartDevice de forma aislada. Esto demuestra el valor practico de DIP/LSP que vimos la lectura por lo que  la sugerencia fue funcional de inmediato, solo le agregué docstrings y type hints

para test_recorder:
copilot sugirio el tmp_path para poder "emular" un archivo externo y asi obtener los datos, verifico todo correctamente y aunque habia algunas lineas que no conocia creo saber para que funciona

### ¿En qué me ayudó?
investigar que es lo que necesitaba para funcionar, como es que funciona, que podria mejorar y en base a lo que requeria en la guia del estudiante cumplia todos los parametros, para poder avanzar correctamente

### ¿Qué hice yo?
verificar que todo estuviera bien, hacer diferentes propuestas y saber si funcionaban, si no buscar porque no y resolver cada duda que tenia

### ¿Qué aprendí?
como es que funciona la comunicacion uart desde adentro, nuevas funciones y usos de nuevas funciones que puede que no sepa bien como funciona ahorita, pero se iran perfeccionando

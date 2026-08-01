# AI_LOG.md

## Martes 28 - Persistencia con SQLAlchemy 2.x
Pedí ayuda para configurar el engine y sessionmaker con SQLAlchemy 2.x (DeclarativeBase, Mapped, mapped_column). Tambien resolvi un problema de firewall en WSL/360 Total Security que bloqueaba las conexiones al server lo que me dio muchos problemas para acceder a la api

## Miercoles 29 - Patron repositorio y capa de servicio
Pedi ayuda para separar la logica en capas: repository (accede a la BD), service (logica de negocio) y main (endpoints), en vez de tener todo mezclado, esto para tener mas orden y que se entienda mejor

## Viernes 31 - Validacion Pydantic y deteccion de anomalias
Pedi ayuda para armar un schema Pydantic que valide la unidad y el rango fisico segun el tipo de sensor (temperatura/humedad), y para agregar deteccion de anomalias (alerta cuando se supera un umbral) o errores cuando supera los rangos fisicos
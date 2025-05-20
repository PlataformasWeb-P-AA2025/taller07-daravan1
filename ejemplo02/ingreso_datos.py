from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()


with open("clubs.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        nombre, deporte, fundacion = linea.strip().split(";")
        club = Club(nombre=nombre, deporte=deporte, fundacion=int(fundacion))
        session.add(club)
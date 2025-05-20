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

# Se obtienen todos los registros de clubes para crear objetos Club y enviarlos a la base de datos
with open("data/datos_clubs.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        # Se separan los datos por el delimitador ";"
        nombre, deporte, fundacion = linea.strip().split(";") 
        club = Club(nombre=nombre, deporte=deporte, fundacion=int(fundacion))
        session.add(club)

# Se obtienen todos los registros de jugadores para crear objetos Jugador y enviarlos a la base de datos
with open("data/datos_jugadores.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        # Se separan los datos por el delimitador ";"
        nombre_club, posicion, dorsal, nombre = linea.strip().split(";") 
        # Se busca el club correspondiente al jugador por su nombre
        club = session.query(Club).filter_by(nombre=nombre_club).one()
        #Se relaciona el jugador con el club
        jugador = Jugador(nombre=nombre, dorsal=int(dorsal), posicion=posicion, club_id=club.id) 
        session.add(jugador)

# Se giardan los cambios en la base de datos
session.commit()

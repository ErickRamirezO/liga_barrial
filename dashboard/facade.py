# myapp/facade.py

from .models import Equipo, Jugador, Arbitro, Partido, Presidente, Vocalia
from .observer import NotificationManager

class LeagueManager:
    def add_team(self, nombre, numero_jugadores, logo, slogan, presidente, capitan):
        nuevo_equipo = Equipo(
            nombre_equipo=nombre,
            cantidad_jugadores=numero_jugadores,
            logo=logo,
            slogan=slogan,
            presidente=presidente,
            capitan=capitan
        )
        nuevo_equipo.save()

    def add_player(self, nombre, apellido, edad, cedula, dorsal, posicion, goles):
        nuevo_jugador = Jugador(
            nombre=nombre,
            apellido=apellido,
            edad=edad,
            cedula=cedula,
            dorsal=dorsal,
            posicion=posicion,
            goles=goles
        )
        nuevo_jugador.save()

    def add_arbitro(self, nombre, apellido, edad, cedula, telefono, federacion):
        nuevo_arbitro = Arbitro(
            nombre=nombre,
            apellido=apellido,
            edad=edad,
            cedula=cedula,
            telefono=telefono,
            federacion=federacion
        )
        nuevo_arbitro.save()

    def add_presidente(self, nombre, apellido, edad, cedula, nombre_equipo):
        nuevo_presidente = Presidente(
            nombre=nombre,
            apellido=apellido,
            edad=edad,
            cedula=cedula,
            nombre_equipo=nombre_equipo
        )
        nuevo_presidente.save()

    def add_vocalia(self, amonestaciones, titulares_del_partido, jugadores_con_anotaciones, faltas):
        nueva_vocalia = Vocalia(
            amonestaciones=amonestaciones,
            titulares_del_partido=titulares_del_partido,
            jugadores_con_anotaciones=jugadores_con_anotaciones,
            faltas=faltas
        )
        nueva_vocalia.save()

    def schedule_match(self, estadio, equipo, fecha, arbitro, jugador, presidente):
        nuevo_partido = Partido(
            estadio=estadio,
            equipo=equipo,
            fecha=fecha,
            arbitro=arbitro,
            jugador=jugador,
            presidente=presidente
        )
        nuevo_partido.save()
        NotificationManager().notify(nuevo_partido)

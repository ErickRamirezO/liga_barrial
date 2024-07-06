from django.db import models
from django.contrib.auth.models import User
import copy

class Persona(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    cedula = models.IntegerField()

    class Meta:
        abstract = True
        
class Arbitro(Persona):
    telefono = models.CharField(max_length=20)

    def clone(self):
        return self.__class__(
            id=self.id,
            nombre=self.nombre,
            apellido=self.apellido,
            edad=self.edad,
            cedula=self.cedula,
            telefono=self.telefono
        )

    def __str__(self):
        return f"Arbitro: {self.nombre} {self.apellido}"

class Presidente(Persona):
    nombre_equipo = models.CharField(max_length=100)

    def clone(self):
        return self.__class__(
            id=self.id,
            nombre=self.nombre,
            apellido=self.apellido,
            edad=self.edad,
            cedula=self.cedula,
            nombre_equipo=self.nombre_equipo
        )

    def __str__(self):
        return f"Presidente: {self.nombre} {self.apellido}"

class Jugador(Persona):
    dorsal = models.IntegerField()
    posicion = models.CharField(max_length=100)
    goles = models.IntegerField()

    def clone(self):
        return self.__class__(
            id=self.id,
            nombre=self.nombre,
            apellido=self.apellido,
            edad=self.edad,
            cedula=self.cedula,
            dorsal=self.dorsal,
            posicion=self.posicion,
            goles=self.goles
        )

    def __str__(self):
        return f"Jugador: {self.nombre} {self.apellido}"

class Vocalia(models.Model):
    amonestaciones = models.IntegerField()
    titulares_del_partido = models.CharField(max_length=255)
    jugadores_con_anotaciones = models.CharField(max_length=255)
    faltas = models.IntegerField()

    def clone(self):
        return self.__class__(
            amonestaciones=self.amonestaciones,
            titulares_del_partido=self.titulares_del_partido,
            jugadores_con_anotaciones=self.jugadores_con_anotaciones,
            faltas=self.faltas
        )

    def __str__(self):
        return f"Vocalia(Titulares: {self.titulares_del_partido}, Amonestaciones: {self.amonestaciones})"

class Partido(models.Model):
    estadio = models.CharField(max_length=100)
    equipo = models.CharField(max_length=100)
    fecha = models.DateField()
    arbitro = models.ForeignKey(Arbitro, on_delete=models.CASCADE)
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    presidente = models.ForeignKey(Presidente, on_delete=models.CASCADE)

    def clone(self):
        return self.__class__(
            estadio=self.estadio,
            equipo=self.equipo,
            fecha=self.fecha,
            arbitro=self.arbitro.clone(),  
            jugador=self.jugador.clone(), 
            presidente=self.presidente.clone() 
        )

    def __str__(self):
        return f"Partido: {self.equipo} vs {self.equipo} at {self.estadio} on {self.fecha}"

class Equipo(models.Model):
    nombre_equipo = models.CharField(max_length=100)
    cantidad_jugadores = models.IntegerField()
    logo = models.ImageField(upload_to='logos/')
    slogan = models.CharField(max_length=255)
    presidente = models.ForeignKey(Presidente, on_delete=models.CASCADE)
    capitan = models.ForeignKey(Jugador, on_delete=models.CASCADE)

    def clone(self):
        return self.__class__(
            nombre_equipo=self.nombre_equipo,
            cantidad_jugadores=self.cantidad_jugadores,
            logo=self.logo,
            slogan=self.slogan,
            presidente=self.presidente.clone(), 
            capitan=self.capitan.clone() 
        )

    def __str__(self):
        return f"Equipo: {self.nombre_equipo}"



# class Match(models.Model):
#     title = models.CharField(max_length=100)
#     date = models.DateField()
#     location = models.CharField(max_length=100)
#     description = models.TextField()

# class Result(models.Model):
#     match = models.ForeignKey(Match, on_delete=models.CASCADE)
#     winner = models.ForeignKey(User, on_delete=models.CASCADE)
#     score = models.CharField(max_length=50)

# class Player(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     position = models.CharField(max_length=50)
#     team = models.CharField(max_length=100)


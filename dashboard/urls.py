from django.urls import path
from .views import dashboard_view,presidente_view,ingresar_presidente,partido_view,ingresar_jugador,arbitro_view,equipo_view,ingresar_equipo,jugador_view, vocalias_view, ingresar_vocalia, ingresar_partidos

urlpatterns = [
    path('arbitro/', arbitro_view, name='arbitro'),
    path('equipos/', equipo_view, name='equipos'),
    path('ingresar_equipo/', ingresar_equipo, name='ingresar_equipo'),
    path('jugadores/', jugador_view, name='jugadores'),
    path('ingresar_jugador/', ingresar_jugador, name='ingresar_jugador'),
    path('partidos/', partido_view, name='partido'),
    path('ingresar_partidos/', ingresar_partidos, name='ingresar_partidos'),
    path('presidentes/', presidente_view, name='presidente'),
    path('ingresar_presidente/', ingresar_presidente, name='ingresar_presidente'),
    path('vocalias/', vocalias_view, name='vocalias'),
    path('ingresar_vocalia/', ingresar_vocalia, name='ingresar_vocalia'),
    path('', dashboard_view, name='dashboard'),
]

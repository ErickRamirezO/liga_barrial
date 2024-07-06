from django.urls import path
from .views import dashboard_view,presidente_view,partido_view,arbitro_view,equipo_view,jugador_view, vocalias_view, ingresar_vocalia

urlpatterns = [
    path('arbitro/', arbitro_view, name='arbitro'),
    path('equipos/', equipo_view, name='equipos'),
    path('jugadores/', jugador_view, name='jugador'),
    path('partidos/', partido_view, name='partido'),
    path('presidente/', presidente_view, name='presidente'),
    path('vocalias/', vocalias_view, name='vocalias'),
    path('ingresar_vocalia/', ingresar_vocalia, name='ingresar_vocalia'),
    path('', dashboard_view, name='dashboard'),
]

from django.urls import path
from .views import dashboard_view, vocalias_view, ingresar_vocalia

urlpatterns = [
    path('vocalias/', vocalias_view, name='vocalias'),
    path('ingresar_vocalia/', ingresar_vocalia, name='ingresar_vocalia'),
    path('', dashboard_view, name='dashboard'),
]

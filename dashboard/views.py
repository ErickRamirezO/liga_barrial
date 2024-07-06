from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .models import Equipo, Jugador, Arbitro, Partido, Presidente, Vocalia

def dashboard_view(request):
    dashboard = loader.get_template('dashboard.html')
    return HttpResponse(dashboard.render())

def equipo_view(request):
    equipos = Equipo.objects.all()
    return render(request, 'equipos.html', {'equipos': equipos})

def jugador_view(request):
    jugador = Jugador.objects.all()
    return render(request, 'jugadores.html', {'jugador': jugador})

def arbitro_view(request):
    arbitro = Arbitro.objects.all()
    return render(request, 'arbitro.html', {'arbitro': arbitro})

def partido_view(request):
    partido = Partido.objects.all()
    return render(request, 'partido.html', {'partido': partido})

def presidente_view(request):
    presidente = Presidente.objects.all()
    return render(request, 'presidente.html', {'presidente': presidente})

def vocalias_view(request):
    vocalias = Vocalia.objects.all()
    return render(request, 'vocalias.html', {'vocalias': vocalias})

def ingresar_vocalia(request):
    if request.method == 'POST':
        # Obtener datos del formulario
        amonestaciones = request.POST.get('amonestaciones')
        titulares = request.POST.get('titulares')
        anotaciones = request.POST.get('anotaciones')
        faltas = request.POST.get('faltas')

        # Guardar los datos en la base de datos
        nueva_vocalia = Vocalia(
            amonestaciones=amonestaciones,
            titulares_del_partido=titulares,
            jugadores_con_anotaciones=anotaciones,
            faltas=faltas
        )
        nueva_vocalia.save()

        # Redirigir a la página de vocalías o donde desees
        return redirect('vocalias')

    # Si no es POST, mostrar el formulario nuevamente
    return render(request, 'ingresar_vocalia.html')

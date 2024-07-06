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

def ingresar_equipo(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        numero_jugadores = request.POST.get('numero_jugadores')
        logo = request.FILES.get('logo')
        slogan = request.POST.get('slogan')
        presidente = request.POST.get('presidente')

        nuevo_equipo = Equipo(
            nombre=nombre,
            numero_jugadores=numero_jugadores,
            logo=logo,
            slogan=slogan,
            presidente=presidente
        )
        nuevo_equipo.save()

        return redirect('equipos')

    return render(request, 'ingresar_equipo.html')

def jugador_view(request):
    jugadores = Jugador.objects.all()
    return render(request, 'jugadores.html', {'jugadores': jugadores})

def ingresar_jugador(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        edad = request.POST.get('edad')
        cedula = request.POST.get('cedula')
        dorsal = request.POST.get('dorsal')
        posicion = request.POST.get('posicion')
        goles = request.POST.get('goles')

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

        return redirect('jugadores')

    return render(request, 'ingresar_jugador.html')

def arbitro_view(request):
    arbitros = Arbitro.objects.all()
    return render(request, 'arbitro.html', {'arbitros': arbitros})

def partido_view(request):
    partidos = Partido.objects.all()
    return render(request, 'partido.html', {'partidos': partidos})

def presidente_view(request):
    presidentes = Presidente.objects.all()
    return render(request, 'presidente.html', {'presidente': presidentes})

def ingresar_presidente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        edad = request.POST.get('edad')
        cedula = request.POST.get('cedula')

        nuevo_presidente = Presidente(
            nombre=nombre,
            apellido=apellido,
            edad=edad,
            cedula=cedula
        )
        nuevo_presidente.save()

        return redirect('presidente')

    return render(request, 'ingresar_presidente.html')

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

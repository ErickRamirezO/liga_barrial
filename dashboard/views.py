from django.shortcuts import render, redirect
from .models import Match, Result, Player, Vocalia

def dashboard_view(request):
    matches = Match.objects.all()
    results = Result.objects.all()
    players = Player.objects.all()
    return render(request, 'dashboard.html', {
        'matches': matches,
        'results': results,
        'players': players,
    })

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

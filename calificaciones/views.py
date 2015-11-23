from django.http import HttpResponse
from django.shortcuts import render

from models import Empresa, Alumno


def index(request):
    empresas = Empresa.objects.order_by('nombre')
    return render(request, 'calificaciones/index.html', {'empresas': empresas})


def ranking(request):
    ranking = dict()
    num_alumnos = dict()
    for alumno in Alumno.objects.all():
        if alumno.empresa in ranking:
            ranking[alumno.empresa] += alumno.puntuacion
            num_alumnos[alumno.empresa] += 1
        else:
            ranking[alumno.empresa] = alumno.puntuacion
            num_alumnos[alumno.empresa] = 1
    for empresa in ranking:
        ranking[empresa] /= num_alumnos[empresa]

    return render(request, 'calificaciones/ranking.html', {'ranking': ranking})


def calificaciones_empresa(request, empresa):
    calificaciones = dict()
    for alumno in Alumno.objects.all():
        if str(alumno.empresa) == empresa:
            calificaciones[str(alumno.nombre)] = str(alumno.puntuacion)

    return render(request, 'calificaciones/puntuaciones.html', {'puntuaciones': calificaciones, 'empresa': empresa})


def alumnos_empresa(request, empresa):
    alumnos = []
    for alumno in Alumno.objects.all():
        if str(alumno.empresa) == empresa:
            alumnos.append(alumno.nombre)


def empresa(request, empresa):
    if Empresa.objects.filter(nombre=empresa).exists():
        return render(request, 'calificaciones/empresa.html', {'empresa': empresa})
    else:
        return HttpResponse("La empresa solicitada no existe en el sistema.")

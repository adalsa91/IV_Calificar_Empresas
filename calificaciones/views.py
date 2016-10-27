# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

from .models import Empresa, Alumno


def index(request):
    """Vista de la página principal de la aplicación.

    En esta vista se muestra un listado de las empresas con enlace
    a sus puntuaciones y un enlace al ranking de empresas mejor puntuadas.

    Args:
    request: petición http.

    Returns:
    Return an HttpResponse con el html renderizado.

    """
    empresas = Empresa.objects.order_by('nombre')
    return render(request, 'calificaciones/index.html', {'empresas': empresas})


def ranking(request):
    """Vista del ranking de empresas mejor valoradas.

    Devuelve un listado con las puntuaciones media de cada empresa
    ordenado de mayor a menor.

    Args:
    request: petición http.

    Returns:
    Devuelve un objeto HttpResponse con el html renderizado.
    """
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
    """Vista del listado de puntuaciones de una empresa.

    En esta vista se muestra un listado con todas las puntuaciones de una
    determinada empresa.

    Args:
    request: petición http.
    empresa: nombre de la empresa.

    Returns:
    Devuelve un objeto HttResponse con el html renderizado.
    """
    calificaciones = dict()
    for alumno in Alumno.objects.all():
        if str(alumno.empresa) == empresa:
            calificaciones[str(alumno.nombre)] = str(alumno.puntuacion)

    return render(request, 'calificaciones/puntuaciones.html',
                  {'puntuaciones': calificaciones, 'empresa': empresa})


def alumnos_empresa(request, empresa):
    """Elabora un listado de alumnos que han votado una determinada empresa.

    Devuelve una lista de alumnos que han puntuado a la empresa pasada como
    argumento.

    Args:
    request: petición http.
    empresa: nombre de la empresa.

    Returns:
    Devuelve un objeto HttResponse con el html renderizado.
    """
    alumnos = []
    for alumno in Alumno.objects.all():
        if str(alumno.empresa) == empresa:
            alumnos.append(alumno.nombre)


def empresa(request, empresa):
    """Vista con datos de la empresa y enlace a calificaciones.

    En esta vista se muestra información general de la empresa y un enlace
    a la lista de calificaciones.

    Args:
    request: petición http.
    empresa: nombre de la empresa.

    Returns:
    Devuelve un objeto HttResponse con el html renderizado.
    """
    if Empresa.objects.filter(nombre=empresa).exists():
        return render(request, 'calificaciones/empresa.html',
                      {'empresa': empresa})
    else:
        return HttpResponse("La empresa solicitada no existe en el sistema.")

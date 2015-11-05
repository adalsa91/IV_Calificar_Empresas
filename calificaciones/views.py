from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from models import Empresa,Alumno


# Create your views here.

def index(request):
#    lista_empresas = Empresa.objects.order_by('nombre')
#    output = ', '.join([p.nombre for p in lista_empresas ])
#    return HttpResponse(output)
    empresas = Empresa.objects.all()
    template = loader.get_template('calificaciones/index.html')
    context = RequestContext(request, {'empresas': empresas})
    return HttpResponse(template.render(context))

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

    template = loader.get_template("calificaciones/ranking.html")
    context = RequestContext(request, {"ranking": ranking})

    return HttpResponse(template.render(context))

def calificaciones_empresa(request, empresa):
    calificaciones=[]
    for alumno in Alumno.objects.all():
        if str(alumno.empresa) == empresa:
            calificaciones.append(alumno.puntuacion)

    return HttpResponse(calificaciones)

def alumnos_empresa(request, empresa):
    alumnos = []
    for alumno in Alumno.objects.all():
        if str(alumno.empresa) == empresa:
            alumnos.append(alumno.nombre)

def empresa(request, empresa):
    if Empresa.objects.filter(nombre=empresa).exists():
        template = loader.get_template("calificaciones/empresa.html")
        context = RequestContext(request, {"empresa": empresa})
        return HttpResponse(template.render(context))
    else:
        return HttpResponse("La empresa solicitada no existe en el sistema.")

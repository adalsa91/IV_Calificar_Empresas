# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class Empresa(models.Model):
    """Modelo para representar una empresa

    Almacena el nombre de la empresa.
    """
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Alumno(models.Model):
    """Modelo para representar un alumno.

    Almacena los datos del alumno y la puntuación realizada.

    """
    nombre = models.CharField(max_length=200)
    empresa = models.ForeignKey(Empresa)
    puntuacion = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.nombre

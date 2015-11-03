from django.db import models

# Create your models here.
class Empresa(models.Model):
	nombre = models.CharField(max_length=200)

class Alumno(models.Model):
	nombre = models.CharField(max_length=200)
	empresa = models.ForeignKey(Empresa)
	puntuacion = models.DecimalField(max_digits=3, decimal_places=1)

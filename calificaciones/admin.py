from django.contrib import admin
from .models import Empresa, Alumno
# Register your models here.
class AlumnoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'empresa', 'puntuacion')

admin.site.register(Empresa)
admin.site.register(Alumno, AlumnoAdmin)


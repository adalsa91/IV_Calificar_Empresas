# IV-Calificar Empresas
Página web para calificar las empresas en las que hacen prácticas los alumnos. Creada como parte de los ejercicios del Tema 2 de la asignatura Infraestructura Virtual.

#Entorno
    Python 2.7.6
    Django 1.8.5

#Modelos
    Empresa
        └nombre
    Alumno
        ├nombre
        ├empresa
        └puntuacion

#Mapa web
    /admin
    /calificaciones
        /ranking
        /<empresa>
            /calificaciones

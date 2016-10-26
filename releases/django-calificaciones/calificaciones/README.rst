=====
Calificaciones
=====

Calificaciones es una aplicación que permite gestionar las valoraciones de los alumnos sobre las prácticas en las que han realizado las prácticas.

Quick start
-----------

1. Añade "calificaciones" en INSTALLED_APPS ::

    INSTALLED_APPS = [
        ...
        'calificaciones',
    ]

2. Incluye el URLconf de calificaciones en el archivo urls.py de tu proyecto::

     url(r'^calificaciones/', include('calificacio.urls')),

3. Ejecuta `python manage.py migrate` para crear los mdoelos de calificaciones.

4. Inicia el servidor de desarrollo y entra en http://127.0.0.1:8000/admin/
   para añadir empresas y puntuaciones (necesitas tener la app de Admin activada).

5. Visita http://127.0.0.1:8000/calificaciones/ para ver las calificaciones.

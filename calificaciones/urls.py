from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ranking$', views.ranking, name='ranking'),
    url(r'^(?P<empresa>[\w]+)/$', views.empresa, name='calificaciones'),
    url(r'^(?P<empresa>[\w]+)/calificaciones/$', views.calificaciones_empresa, name='calificaciones'),
]

from django.urls import include, path
from . import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('peliculas', views.PeliculasList)
router.register('categorias', views.CategoriasList)
router.register('personajes', views.PersonajesList)
router.register('elencos', views.ElencosList)
router.register('personas', views.PersonasList)
router.register('tipos_personas', views.TipospersonasList)

urlpatterns = [
    path('peliculas/', include(router.urls)),
]
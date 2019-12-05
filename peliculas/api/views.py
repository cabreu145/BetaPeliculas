from django.shortcuts import render
from rest_framework import viewsets
from portfolio.models import *
from .serializers import *


class PeliculasList(viewsets.ModelViewSet):
    queryset = Peliculas.objects.all()
    serializer_class = PeliculasSerializer

class CategoriasList(viewsets.ModelViewSet):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer

class PersonajesList(viewsets.ModelViewSet):
    queryset = Personajes.objects.all()
    serializer_class = PersonajesSerializer

class ElencosList(viewsets.ModelViewSet):
    queryset = Elenco.objects.all()
    serializer_class = ElencoSerializer

class PersonasList(viewsets.ModelViewSet):
    queryset = Personas.objects.all()
    serializer_class = PersonasSerializer

class TipospersonasList(viewsets.ModelViewSet):
    queryset = Tipospersonas.objects.all()
    serializer_class = TipospersonasSerializer
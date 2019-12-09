from django.shortcuts import render, HttpResponse, get_object_or_404
from portfolio.models import *

def home(request):
    peliculas = Peliculas.objects.all()
    params = {
        'peliculas': peliculas
    }
    return render(request, "core/index.html", params)

def pelicula(request, pk, template_name='core/peli.html'):
    pelicula = get_object_or_404(Peliculas, pk=pk)
    return render(request, template_name, {'object':pelicula})    



# Create your views here.

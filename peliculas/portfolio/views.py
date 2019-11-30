from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.contrib.auth.models import User, Permission
# Create your views here.



def administrador(request):
    return render(request, "portfolio/administrador.html")

def adminusuario(request):
    usuarios = User.objects.all()
    return render(request, "portfolio/baseformularios.html",{'usuarios':usuarios})

def adminpermiso(request):
    return render(request, "portfolio/permiso.html")

def admincalificacion(request):
    calificaciones = Calificaciones.objects.all()
    
    return render(request, "portfolio/calificacion.html",{'calificaciones':calificaciones})

def admincategoria(request):
    categorias = Categorias.objects.all()
    return render(request, "portfolio/categoria.html",{'categorias':categorias})

def adminpersonas(request):

    return render(request, "portfolio/personas.html")

def adminpelicula(request):
    peliculas = Peliculas.objects.all()
    return render(request, "portfolio/adminpeliculas.html",{'peliculas':peliculas})

def adminpeliculanew(request):
    return render(request, "portfolio/newpelicula.html")
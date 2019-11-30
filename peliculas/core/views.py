from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, "core/index.html")

def pelicula(request):
    return render(request, "core/peli.html")




# Create your views here.

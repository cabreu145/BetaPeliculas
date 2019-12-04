from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import (    
    login_required,
    permission_required
)
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from .forms import NewUserForm, FormNota
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import ListView, DetailView, View 
from django.views.generic.edit import (CreateView, UpdateView, DeleteView, )
from django.views import View
from django.urls import reverse_lazy

from django.core.paginator import Paginator
# Create your views here.



def administrador(request):
    return render(request, "portfolio/administrador.html")

def adminusuario(request):
    usuarios = User.objects.all()
    return render(request, "portfolio/baseformularios.html",{'usuarios':usuarios})

def adminusuarioeditar(request):

    return render(request, "portfolio/editar.base.html")

def adminusuarioeliminar(request):

    return render(request, "portfolio/eliminar.base.html")

def adminusuarionuevo(request):
    next = request.GET.get('next')
    form = NewUserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }


    return render(request, "portfolio/nuevo.base.html", context)

def adminpermiso(request):
    return render(request, "portfolio/permiso.html")

def admincalificacion(request):
    calificaciones_List = Calificaciones.objects.all()
    paginator = Paginator(calificaciones_List,5)

    page = request.GET.get('page')
    calificaciones = paginator.get_page(page)
    
    return render(request, "portfolio/calificacion.html",{'calificaciones':calificaciones})

def admincategoria(request):
    categorias = Categorias.objects.all()
    return render(request, "portfolio/categoria.html",{'categorias':categorias})

def adminpersonas(request):

    return render(request, "portfolio/personas.html")

def adminpelicula(request):
    peliculas = Peliculas.objects.all()
    return render(request, "portfolio/adminpeliculas.html",{'peliculas':peliculas})


    
   

class adminpeliculanew(CreateView):
    model = Peliculas
    form_class = FormNota
    success_url = reverse_lazy('admin_pelicula')

def crud(request):
    
    
    if request.method == 'POST':
        form = FormNota(request.POST)

        if form.is_valid():
            form.save()
            return redirect('admin_pelicula')
    else:
        form = FormNota()

    context ={'form' : form}
    return render(request, 'portfolio/peliculas_form.html', context)

    

def logout_def(request):
    if request.method == "POST":
        logout(request)
    
    return redirect("home")

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Benvenido {username}")
                return redirect('/')
            else:
                messages.error(request, "Usuario o Contraseña invalida")
        else:
            messages.error(request, "Usuario o Contraseña invalida")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "signup.html",
                    context={"form":form})
    
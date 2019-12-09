from django.shortcuts import render, redirect, get_object_or_404
from models import *
from django.db.models import Q
from django.contrib.auth.models import User, Permission, Group
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
from .forms import *
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View
from django.urls import reverse_lazy

from django.core.paginator import Paginator
from django.urls import reverse
# Create your views here.



def administrador(request):
    return render(request, "portfolio/administrador.html")


##########################USUARIO/PERMISOS######################################################################################

def adminusuario(request):
    usuarios = User.objects.all()
    return render(request, "portfolio/baseformularios.html",{'usuarios':usuarios})

class adminusuarioeditar(UpdateView):
    template_name = 'portfolio/UpdateUser.html'
    form_class = NewUserForm

    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(User, id=id_)

    
    
    def get_success_url(self):
        return reverse_lazy('admin_usuario')



class adminusuarioeliminar(DeleteView):
    template_name = 'portfolio/eliminar.base.html' 
    model = User
    form_class = NewUserForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(User, id=id_)
    
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Usuario Eliminada Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('admin_usuario') # Redireccionamos a la vista principal 'leer'
    

    

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

##########################CALIFIACIONES######################################################################################
def admincalificacion(request):
    calificaciones_List = Calificaciones.objects.all()
    paginator = Paginator(calificaciones_List,5)

    page = request.GET.get('page')
    calificaciones = paginator.get_page(page)
    
    return render(request, "portfolio/calificacion.html",{'calificaciones':calificaciones})

class calificacionnew(CreateView):
    model = Calificaciones
    form_class = FormCali
    success_url = reverse_lazy('calificacionnew')
def crudc(request):
        if request.method == 'POST':
            form = FormCali(request.POST)

        

        if form.is_valid():

            form.save()

            return redirect('calificacionnew')

        else:
            form = FormCali()
        


        

            context ={'form' : form}
        return render(request, 'portfolio/calificacionesform.html', context)


class calificacionEdit(UpdateView):
    template_name = 'portfolio/UpdateCali.html'
    model = Calificaciones
    form_class = FormCali

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Calificaciones, idcalificaciones=id_)

    
    
    def get_success_url(self):
        return reverse_lazy('admin_calif')


class calificacionliminar(DeleteView):
    template_name = 'portfolio/eliminarCali.html'
    model = Calificaciones
    form_class = FormCali

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Calificaciones, idcalificaciones=id_)
    
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Usuario Eliminada Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('admin_calif') # Redireccionamos a la vista principal 'leer'




    

    
##########################CATEGORIAS######################################################################################


def admincategoria(request):
    categorias_List = Categorias.objects.all()
    paginator = Paginator(categorias_List,5)

    page = request.GET.get('page')
    categorias = paginator.get_page(page)
    return render(request, "portfolio/categoria.html",{'categorias':categorias})

class categorianew(CreateView):
    model = Categorias
    form_class = FormCat
    success_url = reverse_lazy('catnew')


def crudcat(request):

        if request.method == 'POST':
            form = FormCat(request.POST)

        

        if form.is_valid():

            form.save()

            return redirect('catnew')

        else:
            form = FormCat()
        


        

            context ={'form' : form}
        return render(request, 'portfolio/categoria.html', context)


class categoriaedit(UpdateView):
    template_name = 'portfolio/UpdateCat.html'
    model = Categorias
    form_class = FormCat

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Categorias, idcategoria=id_)

    def get_success_url(self):
        return reverse_lazy('admin_cat')




class categorialiminar(DeleteView):

    template_name = 'portfolio/eliminarCat.html'
    model = Categorias
    form_class = FormCat

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Categorias, idcategoria=id_)
    
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Usuario Eliminada Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('admin_cat') # Redireccionamos a la vista principal 'leer' """

##########################PERSONAS######################################################################################
def adminpersonas(request):
    personas_List = Personas.objects.all()
    paginator = Paginator(personas_List,5)

    page = request.GET.get('page')
    personas = paginator.get_page(page)
    return render(request, "portfolio/personas.html",{'personas':personas})
    

class adminpersonasnew(CreateView):
    model = Personas
    form_class = Formper
    success_url = reverse_lazy('admin_persona')

def crudpersonas(request):
    
    
    if request.method == 'POST':
        form = Formper(request.POST)

        if form.is_valid():
            form.save()
            return redirect('admin_persona')
    else:
        form = Formper()

    context ={'form' : form}
    return render(request, 'portfolio/personas_form.html', context)


class personasedit(UpdateView):
    template_name = 'portfolio/Updatepersona.html'
    model = Personas
    form_class = Formper

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Personas, idpersona=id_)

    def get_success_url(self):
        return reverse_lazy('admin_persona')



class personasiminar(DeleteView): 

    template_name = 'portfolio/eliminarPerso.html'
    model = Personas
    form_class = Formper


    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Personas, idpersona=id_)
    
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Persona Eliminada Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('admin_pelicula') # Redireccionamos a la vista principal 'leer' """

    
##########################PELICULA######################################################################################
def adminpelicula(request):
    peliculas_List = Peliculas.objects.all()
    paginator = Paginator(peliculas_List,5)

    page = request.GET.get('page')
    peliculas = paginator.get_page(page)
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


class peliculaedit(UpdateView):
    template_name = 'portfolio/Updatepeli.html'
    model = Peliculas
    form_class = FormNota

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Peliculas, idpeliculas=id_)

    def get_success_url(self):
        return reverse_lazy('admin_pelicula')



class peliculaliminar(DeleteView):

    template_name = 'portfolio/eliminarPeli.html'
    model = Peliculas
    form_class = FormNota


    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Peliculas, idpeliculas=id_)
    
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Usuario Eliminada Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('admin_pelicula') # Redireccionamos a la vista principal 'leer' """


##########################PERSONAJES######################################################################################
def adminpersonaje(request):

    personaje_List = Personajes.objects.all()
    paginator = Paginator(personaje_List ,5)

    page = request.GET.get('page')
    personajes = paginator.get_page(page)
    
    return render(request, "portfolio/permiso.html",{'personajes':personajes})


    
   

class personajenew(CreateView):

    model = Personajes
    form_class = Formpersonaje
    success_url = reverse_lazy('admin_permisos')

def crudpersonaje(request):
    
    
    if request.method == 'POST':
        form = FormNota(request.POST)

        if form.is_valid():
            form.save()
            return redirect('admin_permisos')
    else:
        form = FormNota()

    context ={'form' : form}
    return render(request, 'portfolio/personajes_form.html', context)


class personajeedit(UpdateView):
    template_name = 'portfolio/Updatepersonaje.html'
    model = Personajes
    form_class = Formpersonaje

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Personajes, idpersonajes=id_)

    def get_success_url(self):
        return reverse_lazy('admin_permisos')



class eliminarpersonaje(DeleteView):

    template_name = 'portfolio/eliminarPersonajes.html'
    model = Personajes
    form_class = Formpersonaje


    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Personajes, idpersonajes=id_)

    
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Usuario Eliminada Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('admin_permisos') # Redireccionamos a la vista principal 'leer'
##########################CAST######################################################################################
def admin_cast(request):

    cast_List = Elenco.objects.all()
    paginator = Paginator(cast_List ,5)

    page = request.GET.get('page')
    casts = paginator.get_page(page)
    
    return render(request, "portfolio/cast.html",{'casts':casts})


    


class castnew(CreateView):

    model = Elenco
    form_class = Formelenco
    success_url = reverse_lazy('admin_cast')

def crudcast(request):
    
    
    if request.method == 'POST':
        form = Formelenco(request.POST)

        if form.is_valid():
            form.save()
            return redirect('admin_cast')
    else:
        form = Formelenco()

    context ={'form' : form}
    return render(request, 'portfolio/cast_form.html', context)


class castedit(UpdateView):
    template_name = 'portfolio/Updateelenco.html'
    model = Elenco
    form_class = Formelenco

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Elenco, idelenco=id_)

    def get_success_url(self):
        return reverse_lazy('admin_cast')



class eliminarcast(DeleteView):

    template_name = 'portfolio/eliminarCast.html'
    model = Elenco
    form_class = Formelenco


    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Elenco, idelenco=id_)

    
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Usuario Eliminada Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('admin_cast') # Redireccionamos a la vista principal 'leer'''








##########################LOG/OUT######################################################################################
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
    
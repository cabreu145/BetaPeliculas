from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.db.models import Q
from django.contrib.auth.models import User, Permission, Group
from django.contrib.auth.decorators import (    
    login_required,
    permission_required
)
from django.contrib.auth import authenticate

from django.contrib.auth import (
    authenticate,
    get_user_model,

)
from .forms import *
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View
from django.urls import reverse_lazy

from django.core.paginator import Paginator
from django.urls import reverse

from django.contrib.auth.decorators import (    
    login_required,
    
)
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout

# Create your views here.




def administrador(request):
    if not request.user.is_authenticated:
        return redirect("admin1")
    return render(request, "portfolio/administrador.html")


##########################USUARIO/PERMISOS######################################################################################

def adminusuario(request):
    if not request.user.is_authenticated:
        return redirect("admin1")

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
    if not request.user.is_authenticated:
        return redirect("admin1")

    next = request.GET.get('next')
    form = NewUserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        do_login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }


    return render(request, "portfolio/nuevo.base.html", context)

##########################CALIFIACIONES######################################################################################

def admincalificacion(request):
    if not request.user.is_authenticated:
        return redirect("admin1")
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
    if not request.user.is_authenticated:
        return redirect("admin1")
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
    if not request.user.is_authenticated:
        return redirect("admin1")
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
    if not request.user.is_authenticated:
        return redirect("admin1")
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
    if not request.user.is_authenticated:
        return redirect("admin1")

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
    if not request.user.is_authenticated:
        return redirect("admin1")

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
def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')


    if request.user.is_authenticated:
        return redirect("admin")

      
def login(request):
    if  request.user.is_authenticated:
        return redirect("admin")
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('admin')

    # Si llegamos al final renderizamos el formulario
    return render(request, "portfolio/login.html", {'form': form})
    
    

    

    
    
from django import forms
from django.forms import (ModelForm, TextInput, DateInput)
from .models import *
from django import forms
from django.contrib.auth.forms import ( UserCreationForm, AuthenticationForm,)
from django.contrib.auth.models import User

class LoginForm (AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("first_name","last_name","username","password1","password2","email", "is_superuser", "is_staff")
        labels = {
            
            'is_superuser': ('Administrador'),
            'is_staff"': ('Editor'),
        }


        #fields = ("first_name","last_name","username","password1","password2","email", "is_superuser", "is_staff")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class FormNota(forms.ModelForm): #Primer formulario contiene todos los fields del model con exeption de fecha 
    class Meta:
        model = Peliculas
        fields = [ 
            'idpeliculas',
            'fecha',
            'titulo' ,
            'Categoria_idCategoria',
            'calificaciones_idcalificaciones',
            'Personas_idPersonas',
            'cast',
            'descripcion',
            'tags',
            'duracion',
            'img',
            'logo',
            'banner'
        ]

class FormCali(forms.ModelForm):
    class Meta:
        model = Calificaciones
        fields = ['calificacion','estatus',]
        exclude = ['idcalificaciones','creado', 'actualizado']

class FormCat(forms.ModelForm):
    class Meta:
        model = Categorias
        fields = ['categoria', 'estatus']
        exclude = ['idcategoria','creado', 'actualizado']

class Formper(forms.ModelForm):
    class Meta:
        model = Personas
        fields = ['persona', 'tipospersonas_idTiposPersonas','estatus',]
        exclude = ['idpersona','creado', 'actualizado','img']

class Formpersonaje(forms.ModelForm):
    class Meta:
        model = Personajes
        fields = ['personaje','estatus',]
        exclude = ['idpersonajes','creado', 'actualizado']

class Formelenco(forms.ModelForm):
    class Meta:
        model = Elenco
        fields = ['personas_idpersonas', 'personajes_idpersonajes', 'img']
        exclude = ['idelenco','creado', 'actualizado']

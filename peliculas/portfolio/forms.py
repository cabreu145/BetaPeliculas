from django import forms
from django.forms import (ModelForm, TextInput)
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
        fields = ("username", "email", "password1", "password2")

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
            'descripcion',
            'tags',
            
        ]

   
       
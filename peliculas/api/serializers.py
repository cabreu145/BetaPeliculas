from portfolio.models import *
from rest_framework import serializers

class PeliculasSerializer(serializers.ModelSerializer):
    categoria = serializers.CharField(source='Categoria_idCategoria.categoria')
    class Meta:
        model = Peliculas
        fields = ('idpeliculas','titulo','fecha','categoria','descripcion', 'cast')

class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = ('idcategoria','categoria')

class PersonajesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personajes
        fields = ('idpersonajes','personaje')

class ElencoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elenco
        fields = ('idelenco','personas_idpersonas','personajes_idpersonajes')

class PersonasSerializer(serializers.ModelSerializer):
    tipo_persona = serializers.CharField(source='tipospersonas_idTiposPersonas.tipo_persona')
    class Meta:
        model = Personas
        fields = ('idpersona','persona','tipo_persona')
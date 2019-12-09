from portfolio.models import *
from rest_framework import serializers

class PeliculasSerializer(serializers.ModelSerializer):
    Categoria_idCategoria = serializers.StringRelatedField()
    calificaciones_idcalificaciones = serializers.StringRelatedField()
    cast = serializers.StringRelatedField(many=True)
    class Meta:
        model = Peliculas
        fields = (
            'idpeliculas',
            'titulo',
            'fecha',
            'Categoria_idCategoria',
            'descripcion', 
            'cast',
            'calificaciones_idcalificaciones'
            )

class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = (
            'idcategoria',
            'categoria',
            'estatus'
            )

class PersonajesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personajes
        fields = (
            'idpersonajes',
            'personaje'
            )

class ElencoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elenco
        fields = (
            'idelenco',
            'personas_idpersonas',
            'personajes_idpersonajes'
            )

class PersonasSerializer(serializers.ModelSerializer):
    #tipo_persona = serializers.CharField(source='tipospersonas_idTiposPersonas.tipo_persona')
    class Meta:
        model = Personas
        fields = (
            'idpersona',
            'persona',
            'tipospersonas_idTiposPersonas',
            'estatus'
            )

class TipospersonasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipospersonas
        fields = (
            'idtipospersonas',
            'tipo_persona',
            'estatus'
            )
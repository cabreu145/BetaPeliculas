from django.contrib import admin

# Register your models here.
    

from .models import *

# Register your models here.

#Acceder a bases de datos alternas#################################################################
class MultiDBModelAdmin(admin.ModelAdmin):
    readonly_fields =('creado', 'actualizado')
    using = ''

    def save_model(self, request, obj, form, change):
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        obj.delete(using=self.using)

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)
###################################################################################################

#Formatos de Display###############################################################################
class CalificacionesDisplay(MultiDBModelAdmin):
    readonly_fields =('creado', 'actualizado')

    def calificacion(self, obj):
        return obj.calificacion
    

    list_display = ['calificacion']
    calificacion.short_description = 'Calificacion'
    

    admin.site.site_header = "Calificaciones"
    admin.site.site_title = "Calificaciones"
class CategoriasDisplay(MultiDBModelAdmin):
    readonly_fields =('creado', 'actualizado')


    def categoria(self, obj):
        return obj.categoria
    

    list_display = ['categoria']
    categoria.short_description = 'Categoria'
    

    admin.site.site_header = "Categorias"
    admin.site.site_title = "Categorias"
class TipospersonaDisplay(MultiDBModelAdmin):
    readonly_fields =('creado', 'actualizado')
    def tipo_persona(self, obj):
        return obj.tipo_persona

    list_display = ['tipo_persona',]
    tipo_persona.short_description = 'Tipo de Personas'  

    admin.site.site_header = "Tipos de Personas"
    admin.site.site_title = "Tipos de Personas"
class PersonasDisplay(MultiDBModelAdmin):
    readonly_fields =('creado', 'actualizado')
    def persona(self, obj):
        return obj.persona
    def tipo_persona(self, obj):
        return obj.tipospersonas_idTiposPersonas.tipo_persona

    list_display = ['persona', 'tipo_persona',]
    persona.short_description = 'Persona'
    tipo_persona.short_description = 'Tipo de Persona'

    admin.site.site_header = "Personas"
    admin.site.site_title = "Personas"

class PeliculasDisplay(MultiDBModelAdmin):
    readonly_fields =('creado', 'actualizado')

    def titulo(self, obj):
        return obj.titulo
    def fecha(self, obj):
        return obj.fecha
    def categoria(self, obj):
        return obj.Categoria_idCategoria
    def calificacion(self, obj):
        return obj.calificaciones_idcalificaciones
    


    
    list_display = ['titulo','fecha', 'categoria', 'calificacion',]
    #list_filter = ('pagina', 'calificacion')
    titulo.short_description = 'Titulo'
    fecha.short_description = 'Fecha Estreno'
    categoria.short_description = 'Categoria'
    calificacion.short_description = 'Calificacion'

    admin.site.site_header = "Peliculas"
    admin.site.site_title = "Pelicuas"


class PersonajesDisplay(MultiDBModelAdmin):

    readonly_fields =('creado', 'actualizado')

    

    def personaje(self, obj):
        return obj.personaje

    def estatus(self, obj):
        return obj.estatus
        
    

    list_display = ['personaje', 'estatus']
    personaje.short_description = 'Personaje'
    

    admin.site.site_header = "Personaje"
    admin.site.site_title = "Personaje"

class ElencoDisplay(MultiDBModelAdmin):
    readonly_fields =('creado', 'actualizado')

    def persona(self, obj):
        return obj.personas_idpersonas

    def personaje(self, obj):
        return obj.personajes_idpersonajes
        
    

    list_display = ['persona', 'personaje']
    persona.short_description = 'Persona'
    personaje.short_description = 'Personaje'
    

    admin.site.site_header = "Elenco"
    admin.site.site_title = "Elenco"


###################################################################################################

#Registers#########################################################################################
admin.site.register(Calificaciones, CalificacionesDisplay)
admin.site.register(Categorias, CategoriasDisplay)
admin.site.register(Tipospersonas, TipospersonaDisplay)
admin.site.register(Personas, PersonasDisplay)
admin.site.register(Peliculas, PeliculasDisplay)
admin.site.register(Personajes, PersonajesDisplay)
admin.site.register(Elenco, ElencoDisplay)
###################################################################################################
from django.db import models
from django.utils.timezone import now



""" class Pelicula(models.Model):
    titulo=models.CharField(max_length=45)
    descripcion=models.TextField()
    categoria=models.TextField()
    actores=models.TextField()
    director=models.TextField()
    calificacion=models.TextField()
    debut=models.TimeField()
    creado=models.TimeField(auto_now_add=True)
    actualizado=models.TimeField(auto_now=True)
    
    class meta:
        verbosa_name = "pelicula"
        verbosa_name_plural ="peliculas"
        ordering ={"-creado"}
    
    def __str__(self):
        return self.titulo """

# Create your models here.

class Tipospersonas(models.Model):
    idtipospersonas = models.AutoField(db_column='idTiposPersonas', primary_key=True)  # Field name made lowercase.
    tipo_persona = models.CharField(max_length=45, blank=True, null=True)
    estatus = models.BooleanField()
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    
    

    class Meta:
        
        db_table = 'tipospersonas'
        verbose_name = "Tipo de Persona"
        verbose_name_plural = "Tipos de Personas"
    
    def __str__(self):
        return self.tipo_persona


class Personas(models.Model):
    idpersona = models.AutoField(db_column='idPersonas', primary_key=True)  # Field name made lowercase.
    persona = models.CharField(max_length=45, blank=True, null=True)
    tipospersonas_idTiposPersonas = models.ForeignKey('Tipospersonas', models.DO_NOTHING, db_column='TiposPersonas_idTiposPersonas')  # Field name made lowercase.
    estatus = models.BooleanField()
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    img = models.CharField(max_length=256,null=True)

    class Meta:
        
        db_table = 'Personas'
        unique_together = (('idpersona', 'tipospersonas_idTiposPersonas'),)
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

    def __str__(self):
        return self.persona

class Categorias(models.Model):
    idcategoria = models.AutoField(db_column='idCategoria', primary_key=True)  # Field name made lowercase.
    categoria = models.CharField(max_length=45, blank=True, null=True)
    estatus = models.BooleanField()
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    

    class Meta:
        
        db_table = 'categorias'
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.categoria


class Calificaciones(models.Model):
    idcalificaciones = models.AutoField(db_column='idCalificaciones', primary_key=True)  # Field name made lowercase.
    calificacion = models.CharField(max_length=45, blank=True, null=True)
    estatus = models.BooleanField()
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    

    class Meta:
        
        db_table = 'calificaciones'
        verbose_name = "Calificacion"
        verbose_name_plural = "Calificaciones"

    def __str__(self):
        return self.calificacion

class Elenco(models.Model):
    idelenco = models.AutoField(db_column='idelenco', primary_key=True)
    personas_idpersonas = models.ForeignKey('Personas', models.DO_NOTHING, db_column='Personas_idPersonas')  # Field name made lowercase.
    personajes_idpersonajes = models.ForeignKey('Personajes', models.DO_NOTHING, db_column='personajes_idpersonajes')
    img = models.CharField(max_length=256,null=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        
        db_table = 'elenco'
        unique_together = (('personas_idpersonas', 'personajes_idpersonajes'),)
    def __str__(self):
        return self.personas_idpersonas.persona + ' - ' + self.personajes_idpersonajes.personaje


class Personajes(models.Model):
    idpersonajes = models.AutoField(db_column='idpersonajes', primary_key=True)
    personaje = models.CharField(max_length=45, blank=True, null=True)
    estatus = models.BooleanField()
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        
        db_table = 'personajes' 
    def __str__(self):
        return self.personaje

class Peliculas(models.Model):
    idpeliculas = models.AutoField(db_column='idPeliculas', primary_key=True)  # Field name made lowercase.
    titulo = models.CharField(max_length=45, db_column='titulo')
    fecha = models.DateField(db_column='FechaEstreno', blank=True, null=True)  # Field name made lowercase.
    Categoria_idCategoria = models.ForeignKey(Categorias, models.DO_NOTHING, db_column='Categoria_idCategoria',verbose_name='Categoría')  # Field name made lowercase.
    calificaciones_idcalificaciones = models.ForeignKey(Calificaciones, models.DO_NOTHING, db_column='Calificaciones_idCalificaciones',verbose_name='Calificaciones')  # Field name made lowercase.
    descripcion = models.TextField(blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    tags = models.TextField(blank=True, null=True)
    duracion = models.IntegerField(default=0)
    cast = models.ManyToManyField(Elenco)
    img = models.CharField(max_length=256,null=True)
    banner = models.CharField(max_length=256,null=True)
    logo = models.CharField(max_length=256,null=True)
    Personas_idPersonas = models.ForeignKey(Personas, models.DO_NOTHING,verbose_name='Director',null=True) 


    class Meta:
        
        db_table = 'peliculas'
        unique_together = (('idpeliculas', 'Categoria_idCategoria', 'calificaciones_idcalificaciones', 'Personas_idPersonas', ),)
        verbose_name = "Pelicula"
        verbose_name_plural = "Peliculas"

    def __unicode__(self):
        return self.titulo
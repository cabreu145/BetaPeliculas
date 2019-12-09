# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Calificaciones(models.Model):
    idcalificaciones = models.AutoField(db_column='idCalificaciones', primary_key=True)  # Field name made lowercase.
    calificacion = models.CharField(max_length=45, blank=True, null=True)
    prioridad = models.IntegerField()
    estatus = models.IntegerField()
    estado = models.IntegerField(blank=True, null=True)
    creado = models.DateTimeField(blank=True, null=True)
    actualizado = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calificaciones'


class Categorias(models.Model):
    idcategoria = models.AutoField(db_column='idCategoria', primary_key=True)  # Field name made lowercase.
    categoria = models.CharField(max_length=45, blank=True, null=True)
    prioridad = models.IntegerField()
    estatus = models.IntegerField()
    creado = models.DateTimeField(blank=True, null=True)
    actualizado = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categorias'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Elenco(models.Model):
    peliculas_idpeliculas = models.ForeignKey('Peliculas', models.DO_NOTHING, db_column='peliculas_idPeliculas', primary_key=True)  # Field name made lowercase.
    personas_idpersonas = models.ForeignKey('Personas', models.DO_NOTHING, db_column='Personas_idPersonas')  # Field name made lowercase.
    personajes_idpersonajes = models.ForeignKey('Personajes', models.DO_NOTHING, db_column='personajes_idpersonajes')

    class Meta:
        managed = False
        db_table = 'elenco'
        unique_together = (('peliculas_idpeliculas', 'personas_idpersonas', 'personajes_idpersonajes'),)


class Peliculas(models.Model):
    idpeliculas = models.AutoField(db_column='idPeliculas', primary_key=True)  # Field name made lowercase.
    fechaestreno = models.DateField(db_column='FechaEstreno')  # Field name made lowercase.
    prioridad = models.IntegerField()
    descripcion = models.TextField()
    calificaciones_idcalificaciones = models.ForeignKey(Calificaciones, models.DO_NOTHING, db_column='Calificaciones_idCalificaciones')  # Field name made lowercase.
    categoria_idcategoria = models.ForeignKey(Categorias, models.DO_NOTHING, db_column='Categoria_idCategoria')  # Field name made lowercase.
    personas_idpersonas = models.IntegerField()
    tipospersonas_idtipospersonas = models.IntegerField(db_column='TiposPersonas_idTiposPersonas')  # Field name made lowercase.
    tags = models.CharField(max_length=45, blank=True, null=True)
    creado = models.DateTimeField(blank=True, null=True)
    actualizado = models.DateTimeField(blank=True, null=True)
    titulo = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'peliculas'
        unique_together = (('idpeliculas', 'categoria_idcategoria', 'calificaciones_idcalificaciones', 'personas_idpersonas', 'tipospersonas_idtipospersonas'),)


class Personajes(models.Model):
    idpersonajes = models.IntegerField(primary_key=True)
    personaje = models.CharField(max_length=45, blank=True, null=True)
    estatus = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personajes'


class Personas(models.Model):
    idpersonas = models.AutoField(db_column='idPersonas', primary_key=True)  # Field name made lowercase.
    persona = models.CharField(max_length=45, blank=True, null=True)
    estatus = models.IntegerField()
    tipospersonas_idtipospersonas = models.ForeignKey('Tipospersonas', models.DO_NOTHING, db_column='TiposPersonas_idTiposPersonas')  # Field name made lowercase.
    creado = models.DateTimeField(blank=True, null=True)
    actualizado = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personas'
        unique_together = (('idpersonas', 'tipospersonas_idtipospersonas'),)


class Tipospersonas(models.Model):
    idtipospersonas = models.AutoField(db_column='idTiposPersonas', primary_key=True)  # Field name made lowercase.
    tipo_persona = models.CharField(max_length=45, blank=True, null=True)
    estatus = models.IntegerField()
    actualizado = models.DateTimeField(blank=True, null=True)
    creado = models.DateTimeField(blank=True, null=True)
    prioridad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipospersonas'

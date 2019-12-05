"""peliculas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from core import views as core_views
from portfolio import views as portfolio_views
from django.conf import settings

from api.views import *

urlpatterns = [
    path('', core_views.home, name="home"),
    path('pelicula/<int:pk>/', core_views.pelicula, name="pelicula"),
    path('admin', portfolio_views.administrador, name="admin"),
    path('admin/usuario', portfolio_views.adminusuario, name="admin_usuario"),
    path('admin/usuario/nuevo', portfolio_views.adminusuarionuevo, name="nuevoUser"),
    path('admin/usuario/update/<int:id>/', portfolio_views.adminusuarioeditar.as_view(), name="updates"),
    path('admin/usuario/eliminar/<int:id>/', portfolio_views.adminusuarioeliminar.as_view(), name="eliminarUser"),
    path('admin/permiso', portfolio_views.adminpermiso, name="admin_permisos"),
    path('admin/calificacion', portfolio_views.admincalificacion, name="admin_calif"),
    path('admin/calificacion/nuevo', portfolio_views.calificacionnew.as_view(template_name = "portfolio/calificacionesform.html"), name="calificacionnew"),
    path('admin/calificacion/editar/<int:id>/', portfolio_views.calificacionEdit.as_view(), name="editarcalif"),
    path('admin/calificacion/eliminar/<int:id>/', portfolio_views.calificacionliminar.as_view(), name="eliminarcalif"),
    path('admin/categoria', portfolio_views.admincategoria, name="admin_cat"),
    path('admin/categoria/nuevo', portfolio_views.categorianew.as_view(), name="catnew"),
    path('admin/categoria/update/<int:id>/', portfolio_views.categoriaedit.as_view(), name="cateditar"),
    path('admin/categoria/eliminar/<int:id>/', portfolio_views.categorialiminar.as_view(), name="cateli"),
    path('admin/personas', portfolio_views.adminpersonas, name="admin_persona"),
    path('admin/personas/nueva', portfolio_views.adminpersonasnew.as_view(), name="nueva_persona"),
    path('admin/personas/update/<int:id>/', portfolio_views.personasedit.as_view(), name="personaditar"),
    path('admin/personas/eliminar/<int:id>/', portfolio_views.personasiminar.as_view(), name="eli_persona"),
    path('admin/pelicula', portfolio_views.adminpelicula, name="admin_pelicula"),
    path('admin/pelicula/nueva', portfolio_views.adminpeliculanew.as_view(), name="nueva_pelicula"),
    path('admin/pelicula/update/<int:id>/', portfolio_views.peliculaedit.as_view(), name="edit_pelicula"),
    path('admin/pelicula/eliminar/<int:id>/', portfolio_views.peliculaliminar.as_view(), name="eli_pelicula"),
    path('lock/', admin.site.urls),
    path('api/', include('api.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_roo=settings.MEDIA_ROOT)

from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from .views import Home, crearPelicula, crearSala, crearFuncion, listarPelicula
from .views import listarSala, listarFuncion
from .views import editarPelicula, editarSala, editarFuncion
from .views import eliminarPelicula, eliminarSala, eliminarFuncion
from .views import *
urlpatterns = [
    path('', login_required(Home), name='index'),
    path('crear_pelicula/',login_required(crearPelicula), name = 'crear_pelicula'),
    path('crear_sala/',login_required(crearSala), name = 'crear_sala'),
    path('crear_funcion/',login_required(crearFuncion), name = 'crear_funcion'),

    path('listar_pelicula/',login_required(listarPelicula), name = 'listar_pelicula'),
    path('listar_sala/',login_required(listarSala), name = 'listar_sala'),
    path('listar_funcion/',login_required(listarFuncion), name = 'listar_funcion'),

    path('editar_pelicula/<int:id>',login_required(editarPelicula), name = 'editar_pelicula'),
    path('editar_sala/<int:id>',login_required(editarSala), name = 'editar_sala'),
    path('editar_funcion/<int:id>',login_required(editarFuncion), name = 'editar_funcion'),

    path('eliminar_pelicula/<int:id>',login_required(eliminarPelicula), name = 'eliminar_pelicula'),
    path('eliminar_sala/<int:id>',login_required(eliminarSala), name = 'eliminar_sala'),
    path('eliminar_funcion/<int:id>',login_required(eliminarFuncion), name = 'eliminar_funcion'),

]

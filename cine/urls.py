from django.urls import path
from . import views
from .views import Home, crearPelicula, crearSala, crearFuncion, listarPelicula
from .views import listarSala, listarFuncion
from .views import editarPelicula, editarSala, editarFuncion
from .views import eliminarPelicula, eliminarSala, eliminarFuncion
urlpatterns = [
    path('', Home, name='index'),
    path('crear_pelicula/',crearPelicula, name = 'crear_pelicula'),
    path('crear_sala/',crearSala, name = 'crear_sala'),
    path('crear_funcion/',crearFuncion, name = 'crear_funcion'),

    path('listar_pelicula/',listarPelicula, name = 'listar_pelicula'),
    path('listar_sala/',listarSala, name = 'listar_sala'),
    path('listar_funcion/',listarFuncion, name = 'listar_funcion'),

    path('editar_pelicula/<int:id>',editarPelicula, name = 'editar_pelicula'),
    path('editar_sala/<int:id>',editarSala, name = 'editar_sala'),
    path('editar_funcion/<int:id>',editarFuncion, name = 'editar_funcion'),

    path('eliminar_pelicula/<int:id>',eliminarPelicula, name = 'eliminar_pelicula'),
    path('eliminar_sala/<int:id>',eliminarSala, name = 'eliminar_sala'),
    path('eliminar_funcion/<int:id>',eliminarFuncion, name = 'eliminar_funcion'),

]

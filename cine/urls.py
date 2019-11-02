from django.urls import path
from . import views
from .views import Home, crearPelicula, crearSala, crearFuncion

urlpatterns = [
    path('', Home, name='index'),
    path('crear_pelicula/',crearPelicula, name = 'crear_pelicula'),
    path('crear_sala/',crearSala, name = 'crear_sala'),
    path('crear_funcion/',crearFuncion, name = 'crear_funcion'),
]

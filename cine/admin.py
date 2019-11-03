from django.contrib import admin
from .models import Pelicula, Sala, Funcion

class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('titulo','Descripcion')

admin.site.register(Pelicula)
admin.site.register(Sala)
admin.site.register(Funcion)

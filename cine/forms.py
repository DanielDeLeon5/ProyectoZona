from django import forms
from .models import Pelicula, Sala, Funcion

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['title','text']

class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ['nombre','descripcion','asientos']

class FuncionForm(forms.ModelForm):
    class Meta:
        model = Funcion
        fields = ['descripcion','horario','pelicula_id','sala_id']

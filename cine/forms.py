from django import forms
from .models import Pelicula, Sala, Funcion

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['title','text']
        widgets = {
            'title' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese nombre de la pelicula'
                }
            ),
            'text' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese una descripcion'
                }
            )
        }

class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ['nombre','descripcion','asientos']
        widgets = {
            'nombre' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese el nombre de la sala'
                }
            ),
            'descripcion' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese una descripcion'
                }
            ),
            'asientos' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese el numero de asientos',
                    'type' : 'number'
                }
            )
        }

class FuncionForm(forms.ModelForm):
    class Meta:
        model = Funcion
        fields = ['descripcion','horario','pelicula_id','sala_id']
        widgets = {
            'descripcion' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese una descripcion'
                }
            ),
            'horario' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese horario de funcion'
                }
            )

        }

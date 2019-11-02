from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Pelicula, Funcion
from .forms import PeliculaForm, SalaForm, FuncionForm

def Home(request):
    return render(request,'cine/index.html')

def crearPelicula(request):
    if request.method == "POST":
        pelicula_form = PeliculaForm(request.POST)
        if pelicula_form.is_valid():
            pelicula_form.save()
            return redirect('index')
    else:
        pelicula_form = PeliculaForm()
    return render(request,'cine/crear_pelicula.html',{'pelicula_form':pelicula_form})

def crearSala(request):
    if request.method == "POST":
        sala_form = SalaForm(request.POST)
        if sala_form.is_valid():
            sala_form.save()
            return redirect('index')
    else:
        sala_form = SalaForm()
    return render(request,'cine/crear_sala.html',{'sala_form':sala_form})

def crearFuncion(request):
    if request.method == "POST":
        funcion_form = FuncionForm(request.POST)
        if funcion_form.is_valid():
            funcion_form.save()
            return redirect('index')
    else:
        funcion_form = FuncionForm()
    return render(request,'cine/crear_funcion.html',{'funcion_form':funcion_form})

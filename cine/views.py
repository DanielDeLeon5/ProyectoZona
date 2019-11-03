from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.views.generic import TemplateView,ListView
from .models import Pelicula, Funcion, Sala
from .forms import PeliculaForm, SalaForm, FuncionForm

class Inicio(ListView):
    model = Funcion
    template_name = 'cine/index.html'
    context_object_name = 'funciones'
    queryset = Funcion.objects.all()

def Home(request):
    funciones = Funcion.objects.all()
    return render(request,'cine/index.html',{'funciones':funciones})

def crearPelicula(request):
    if request.method == "POST":
        pelicula_form = PeliculaForm(request.POST)
        if pelicula_form.is_valid():
            pelicula_form.save()
            return redirect('listar_pelicula')
    else:
        pelicula_form = PeliculaForm()
    return render(request,'cine/crear_pelicula.html',{'pelicula_form':pelicula_form})

def crearSala(request):
    if request.method == "POST":
        sala_form = SalaForm(request.POST)
        if sala_form.is_valid():
            sala_form.save()
            return redirect('listar_sala')
    else:
        sala_form = SalaForm()
    return render(request,'cine/crear_sala.html',{'sala_form':sala_form})

def crearFuncion(request):
    if request.method == "POST":
        funcion_form = FuncionForm(request.POST)
        if funcion_form.is_valid():
            funcion_form.save()
            return redirect('listar_funcion')
    else:
        funcion_form = FuncionForm()
    return render(request,'cine/crear_funcion.html',{'funcion_form':funcion_form})

def listarPelicula(request):
    peliculas = Pelicula.objects.all()
    return render(request,'cine/listar_pelicula.html',{'peliculas':peliculas})

def listarSala(request):
    salas = Sala.objects.all()
    return render(request,'cine/listar_sala.html',{'salas':salas})

def listarFuncion(request):
    funciones = Funcion.objects.all()
    return render(request,'cine/listar_funcion.html',{'funciones':funciones})

def editarPelicula(request,id):
    pelicula_form = None
    error = None
    try:
        pelicula = Pelicula.objects.get(id = id)
        if request.method == 'GET':
            pelicula_form = PeliculaForm(instance = pelicula)
        else:
            pelicula_form = PeliculaForm(request.POST, instance = pelicula)
            if pelicula_form.is_valid():
                pelicula_form.save()
            return redirect('listar_pelicula')
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'cine/crear_pelicula.html',{'pelicula_form':pelicula_form,'error':error})

def editarSala(request,id):
    sala_form = None
    error = None
    try:
        sala = Sala.objects.get(id = id)
        if request.method == 'GET':
            sala_form = SalaForm(instance = sala)
        else:
            sala_form = SalaForm(request.POST, instance = sala)
            if sala_form.is_valid():
                sala_form.save()
            return redirect('listar_sala')
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'cine/crear_sala.html',{'sala_form':sala_form,'error':error})

def editarFuncion(request,id):
    funcion_form = None
    error = None
    try:
        funcion = Funcion.objects.get(id = id)
        if request.method == 'GET':
            funcion_form = FuncionForm(instance = funcion)
        else:
            funcion_form = FuncionForm(request.POST, instance = funcion)
            if funcion_form.is_valid():
                funcion_form.save()
            return redirect('listar_funcion')
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'cine/crear_funcion.html',{'funcion_form':funcion_form,'error':error})

def  eliminarPelicula(request,id):
    pelicula = Pelicula.objects.get(id = id)
    pelicula.delete()
    return redirect('listar_pelicula')

def  eliminarSala(request,id):
    sala = Sala.objects.get(id = id)
    sala.delete()
    return redirect('listar_sala')

def  eliminarFuncion(request,id):
    funcion = Funcion.objects.get(id = id)
    funcion.delete()
    return redirect('listar_funcion')

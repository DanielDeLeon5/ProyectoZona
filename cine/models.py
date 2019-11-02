from django.db import models
from django.utils import timezone


class Pelicula(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            auto_now = True, auto_now_add = False)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Sala(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    asientos = models.IntegerField()

    def __str__(self):
        return self.nombre

class Funcion(models.Model):
    id = models.AutoField(primary_key = True)
    descripcion = models.TextField()
    horario = models.TextField()
    created_date = models.DateTimeField(
            auto_now = True, auto_now_add = False)
    pelicula_id = models.ForeignKey(Pelicula, on_delete = models.CASCADE)
    sala_id = models.ManyToManyField(Sala)

    def __str__(self):
        return self.horario

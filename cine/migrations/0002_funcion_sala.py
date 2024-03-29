# Generated by Django 2.0.13 on 2019-11-01 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField()),
                ('horario', models.TextField()),
                ('pelicula_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cine.Pelicula')),
            ],
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('asientos', models.IntegerField()),
            ],
        ),
    ]

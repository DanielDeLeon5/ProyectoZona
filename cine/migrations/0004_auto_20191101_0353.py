# Generated by Django 2.0.13 on 2019-11-01 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cine', '0003_funcion_sala_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcion',
            name='sala_id',
        ),
        migrations.AddField(
            model_name='funcion',
            name='sala_id',
            field=models.ManyToManyField(to='cine.Sala'),
        ),
    ]

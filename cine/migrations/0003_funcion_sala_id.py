# Generated by Django 2.0.13 on 2019-11-01 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cine', '0002_funcion_sala'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcion',
            name='sala_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cine.Sala'),
            preserve_default=False,
        ),
    ]
# Generated by Django 3.2.4 on 2021-08-08 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VentaEntradas', '0016_auto_20210808_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='fechaYHoraVenta',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='exposicion',
            name='fechaFin',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='exposicion',
            name='fechaFinReplanificada',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='exposicion',
            name='fechaInicio',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='exposicion',
            name='fechaInicioReplanificada',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='exposicion',
            name='horaApertura',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='exposicion',
            name='horaCierre',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='exposicion',
            name='nombre',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='obra',
            name='alto',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='obra',
            name='ancho',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='obra',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='obra',
            name='duracionExtendida',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='obra',
            name='duracionResumida',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='obra',
            name='fechaCreacion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='obra',
            name='fechaPrimerIngreso',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='obra',
            name='nombre',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='obra',
            name='peso',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reservavisita',
            name='cantidadAlumnos',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reservavisita',
            name='cantidadAlumnosConfirmada',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reservavisita',
            name='duracionEstimada',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reservavisita',
            name='fechaHoraCreacion',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reservavisita',
            name='fechaHoraReserva',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reservavisita',
            name='fechaYHoraFinReal',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reservavisita',
            name='fechaYHoraInicioReal',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sede',
            name='cantMaxPorGuia',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sede',
            name='diaFin',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sede',
            name='diaInicio',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sede',
            name='horaApetura',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sede',
            name='horaCierre',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sesion',
            name='fechaFin',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sesion',
            name='fechaInicio',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sesion',
            name='horaFin',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sesion',
            name='horaInicio',
            field=models.TimeField(blank=True, null=True),
        ),
    ]

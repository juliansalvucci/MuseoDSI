# Generated by Django 3.2.4 on 2021-08-08 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('VentaEntradas', '0014_auto_20210808_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='calle',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='codigoValidacion',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='cuit',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='dni',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fechaIngreso',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fechaNacimiento',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='mail',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='numero',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='sede',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sd', to='VentaEntradas.sede', verbose_name='Sede'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='telefono',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='monto',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='sede',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sede', to='VentaEntradas.sede', verbose_name='Sede'),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='tarifa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tarifa', to='VentaEntradas.tarifa', verbose_name='Tarifa'),
        ),
        migrations.AlterField(
            model_name='exposicion',
            name='fechaFin',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='exposicion',
            name='fechaFinReplanificada',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='exposicion',
            name='fechaInicio',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='exposicion',
            name='fechaInicioReplanificada',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='exposicion',
            name='nombre',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='obra',
            name='alto',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='obra',
            name='ancho',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='obra',
            name='descripcion',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='obra',
            name='fechaCreacion',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='obra',
            name='fechaPrimerIngreso',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='obra',
            name='nombre',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='obra',
            name='peso',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='obra',
            name='valuacion',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='reservavisita',
            name='cantidadAlumnos',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='reservavisita',
            name='cantidadAlumnosConfirmada',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='reservavisita',
            name='duracionEstimada',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='reservavisita',
            name='fechaHoraCreacion',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='reservavisita',
            name='fechaHoraReserva',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='reservavisita',
            name='sede',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Sede', to='VentaEntradas.sede', verbose_name='Sede'),
        ),
        migrations.AlterField(
            model_name='sede',
            name='cantMaxPorGuia',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sesion',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='usuario', to='VentaEntradas.usuario', verbose_name='Usuario'),
        ),
        migrations.AlterField(
            model_name='tipodeentrada',
            name='nombre',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='tipodevisita',
            name='nombre',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='empleado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='emp', to='VentaEntradas.empleado', verbose_name='empleado'),
        ),
    ]

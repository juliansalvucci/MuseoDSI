# Generated by Django 3.2.4 on 2021-07-03 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('VentaEntradas', '0008_obra'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservaVisita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidadAlumnos', models.IntegerField(help_text='Cantidad de alumnos', verbose_name='cantidadAlumnos')),
                ('cantidadAlumnosConfirmada', models.IntegerField(help_text='Cantidad de alumnos confirmada', verbose_name='cantidadAlumnosConfirmada')),
                ('duracionEstimada', models.IntegerField(help_text='Duración estimada', verbose_name='duracionEstimada')),
                ('fechaHoraCreacion', models.DateTimeField(help_text='Fecha y hora de creación', verbose_name='fechaHoraCreacion')),
                ('fechaHoraReserva', models.DateTimeField(help_text='Fecha y hora de reserva', verbose_name='fechaHoraReserva')),
                ('horaInicioReal', models.TimeField(help_text='Hora de inicio real', verbose_name='horaInicioReal')),
                ('horaFinReal', models.TimeField(help_text='Hora de fin real', verbose_name='horaFinReal')),
                ('numeroReserva', models.IntegerField(help_text='Numero de reserva', verbose_name='numeroRserva')),
                ('sede', models.ForeignKey(help_text='Sede', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Sede', to='VentaEntradas.sede', verbose_name='Sede')),
            ],
        ),
    ]
# Generated by Django 3.2.4 on 2021-08-08 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('VentaEntradas', '0017_auto_20210808_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleexposicion',
            name='obra',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='obr', to='VentaEntradas.obra', verbose_name='Obra'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='sede',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sd', to='VentaEntradas.sede', verbose_name='Sede'),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='monto',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='sede',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sede', to='VentaEntradas.sede', verbose_name='Sede'),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='tarifa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tarifa', to='VentaEntradas.tarifa', verbose_name='Tarifa'),
        ),
        migrations.AlterField(
            model_name='exposicion',
            name='empleado',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='e', to='VentaEntradas.empleado', verbose_name='Empleado'),
        ),
        migrations.AlterField(
            model_name='obra',
            name='valuacion',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='reservavisita',
            name='sede',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Sede', to='VentaEntradas.sede', verbose_name='Sede'),
        ),
        migrations.AlterField(
            model_name='sesion',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='usuario', to='VentaEntradas.usuario', verbose_name='Usuario'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='empleado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='emp', to='VentaEntradas.empleado', verbose_name='empleado'),
        ),
    ]

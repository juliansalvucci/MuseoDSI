# Generated by Django 3.2.4 on 2021-07-03 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VentaEntradas', '0002_tipodevisita'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido', models.TextField(help_text='Apellido de empleado', max_length=200, verbose_name='apellido')),
                ('nombre', models.TextField(help_text='Nombre de empleado', max_length=200, verbose_name='nombre')),
                ('codigoValidacion', models.IntegerField(help_text='Código de validación', verbose_name='CodigoValidacion')),
                ('cuit', models.IntegerField(help_text='CUIT', verbose_name='cuit')),
                ('dni', models.IntegerField(help_text='DNI', verbose_name='dni')),
                ('calle', models.TextField(help_text='Calle', max_length=200, verbose_name='calle')),
                ('numero', models.IntegerField(help_text='Número', verbose_name='numero')),
                ('fechaIngreso', models.DateField(help_text='Fecha de ingreso', verbose_name='fechaIngreso')),
                ('fechaNacimiento', models.DateField(help_text='Fecha de nacimiento', verbose_name='fechaNacimiento')),
                ('mail', models.EmailField(help_text='Mail', max_length=254, verbose_name='mail')),
                ('telefono', models.IntegerField(help_text='Telefono', verbose_name='telefono')),
            ],
        ),
    ]

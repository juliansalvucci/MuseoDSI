# Generated by Django 3.2.4 on 2021-07-03 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoDeEntrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(help_text='Nombre de tipo de entrada', max_length=200, verbose_name='nombre')),
            ],
        ),
    ]

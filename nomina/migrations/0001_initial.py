# Generated by Django 4.0.3 on 2022-03-10 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('rfc', models.CharField(max_length=13, verbose_name='RFC')),
                ('curp', models.CharField(max_length=18, verbose_name='CURP')),
                ('puesto', models.CharField(max_length=30, verbose_name='Puesto')),
                ('sueldo', models.DecimalField(decimal_places=2, max_digits=7)),
                ('fecha_ingreso', models.DateField()),
            ],
        ),
    ]

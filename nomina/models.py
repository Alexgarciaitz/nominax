from django.db import models

# Create your models here.


class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=100)
    rfc = models.CharField('RFC', max_length=13)
    curp = models.CharField('CURP', max_length=18)
    puesto = models.CharField('Puesto', max_length=30)
    sueldo = models.DecimalField(max_digits=7 ,decimal_places=2)
    fecha_ingreso = models.DateField()
    #para imprimir un objeto
    def __str__(self):
        return self.nombre

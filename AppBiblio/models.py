from django.db import models

# Create your models here.

class Usuario(models.Model):
    
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    Ingreso = models.IntegerField()
    documento = models.IntegerField()
    
class Libro(models.Model):
    
    titulo = models.CharField(max_length=40)
    autor = models.CharField(max_length=40)
    editorial = models.CharField(max_length=40)
    inventario = models.IntegerField(default=1)
    
class Prestamo(models.Model):
    lib = models.IntegerField(default=1)
    user = models.IntegerField(default=1)
    fecha = models.DateField()
    devuelto = models.BooleanField(default=False)
    
from django.db import models

# Create your models here.
class alumno(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=65, default="")
    direccion = models.CharField(max_length=50, default="")
    telefono = models.CharField(max_length=9, default="")
    
class materia(models.Model):
    codigo = models.CharField(max_length=2)
    nombre = models.CharField(max_length=65)
    uv = models.SmallIntegerField(max_length=1)
    
class Docente(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=65)
    telefono = models.CharField(max_length=9)
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Perfil(models.Model):
    nombre = models.CharField(max_length=30)
    imagen = models.ImageField()
    link = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    email = models.EmailField()
    contraseña = models.CharField(max_length=30)

class Usuario(User):
    nombre = models.CharField(max_length=30)
    imagen = models.ImageField()
    link = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    mail = models.EmailField()
    contraseña = models.CharField(max_length=30)
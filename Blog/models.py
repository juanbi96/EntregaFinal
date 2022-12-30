from django.db import models

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=60)
    subtitulo = models.CharField(max_length=120)
    cuerpo = models.CharField(max_length=1000)
    autor = models.CharField(max_length=30)
    fecha = models.DateField()
    imagen = models.ImageField()

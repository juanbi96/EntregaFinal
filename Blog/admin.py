from django.contrib import admin
from .models import *
# Register your models here.

#Hay que registrar los modelos con admin.site.register(NombreDelModelo)

admin.site.register(Post)
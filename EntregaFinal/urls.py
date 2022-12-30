"""EntregaFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Login.views import *
from Registro.views import *
from Blog.views import *
from Registro.forms import *
from Perfiles.views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", inicio, name="inicio"),
    path('admin/', admin.site.urls),
    path('registro/', registrarse, name="registrarse"),
    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('about/', about_me, name="about_me"),
    path('pages/', pages, name="pages"),
    path('perfil/', perfil, name ="perfil"),
    path('agregar_post/', agregar_post, name="agregar_post"),
    path('eliminar_post/<id>', eliminar_post, name="eliminar_post"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
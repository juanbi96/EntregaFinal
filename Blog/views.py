from django.shortcuts import render
from .forms import *
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):
    return render(request, "inicio.html", {"mensaje_inicio": "Bienvenido a Forum"})

def about_me(request):
    return render(request, "about_me.html")

@login_required
def agregar_post(request):
    if request.method == "POST":
        form_post = NuevoPost(request.POST)
        if form_post.is_valid():
            datos = form_post.cleaned_data
            titulo=datos["titulo"]
            subtitulo=datos["subtitulo"]
            cuerpo=datos["cuerpo"]
            autor=datos["autor"]
            fecha=datos["fecha"]
            imagen=datos["imagen"]
            form_post= Post(titulo=titulo, subtitulo=subtitulo, cuerpo=cuerpo, autor=autor, fecha=fecha, imagen=imagen)
            form_post.save()
            return render(request, "inicio.html", {"mensaje_exito": "El post ha sido creado exitosamente"})
        else:
            formulario_vacio = NuevoPost()
            return render(request, "agregar_post.html", {"form":formulario_vacio})
    else:
        formulario_vacio = NuevoPost()
        return render(request, "agregar_post.html", {"form":formulario_vacio})

def pages(request):
    posts=Post.objects.all()
    return render(request, "pages.html", {"posts":posts})

@login_required
def eliminar_post(request, id):
    post=Post.objects.get(id=id)
    Post.delete()
    posts=Post.objects.all()
    return render(request, "pages.html", {"mensaje_eliminado":"El post ha sido eliminado correctamente."})

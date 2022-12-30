from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import *

# Create your views here.

def perfil(request):
    if request.method=='POST':
        form=PerfilForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            form.save()
            return render(request, "perfil.html", {"mensaje":"El perfil ha sido actualizado correctamente"})
        else:
            form_vacio=PerfilForm(request.POST)
            return render(request, "perfil.html", {"mensaje_error":"Por favor, ingrese los datos correctamente."})
    else:
        PerfilForm(request.POST)
        return render(request, "perfil.html")

from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistroUsuarioForm

# Create your views here.

def registrarse(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username") # Procesa la información del formulario
            form.save()                                # Crea un nuevo usuario y lo guarda en la base de datos 
            return render(request, "inicio.html", {"mensaje":"Usuario creado exitosamente"})  # Redirige al usuario a la página de inicio de sesión
        else:
            return render(request, "registro.html", {'form': form, 'mensaje':"Error al crear el usuario"})
    else:
        form = RegistroUsuarioForm()
    return render(request, "registro.html")

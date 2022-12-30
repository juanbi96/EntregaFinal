from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

def login_request(request):
    if request.method == "POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")

            usuario=authenticate(username=username, password=password)   #Trae usuario de la BD con ese username y password.

            if usuario is not None:
                login(request, usuario)
                return render(request, "inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "login.html", {"mensaje_error":"Usuario o contraseña incorrectos. Por favor, intente de nuevo", "form":form})

        else:
            return render(request, "login.html", {"mensaje_error":"Usuario o contraseña incorrectos. Por favor, intente de nuevo", "form":form})
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form":form})